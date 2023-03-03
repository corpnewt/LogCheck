#!/usr/bin/env python
import sys, os, binascii, json, argparse, re
from collections import OrderedDict
from Scripts import plist, utils

class LogCheck:
    def __init__(self):
        self.u = utils.Utils("LogCheck")
        if os.name=="nt":
            self.min_h = 30
            self.min_w = 120
        else:
            self.min_h = 24
            self.min_w = 80
        self.booter_bug_start = "068"
        self.booter_bug_stop = "090"
        self.booter_quirks = {
            "ALRBL": "AllowRelocationBlock",
            "RTDFRG": "AvoidRuntimeDefrag",
            "DEVMMIO": "DevirtualiseMmio",
            "NOSU": "DisableSingleUser",
            "NOVRWR": "DisableVariableWrite",
            "NOSB": "ProtectSecureBoot",
            "FBSIG": "ForceBooterSignature",
            "NOHBMAP": "DiscardHibernateMap",
            "SMSLIDE": "EnableSafeModeSlide",
            "WRUNPROT": "EnableWriteUnprotector",
            "FEXITBS": "ForceExitBootServices",
            "PRMRG": "ProtectMemoryRegions",
            "CSLIDE": "ProvideCustomSlide",
            "MSLIDE": "ProvideMaxSlide",
            "PRSRV": "ProtectUefiServices",
            "RBMAP": "RebuildAppleMemoryMap",
            "VMAP": "SetupVirtualMap",
            "APPLOS": "SignalAppleOS",
            "RTPERMS": "SyncRuntimePermissions",
            "ARBAR": "ResizeAppleGpuBars",
            "RBIO": "ResizeUsePciRbIo"
        }
        self.bugged_booter_quirks = {}
        # Correct for a logging bug introduced in 0.6.8 - first create a shallow copy
        for x in self.booter_quirks:
            self.bugged_booter_quirks[x] = self.booter_quirks[x]
        # Update our bugged values
        self.bugged_booter_quirks["NOVRWR"] = "ForceBooterSignature"
        self.bugged_booter_quirks["NOSB"] = "DisableVariableWrite"
        self.bugged_booter_quirks["FBSIG"] = "ProtectSecureBoot"

    def un_hex(self, value, swap = True, strip_null = True):
        h = value
        if value.lower().startswith("0x"): h = value[2:]
        h = "".join([x for x in h.upper() if x in "0123456789ABCDEF"])
        if len(h) % 2: return value # Not even
        if swap or strip_null:
            # Time for a stupidly long one liner just because
            h = "".join(["" if h[i:i+2]=="00" and strip_null else h[i:i+2] for i in range(0,len(h),2)][::-1 if swap else None])
        try: return binascii.unhexlify(h.encode()).decode()
        except: return value

    def check_booter_bork(self, oc_version):
        return self.booter_bug_start <= oc_version.split("-")[1] < self.booter_bug_stop
        try: return self.booter_bug_start <= oc_version.split("-")[1] < self.booter_bug_stop
        except: return True

    def map_booter_quirk(self, quirk, oc_version):
        # Split the quirk and value for mapping
        try: q,v = quirk.split(" -> ")
        except: return quirk # Broke - bail
        d = self.bugged_booter_quirks if self.check_booter_bork(oc_version) else self.booter_quirks
        return "{} -> {}".format(d.get(q,q),v)

    def get_log(self):
        while True:
            self.u.resize(self.min_w,self.min_h)
            self.u.head()
            print("")
            print("Please drag and drop your opencore-[timestamp].txt log here.")
            print("")
            print("Make sure you are using a debug build of OpenCore!")
            print("")
            print("If you are building an MMIO whitelist, make sure to enable the")
            print("DevirtualiseMmio quirk in your config.plist!")
            print("")
            print("Q. Quit")
            print("")
            menu = self.u.grab("Please drag and drop the log here:  ")
            if not menu: continue
            if menu.lower() == "q":
                self.u.custom_quit()
            l_path = self.u.check_path(menu)
            if not l_path:
                self.error(title="Invalid Path",message="Could not locate:\n{}".format(menu))
                continue
            if not os.path.isfile(l_path):
                self.error(title="Invalid Path",message="The following is a directory, not an OpenCore log:\n{}".format(menu))
                continue
            log,error = self.load_log(l_path)
            if error:
                self.error(title="Error Loading File",message="Could not read file:\n{}".format(error))
                continue
            return log

    def load_log(self, log_path=None):
        if not log_path: return (None,None)
        # Should have the log - load it and save our path and info
        try:
            with open(log_path,"r") as f:
                log = f.read().replace("\r","")
            return (log,None)
        except Exception as e:
            return (None,e)
        return (None,None)

    def parse_log(self, log):
        # Let's walk the log and extract info
        l_info = {}
        last_hda_controller = None
        last_codec = None
        last_cpu = None
        for line in log.split("\n"):
            if "HDA: Connecting controller - " in line:
                # Got an audio controller - save it
                controllers = l_info.get("audio_controllers",{})
                try:
                    last_hda_controller = line.split(" - ")[-1]
                    controllers[last_hda_controller] = {} # Placeholder
                    l_info["audio_controllers"] = controllers
                except: pass
            elif "HDA: Connecting codec " in line and last_hda_controller is not None:
                # Got a codec and controller - save it
                controllers = l_info.get("audio_controllers",{})
                controller  = controllers.get(last_hda_controller,{})
                try:
                    last_codec = line.split("HDA: Connecting ")[1].capitalize()
                    controller[last_codec] = []
                    controllers[last_hda_controller] = controller
                    l_info["audio_controllers"] = controllers
                except: pass
            elif "HDA:  | " in line \
                and last_codec is not None \
                and last_hda_controller is not None \
                and any((x in line for x in ("Codec ID: ","Codec name: "," is an output "))):
                # We got some codec info
                controllers = l_info.get("audio_controllers",{})
                controller  = controllers.get(last_hda_controller,{})
                codec       = controller.get(last_codec,[])
                try:
                    if " is an output " in line: # Got an output specifier
                        output_mask = int(line.split("(bitmask ")[1].split(")")[0])
                        output_bit  = len("{:b}".format(output_mask))-1
                        value = "Output at bit-{} (bitmask {})".format(output_bit,output_mask)
                    else: # Got some other info
                        value = line.split("HDA:  | ")[1]
                    codec.append(value)
                    controller[last_codec] = codec
                    controllers[last_hda_controller] = controller
                except: pass
            elif "OCABC: MMIO devirt " in line:
                mmio_devirt = l_info.get("mmio_devirt",[])
                try:
                    addr = line.split("OCABC: MMIO devirt ")[1].split(" (")[0]
                    mmio_devirt.append("{} ({})".format(addr,int(addr,16)))
                    l_info["mmio_devirt"] = mmio_devirt
                except: pass
            elif "OC: Current version is " in line:
                # Got the version
                try: l_info["oc_version"] = line.split("OC: Current version is ")[1]
                except: pass
            elif "OCCPU: Found " in line:
                # Got a CPU
                cpus = l_info.get("cpus",[])
                try:
                    cpus.append({"name":line.split("OCCPU: Found ")[1].strip()})
                    l_info["cpus"] = cpus
                except: pass
            elif "OCCPU: Pkg " in line and l_info.get("cpus"):
                # Apply the CPU info to the last CPU added
                last_cpu = l_info["cpus"][-1] # Get it explicitly as we know it exists
                try: last_cpu["cores_threads"] = line.split("Cores ")[1].replace(" Threads ","/")
                except: pass
            elif "OCCPU: Detected Apple Processor Type: " in line and l_info.get("cpus"):
                # Apply the CPU info to the last CPU added
                last_cpu = l_info["cpus"][-1] # Get it explicitly as we know it exists
                try: last_cpu["apple_processor_type"] = line.split("OCCPU: Detected Apple Processor Type: ")[1]
                except: pass
            elif "OCCPU: " in line and " CFG Lock " in line:
                try: l_info["cfg_lock"] = line.split()[-1] != "0"
                except: pass
            elif "OCVAR: Locate emulated NVRAM protocol - " in line:
                try: l_info["emulated_nvram"] = line.split("OCVAR: Locate emulated NVRAM protocol - ")[1] != "Not Found"
                except: pass
            elif "OC: Setting devprop " in line:
                device_properties = l_info.get("device_properties_add",{})
                try:
                    path = line.split("OC: Setting devprop ")[1].split(":")[0]
                    props = device_properties.get(path,[])
                    props.append(" - ".join(line.split(":")[-1].split(" - ")[:-1]))
                    device_properties[path] = props
                    l_info["device_properties_add"] = device_properties
                except: pass
            elif "OC: Removing devprop " in line:
                device_properties = l_info.get("device_properties_delete",{})
                try:
                    path = line.split("OC: Removing devprop ")[1].split(":")[0]
                    props = device_properties.get(path,[])
                    props.append(" - ".join(line.split(":")[-1].split(" - ")[:-1]))
                    delete[path] = props
                    l_info["device_properties_delete"] = device_properties
                except: pass
            elif "OCVAR: Setting NVRAM " in line:
                nvram = l_info.get("nvram_add",{})
                try:
                    guid = line.split(" NVRAM ")[1].split(":")[0]
                    value = line.split(guid+":")[1]
                    value = " - ".join(value.split(" - ")[:-1])
                    values = nvram.get(guid,[])
                    values.append(value)
                    nvram[guid] = values
                    l_info["nvram_add"] = nvram
                except: pass
            elif "OC: Deleting NVRAM " in line or "OC: Not deleting NVRAM " in line:
                nvram = l_info.get("nvram_delete",{})
                try:
                    guid = line.split(" NVRAM ")[1].split(":")[0]
                    value = line.split(guid+":")[1]
                    sep = ", " if value.endswith(", matches add") else " - "
                    value = sep.join(value.split(sep)[:-1])
                    values = nvram.get(guid,[])
                    values.append(value)
                    nvram[guid] = values
                    l_info["nvram_delete"] = nvram
                except: pass
            elif "OC: Driver " in line and " is being loaded..." in line:
                uefi_drivers_loaded = l_info.get("uefi_drivers_loaded",[])
                try:
                    uefi_drivers_loaded.append(line.split("OC: Driver ")[1].split(" at ")[0])
                    l_info["uefi_drivers_loaded"] = uefi_drivers_loaded
                except: pass
            elif "OC: Driver " in line and " is successfully loaded!" in line:
                uefi_drivers = l_info.get("uefi_drivers",[])
                try:
                    uefi_drivers.append(line.split("OC: Driver ")[1].split(" at ")[0])
                    l_info["uefi_drivers"] = uefi_drivers
                except: pass
            elif ("OCA: Applying " in line or "OC: Applying " in line) and " byte ACPI patch " in line:
                acpi_patch = l_info.get("acpi_patch",[])
                # TODO:
                # Update if OC logs comments for ACPI patches in the future
                sep = "OCA: Applying " if "OCA: Applying " in line else "OC: Applying "
                try:
                    acpi_patch.append(line.split(sep)[1])
                    l_info["acpi_patch"] = acpi_patch
                except: pass
            elif "OCA: Inserted table " in line:
                acpi_add = l_info.get("acpi_add",[])
                try:
                    table_name = self.un_hex(line.split("(")[1].split(")")[0])
                    table_oem  = self.un_hex(line.split("(OEM ")[1].split(")")[0])
                    acpi_add.append("{} -> {}".format(table_name,table_oem))
                    l_info["acpi_add"] = acpi_add
                except: pass
            elif "OCA: Deleting table " in line:
                acpi_delete = l_info.get("acpi_delete",[])
                try:
                    table_name = self.un_hex(line.split("(")[1].split(")")[0])
                    table_oem  = self.un_hex(line.split("(OEM ")[1].split(")")[0])
                    acpi_delete.append("{} -> {}".format(table_name,table_oem))
                    l_info["acpi_delete"] = acpi_delete
                except: pass
            elif "OCA: Replaced DSDT of " in line:
                acpi_add = l_info.get("acpi_add",[])
                acpi_add.append("DSDT")
                l_info["acpi_add"] = acpi_add
            elif "OCSMB: Current SMBIOS " in line:
                try: l_info["current_smbios"] = line.split("OCSMB: Current SMBIOS ")[1].strip()
                except: pass
            elif "OC: New SMBIOS: " in line:
                try: l_info["target_smbios"] = line.split("OC: New SMBIOS: ")[1]
                except: pass
            elif "OCB: Registering entry " in line:
                entries = l_info.get("picker_entries",[])
                try:
                    entry = " (T:".join(line.split("OCB: Registering entry ")[1].split(" (T:")[:-1])
                    if not entry in entries:
                        entries.append(entry)
                        l_info["picker_entries"] = entries
                except: pass
            elif "OCB: Should boot from " in line:
                try: l_info["booted_entry"] = " (T:".join(line.split("OCB: Should boot from ")[1].split(" (T:")[:-1])
                except: pass
            elif "OCOS: OS set: " in line:
                try: l_info["booted_os"] = line.split("OCOS: OS set: ")[1]
                except: pass
            elif "OCAK: Read kernel version " in line:
                try: l_info["booted_kernel"] = line.split("OCAK: Read kernel version ")[1].split(" (")[0]
                except: pass
            elif "OC: " in line and " injection " in line and not " injection skips " in line:
                if ") - " in line: # Result of injection
                    if not line.endswith(" - Success"):
                        kernel_add_failed = l_info.get("kernel_add_failed",[])
                        try:
                            failed_kext = " (".join(line.split(" injection ")[1].split(" (")[:-1])
                            reason      = line.split(" - ")[-1]
                            kernel_add_failed.append("{} - {}".format(failed_kext,reason))
                            l_info["kernel_add_failed"] = kernel_add_failed
                        except: pass
                else: # Likely has the kext version?
                    kernel_add = l_info.get("kernel_add",[])
                    try:
                        kernel_add.append(line.split(" injection ")[1])
                        l_info["kernel_add"] = kernel_add
                    except: pass
            elif "OC: " in line and " blocker " in line and not " blocker skips " in line:
                kernel_block = l_info.get("kernel_block",[])
                try:
                    kext = " (".join(" for ".join(line.split(" for ")[1:]).split(" (")[:-1])
                    kernel_block.append(kext)
                    l_info["kernel_block"] = kernel_block
                except: pass
            elif "OCABC: MAT support is " in line:
                try: l_info["mat_support"] = line.split("OCABC: MAT support is ")[1] != "0"
                except: pass
            elif "OCABC: All slides are usable!" in line:
                l_info["all_slides"] = True
            elif "OCABC: Only " in line and " slide values are usable!" in line:
                l_info["all_slides"] = False
                try: l_info["usable_slides"] = line.split("OCABC: Only ")[1].split(" slide values")[0]
                except: pass
            elif "OCABC: Valid slides - " in line:
                l_info["all_slides"] = False
                try: l_info["valid_slides"] = line.split("OCABC: Valid slides - ")[1]
                except: pass
            elif "AAPL: #[EB|MBA:NV] " in line:
                try: l_info["boot-args"] = '">'.join('"<'.join(line.split('<"')[1:]).split('">')[:-1])
                except: pass
            elif "OCABC: " in line and any((x in line for x in self.bugged_booter_quirks)):
                booter_quirks = l_info.get("booter_quirks",[])
                try: # h[i:i+2] for i in range(0,len(h),2)
                    quirks = line.split("OCABC: ")[1].split()
                    booter_quirks.extend(["{} -> {}".format(*quirks[i:i+2]) for i in range(0,len(quirks),2)])
                    l_info["booter_quirks"] = booter_quirks
                except: pass
        # Time to organize the data!
        l_info["uefi_drivers_failed"] = [x for x in l_info.get("uefi_drivers",[]) if not x in l_info.get("uefi_drivers_loaded",[])]
        # Remap the booter quirks to their "nice" names - and account for borked order as of 0.6.8
        if l_info.get("booter_quirks") and l_info.get("oc_version"):
            save_key = "booter_quirks_repaired" if self.check_booter_bork(l_info["oc_version"]) else "booter_quirks"
            mapped_quirks = sorted([self.map_booter_quirk(q,l_info["oc_version"]) for q in l_info.pop("booter_quirks",[])],key=lambda x:x.lower())
            l_info[save_key] = mapped_quirks
        # Let's migrate the dict to a new one with a preset order of keys
        # to make the flow of checking info a little easier
        key_order = (
            "oc_version",
            "booted_os",
            "booted_kernel",
            "cpus",
            "current_smbios",
            "target_smbios",
            "boot-args",
            "cfg_lock",
            "mat_support",
            "mmio_devirt",
            "all_slides",
            "usable_slides",
            "valid_slides",
            "audio_controllers",
            "acpi_add",
            "acpi_delete",
            "acpi_patch",
            "booter_quirks",
            "booter_quirks_repaired",
            "device_properties_add",
            "device_properties_delete",
            "kernel_add",
            "kernel_add_failed",
            "kernel_block",
            "emulated_nvram",
            "nvram_add",
            "nvram_delete",
            "uefi_drivers",
            "uefi_drivers_failed",
            "picker_entries",
            "booted_entry"
        )
        l_organized = OrderedDict()
        for key in key_order:
            if key in l_info and l_info[key] != []:
                l_organized[key] = l_info[key]
        return l_organized

    def main(self):
        while True:
            l_organized = self.parse_log(self.get_log())
            # Got the info - set the window size to show it
            json_info = json.dumps(l_organized,indent=2) if l_organized else "No info found in the passed log!"
            h = max(len(json_info.split("\n"))+6,self.min_h)
            w = max(max([len(x) for x in json_info.split("\n")]),self.min_w)
            self.u.resize(w,h)
            self.u.head("OpenCore Log Results")
            print("")
            print(json_info)
            print("")
            self.u.grab("Press [enter] to return")
            continue

    def error(self,title = None, message = None):
        self.u.head(title)
        print("")
        print(message)
        print("")
        self.u.grab("Press [enter] to return...")

    def cli_main(self,input_file=None,output_file=None,match_keys=None,skip_keys=None):
        # Let's make sure our input file exists
        i = self.u.check_path(input_file)
        if not i:
            print("'{}' does not exist!".format(input_file))
            exit(1)
        if os.path.isdir(i):
            print("'{}' is a directory!".format(input_file))
        # Try to load it
        log,error = self.load_log(input_file)
        if error:
            print("Could not read file:\n{}".format(error))
            exit(1)
        # We have the log - parse it
        l_organized = self.parse_log(log)
        # Let's see if we have regex to worry about
        if match_keys:
            try:
                r = re.compile(match_keys)
            except Exception as e:
                print("Could not compile match-keys regex:\n{}".format(e))
                exit(1)
            for key in list(l_organized):
                if not r.search(key):
                    l_organized.pop(key,None)
        if skip_keys:
            try:
                s = re.compile(skip_keys)
            except Exception as e:
                print("Could not compile skip-keys regex:\n{}".format(e))
                exit(1)
            for key in list(l_organized):
                if s.search(key):
                    l_organized.pop(key,None)
        # Let's print to stdout if no output path - or write to a file
        if output_file:
            try:
                json.dump(l_organized,open(output_file,"w"),indent=2)
            except Exception as e:
                print("Could not save to '{}':\n{}".format(output_file,e))
                exit(1)
        else:
            print(json.dumps(l_organized,indent=2))

if __name__ == '__main__':
    # Setup the cli args
    parser = argparse.ArgumentParser(prog="LogCheck", description="Py script to scrape high level info from an opencore log")
    parser.add_argument("-i", "--input", help="path to the input opencore-[timestamp].txt log file")
    parser.add_argument("-o", "--output", help="path to the output json file - omit for stdout (requires --input)")
    parser.add_argument("-m", "--match-keys", help="regex pattern for top level keys to include (cli only)")
    parser.add_argument("-s", "--skip-keys", help="regex pattern for top level keys to exclude (cli only)")

    args = parser.parse_args()

    m = LogCheck()
    if args.input: # Got cli args
        m.cli_main(input_file=args.input,output_file=args.output,match_keys=args.match_keys,skip_keys=args.skip_keys)
    else:
        m.main()
