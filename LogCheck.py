#!/usr/bin/env python
import sys, os, binascii, json
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

    def main(self):
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
            # Should have the log - load it and save our path and info
            try:
                with open(l_path,"r") as f:
                    log = f.read()
            except Exception as e:
                self.error(title="Error Loading File",message="Could not read file:\n{}".format(e))
                continue # Invalid file
            # Let's walk the log and extract info
            l_info = {}
            loaded_drivers = []
            drivers = []
            for line in log.split("\n"):
                # MMIO Devirt checks
                if "OCABC: MMIO devirt " in line:
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
                        cpus.append(line.split("OCCPU: Found ")[1].strip())
                        l_info["cpus"] = cpus
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
                    try:
                        drivers.append(line.split("OC: Driver ")[1].split(" at ")[0])
                    except: pass
                elif "OC: Driver " in line and " is successfully loaded!" in line:
                    try:
                        loaded_drivers.append(line.split("OC: Driver ")[1].split(" at ")[0])
                    except: pass
                elif "OCA: Applying " in line and " byte ACPI patch " in line:
                    acpi_patch = l_info.get("acpi_patch",[])
                    # TODO:
                    # Update if OC logs comments for ACPI patches in the future
                    try:
                        acpi_patch.append(line.split("OCA: Applying ")[1])
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
                elif "OC: New SMBIOS: " in line:
                    try: l_info["smbios"] = line.split("OC: New SMBIOS: ")[1]
                    except: pass
                elif "OCB: Registering entry " in line:
                    entries = l_info.get("picker_entries",[])
                    try:
                        entry = " (T:".join(line.split("OCB: Registering entry ")[1].split(" (T:")[:-1])
                        if not entry in entries:
                            entries.append(entry)
                            l_info["picker_entries"] = entries
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
                    try: l_info["mat_support"] = line.split("OCABC: MAT support is ")[1]
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
            # Time to organize the data!
            failed_drivers = [x for x in drivers if not x in loaded_drivers]
            if loaded_drivers: l_info["uefi_drivers"] = loaded_drivers
            if failed_drivers: l_info["uefi_drivers_failed"] = failed_drivers
            # Let's migrate the dict to a new one with a preset order of keys
            # to make the flow of checking info a little easier
            key_order = (
                "oc_version",
                "booted_os",
                "booted_kernel",
                "cpus",
                "smbios",
                "boot-args",
                "mat_support",
                "mmio_devirt",
                "all_slides",
                "usable_slides",
                "valid_slides",
                "acpi_add",
                "acpi_delete",
                "acpi_patch",
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
            )
            l_organized = {}
            for key in key_order:
                if key in l_info: l_organized[key] = l_info[key]
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

if __name__ == '__main__':
    m = LogCheck()
    m.main()
