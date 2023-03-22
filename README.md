# LogCheck
Py script to scrape high level info from an opencore log

```
usage: LogCheck [-h] [-o OUTPUT] [-m MATCH_KEYS] [-s SKIP_KEYS] [input_file ...]

Py script to scrape high level info from an opencore log

positional arguments:
  input_file            path to the input opencore-[timestamp].txt log file

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to the output json file - omit for stdout (requires an input_file)
  -m MATCH_KEYS, --match-keys MATCH_KEYS
                        regex pattern for top level keys to include (cli only)
  -s SKIP_KEYS, --skip-keys SKIP_KEYS
                        regex pattern for top level keys to exclude (cli only)
```

<details>
<summary>Example OpenCore Log</summary>
  <pre>00:000 00:000 BS: Starting OpenCore application...
00:000 00:000 BS: Booter path - \EFI\BOOT\BOOTX64.EFI
00:000 00:000 OCFS: Trying to locate filesystem on 91CA6518 93741E18
00:000 00:000 OCFS: Filesystem DP - \EFI\BOOT\BOOTX64.EFI
00:000 00:000 BS: Trying to load OpenCore image...
00:000 00:000 BS: Relative path - EFI
00:000 00:000 BS: Startup path - EFI\OpenCore.efi (0)
00:000 00:000 BS: Fallback to absolute path - EFI\OC\OpenCore.efi
00:000 00:000 BS: Read OpenCore image of 995328 bytes
00:000 00:000 OCM: Loaded image at 93736898 handle
00:000 00:000 OCM: Loaded image has DeviceHandle 91CA6518 FilePath 901FFF98 ours DevicePath 93738E98
00:000 00:000 OCCPU: TSC Adjust 0
00:000 00:000 OCCPU: Queried Core Crystal Clock Frequency    24000000Hz
00:000 00:000 OCCPU: CPUFrequencyFromART  3504000000Hz  3504MHz = 24000000 * 292 / 2
00:000 00:000 OC: Starting OpenCore...
00:000 00:000 OC: Booter path - EFI\OC\OpenCore.efi
00:000 00:000 OCFS: Trying to locate filesystem on 91CA6518 901FFF98
00:000 00:000 OCFS: Filesystem DP - EFI\OC\OpenCore.efi
00:000 00:000 OC: Absolute booter path - EFI\OC\OpenCore.efi
00:000 00:000 OC: Storage root EFI\OC\OpenCore.efi
00:000 00:000 OCST: Missing vault data, ignoring...
00:000 00:000 OC: OcMiscEarlyInit...
00:000 00:000 OC: Loaded configuration of 23640 bytes
00:000 00:000 OCS: Missing key ResizeUsePciRbIo, context <Quirks>!
00:000 00:000 OC: Got 5 drivers
00:000 00:000 OC: Watchdog status is 0
00:088 00:088 OC: OpenCore DBG-090-2023-03-06 is loading in Optional mode (0/0)...
00:116 00:028 OC: Boot timestamp - 2023.03.20 08:24:49
00:162 00:045 OCCPU: MP services threads 16 (enabled 16) - Success
00:208 00:046 OCCPU: MP services Pkg 1 Cores 8 Threads 2 - Success
00:236 00:028 OCCPU: Found 11th Gen Intel(R) Core(TM) i9-11900K @ 3.50GHz
00:271 00:034 OCCPU: Signature A0671 Stepping 1 Model A7 Family 6 Type 0 ExtModel A ExtFamily 0 uCode 3C CPUID MAX (1B/80000008)
00:299 00:027 OCCPU: EIST CFG Lock 0
00:327 00:028 OCCPU: TSC Adjust 0
00:373 00:045 OCCPU: Queried Core Crystal Clock Frequency    24000000Hz
00:401 00:027 OCCPU: CPUFrequencyFromART  3504000000Hz  3504MHz = 24000000 * 292 / 2
00:435 00:034 OCCPU: Timer address is 0 from Unknown INTEL
00:463 00:028 OCCPU: Failed to get FSBFrequency data using Apple Platform Info - Not Found
00:492 00:028 OCCPU: Intel TSC:  3504000000Hz,  3504MHz; FSB:   100114285Hz,   100MHz; MaxBusRatio: 35
00:538 00:046 OCCPU: Detected Apple Processor Type: 10 -> 1009
00:567 00:028 OCCPU: CPUFrequencyFromTSC           0Hz     0MHz
00:601 00:034 OCCPU: CPUFrequency  3504000000Hz  3504MHz
00:629 00:028 OCCPU: FSBFrequency   100114285Hz   100MHz
00:658 00:028 OCCPU: Pkg 1 Cores 8 Threads 16
00:686 00:028 OC: OcLoadNvramSupport...
00:732 00:046 OCVAR: Locate emulated NVRAM protocol - Not Found
00:768 00:035 OC: Deleting NVRAM 4D1EDE05-38C7-4A6A-9CC6-4BCCA8B38C14:DefaultBackgroundColor - Not Found
00:796 00:028 OC: Not deleting NVRAM 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:rtc-blacklist, matches add
00:826 00:030 OC: Deleting NVRAM 7C436110-AB2A-4BBB-A880-FE41995C9F82:boot-args - Success
00:873 00:046 OC: Not deleting NVRAM 7C436110-AB2A-4BBB-A880-FE41995C9F82:ForceDisplayRotationInEFI, matches add
00:922 00:049 OCVAR: Setting NVRAM 4D1EDE05-38C7-4A6A-9CC6-4BCCA8B38C14:DefaultBackgroundColor - Success
00:969 00:046 OCVAR: Setting NVRAM 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:rtc-blacklist - Not Found
00:998 00:028 OCVAR: Setting NVRAM 7C436110-AB2A-4BBB-A880-FE41995C9F82:ForceDisplayRotationInEFI - ignored, exists
01:026 00:028 OCVAR: Setting NVRAM 7C436110-AB2A-4BBB-A880-FE41995C9F82:SystemAudioVolume - ignored, exists
01:056 00:030 OCVAR: Setting NVRAM 7C436110-AB2A-4BBB-A880-FE41995C9F82:boot-args - Success
01:102 00:045 OCVAR: Setting NVRAM 7C436110-AB2A-4BBB-A880-FE41995C9F82:csr-active-config - ignored, exists
01:131 00:028 OCVAR: Setting NVRAM 7C436110-AB2A-4BBB-A880-FE41995C9F82:prev-lang:kbd - ignored, exists
01:177 00:046 OCVAR: Setting NVRAM 7C436110-AB2A-4BBB-A880-FE41995C9F82:run-efi-updater - ignored, exists
01:205 00:028 OC: Current version is DBG-090-2023-03-06
01:234 00:028 OC: OcMiscMiddleInit...
01:280 00:046 OC: StorageHandle 91CA6518 with Disabled LauncherOption pointing to Default
01:309 00:029 OC: OcLoadUefiSupport...
01:355 00:045 OCAU: OcAudioInstallProtocols (0, 0)
01:383 00:028 OCAU: 4B228577-6274-4A48-82AE-0713A1171987 protocol - Not Found
01:411 00:028 OCAU: C32332DF-FC56-4FE1-9358-BA0D529B24CD protocol - Not Found
01:457 00:045 OCAU: F4CB0B78-243B-11E7-A524-B8E8562CBAFA protocol - Not Found
01:485 00:028 OCAU: 3224B169-EC34-46D2-B779-E1B1687F525F protocol - Not Found
01:532 00:046 OCAE: Builtin installed
01:560 00:028 OCRTC: Wake log is 0xB7 0x0C  233 0x0E
01:589 00:028 OCEG: Discovered rotate NVRAM override to 0
01:635 00:045 OC: Automatic SB model j185f from model iMac20,2
01:681 00:046 OC: Loading Apple Secure Boot with j185f (level 1)
01:738 00:057 OCII: AIFTimerBoostInit Current timer is 10000
01:766 00:027 OC: Installing KeySupport...
01:794 00:028 OCII: gST->ConIn 95A01BF0 vs found 95A01BF0
01:823 00:028 AIK: Using 5 (50ms)
01:869 00:046 OCABC: ALRBL 0 RTDFRG 1 DEVMMIO 1 NOSU 0 NOVRWR 0 NOSB 0 FBSIG 0 NOHBMAP 0 SMSLIDE 1 WRUNPROT 0
01:915 00:045 OCABC: FEXITBS 0 PRMRG 0 CSLIDE 1 MSLIDE 0 PRSRV 1 RBMAP 1 VMAP 1 APPLOS 0 RTPERMS 1 ARBAR -1 RBIO 0
01:943 00:028 OCABC: Firmware has 4093768 free pages (554824 in lower 4 GB)
01:972 00:028 OCABC: Awaiting rendezvous with OpenRuntime r12
02:000 00:028 OC: RequestBootVarRouting 1
02:047 00:047 OCDM: Found 0x20046/0x20046 UEFI version (376 bytes, 0 rebuilding to 376) gST 99EFE018 gBS 87F8A0B0 gBS->CreateEventEx 87F7D090 &gBS 80ADDE40
02:076 00:028 OC: AVX enabled - 1
02:122 00:046 OC: Got 5 drivers
02:150 00:027 OC: Driver HfsPlus.efi at 0 (HfsPlus.efi) is being loaded...
02:188 00:037 OCABC: EfiBootRt candidate - <nil>
02:234 00:045 OCABC: IsEfiBootRt 0 (BP 1, Apple 0)
02:262 00:028 OCB: Arch filtering 0(37892)->9007F018(37892) caps 4 - Success
02:308 00:045 OCABC: Recovering trashed GetMemoryMap pointer
02:336 00:028 OC: Driver HfsPlus.efi at 0 is successfully loaded!
02:365 00:028 OC: Driver HfsPlus.efi at 0 needs connection.
02:428 00:063 OC: Driver OpenRuntime.efi at 1 (OpenRuntime.efi) is being loaded...
02:462 00:033 OCABC: EfiBootRt candidate - <nil>
02:507 00:045 OCABC: IsEfiBootRt 0 (BP 1, Apple 0)
02:536 00:028 OCB: Arch filtering 0(45056)->9007D018(45056) caps 4 - Success
02:564 00:028 OCABC: Recovering trashed GetMemoryMap pointer
02:592 00:027 OCABC: Got rendezvous with OpenRuntime r12
02:638 00:045 OCABC: MAT support is 1
02:684 00:045 OC: Driver OpenRuntime.efi at 1 is successfully loaded!
02:712 00:028 OC: Driver ResetNvramEntry.efi at 2 (ResetNvramEntry.efi) is being loaded...
02:746 00:033 OCABC: EfiBootRt candidate - <nil>
02:774 00:028 OCABC: IsEfiBootRt 0 (BP 1, Apple 0)
02:821 00:046 OCB: Arch filtering 0(69632)->90077018(69632) caps 4 - Success
02:867 00:046 OCABC: Recovering trashed GetMemoryMap pointer
02:895 00:028 OCCPU: TSC Adjust 0
02:923 00:028 OCCPU: Queried Core Crystal Clock Frequency    24000000Hz
02:951 00:028 OCCPU: CPUFrequencyFromART  3504000000Hz  3504MHz = 24000000 * 292 / 2
02:997 00:046 OC: Driver ResetNvramEntry.efi at 2 is successfully loaded!
03:026 00:028 OC: Driver AudioDxe.efi at 3 (AudioDxe.efi) is being loaded...
03:081 00:055 OCABC: EfiBootRt candidate - <nil>
03:109 00:028 OCABC: IsEfiBootRt 0 (BP 1, Apple 0)
03:155 00:045 OCB: Arch filtering 0(212992)->8FBD1018(212992) caps 4 - Success
03:201 00:046 OCABC: Recovering trashed GetMemoryMap pointer
03:229 00:028 OCCPU: TSC Adjust 0
03:275 00:045 OCCPU: Queried Core Crystal Clock Frequency    24000000Hz
03:303 00:028 OCCPU: CPUFrequencyFromART  3504000000Hz  3504MHz = 24000000 * 292 / 2
03:332 00:028 HDA: GPIO setup stages 0x0 GPIO pin mask 0x0 (auto) Restore NSNPEN 0 Force device <null string> Setup delay 0
03:378 00:046 OC: Driver AudioDxe.efi at 3 is successfully loaded!
03:406 00:028 OC: Driver AudioDxe.efi at 3 needs connection.
03:452 00:045 OC: Driver OpenCanopy.efi at 4 (OpenCanopy.efi) is being loaded...
03:490 00:037 OCABC: EfiBootRt candidate - <nil>
03:518 00:028 OCABC: IsEfiBootRt 0 (BP 1, Apple 0)
03:564 00:046 OCB: Arch filtering 0(167936)->8FFC0018(167936) caps 4 - Success
03:592 00:028 OCABC: Recovering trashed GetMemoryMap pointer
03:638 00:045 OCCPU: TSC Adjust 0
03:666 00:028 OCCPU: Queried Core Crystal Clock Frequency    24000000Hz
03:694 00:027 OCCPU: CPUFrequencyFromART  3504000000Hz  3504MHz = 24000000 * 292 / 2
03:722 00:028 OCUI: Registered custom GUI protocol
03:768 00:046 OC: Driver OpenCanopy.efi at 4 is successfully loaded!
03:815 00:046 OC: Connecting drivers...
03:863 00:048 HDA: Connecting controller - PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x1)
03:892 00:028 HDA: Controller version 1.0
03:938 00:045 HDA: Capabilities:
03:984 00:046 HDA:  | 64-bit: Yes  Serial Data Out Signals: 0
04:030 00:045 HDA:  | Bidir streams: 0  Input streams: 0  Output streams: 6
04:058 00:028 HDA: Controller is AMD Ellesmere HD Audio Controller
04:187 00:128 HDA: Controller protocols installed
04:225 00:038 HDA: Controller initialized
04:271 00:046 HDA: Connecting codec 0x0
04:304 00:033 HDA:  | Codec ID: 0x1002:0xAA01
04:356 00:051 HDA:  | Codec name: AMD (Unknown)
04:389 00:033 HDA:  | Codec contains 1 function groups, start @ 0x1, end @ 0x1
04:422 00:033 HDA:  | Function group @ 0x1 is of type 0x1
04:493 00:070 HDA:  | Function group @ 0x1 output amp capabilities: 0x0
04:532 00:038 HDA:  | Function group @ 0x1 GPIO capabilities: 0x0
04:582 00:050 HDA:  | Function group @ 0x1 contains 14 widgets, start @ 0x2, end @ 0xF
05:039 00:456 HDA:  |  Widget @ 0x2 (type 0x0)
05:067 00:028 HDA:  | Port widget @ 0x3 is an output (pin defaults 0x185600F0) (bitmask 1)
05:113 00:046 HDA:  |  Widget @ 0x4 (type 0x0)
05:141 00:028 HDA:  | Port widget @ 0x5 is an output (pin defaults 0x185600F0) (bitmask 2)
05:187 00:045 HDA:  |  Widget @ 0x6 (type 0x0)
05:216 00:028 HDA:  | Port widget @ 0x7 is an output (pin defaults 0x185600F0) (bitmask 4)
05:244 00:028 HDA:  |  Widget @ 0x8 (type 0x0)
05:289 00:045 HDA:  | Port widget @ 0x9 is an output (pin defaults 0x185600F0) (bitmask 8)
05:336 00:046 HDA:  |  Widget @ 0xA (type 0x0)
05:381 00:045 HDA:  | Port widget @ 0xB is an output (pin defaults 0x185600F0) (bitmask 16)
05:410 00:028 HDA:  |  Widget @ 0xC (type 0x0)
05:438 00:028 HDA:  | Port widget @ 0xD is an output (pin defaults 0x185600F0) (bitmask 32)
05:466 00:028 HDA: Codec protocols installed
05:513 00:046 HDA: Codec initialized
05:660 00:147 HDA: Connecting controller - PciRoot(0x0)/Pci(0x1F,0x3)
05:688 00:028 HDA: Controller disable no snoop
05:716 00:028 HDA: Controller version 1.0
05:745 00:028 HDA: Capabilities:
05:791 00:045 HDA:  | 64-bit: Yes  Serial Data Out Signals: 0
05:819 00:028 HDA:  | Bidir streams: 0  Input streams: 7  Output streams: 9
05:864 00:045 HDA: Controller is Intel HD Audio Controller
05:993 00:128 HDA: Controller protocols installed
06:042 00:048 HDA: Controller initialized
06:088 00:046 HDA: Connecting codec 0x0
06:121 00:033 HDA:  | Codec ID: 0x10EC:0xB00
06:172 00:050 HDA:  | Codec name: Realtek (Unknown)
06:205 00:033 HDA:  | Codec contains 1 function groups, start @ 0x1, end @ 0x1
06:239 00:033 HDA:  | Function group @ 0x1 is of type 0x1
06:327 00:088 HDA:  | Function group @ 0x1 output amp capabilities: 0x0
06:365 00:038 HDA:  | Function group @ 0x1 GPIO capabilities: 0x40000002
06:416 00:050 HDA:  | Function group @ 0x1 contains 37 widgets, start @ 0x2, end @ 0x26
06:469 00:053 HDA:  | Widget @ 0x2 output amp capabilities: 0x25757
06:558 00:088 HDA:  | Widget @ 0x3 output amp capabilities: 0x25757
06:645 00:087 HDA:  | Widget @ 0x4 output amp capabilities: 0x25757
06:751 00:106 HDA:  | Widget @ 0x5 output amp capabilities: 0x25757
07:494 00:742 HDA:  | Widget @ 0x14 output amp capabilities: 0x80000000
07:598 00:104 HDA:  | Widget @ 0x15 output amp capabilities: 0x80000000
07:697 00:099 HDA:  | Widget @ 0x16 output amp capabilities: 0x80000000
07:796 00:099 HDA:  | Widget @ 0x17 output amp capabilities: 0x80000000
07:978 00:181 HDA:  | Widget @ 0x18 output amp capabilities: 0x80000000
08:160 00:181 HDA:  | Widget @ 0x19 output amp capabilities: 0x80000000
08:324 00:163 HDA:  | Widget @ 0x1A output amp capabilities: 0x80000000
08:487 00:163 HDA:  | Widget @ 0x1B output amp capabilities: 0x80000000
08:929 00:441 HDA:  | Widget @ 0x25 output amp capabilities: 0x25757
09:060 00:131 HDA:  |  Widget @ 0xC (type 0x2)
09:088 00:027 HDA:  |  Widget @ 0x2 (type 0x0)
09:134 00:045 HDA:  | Port widget @ 0x14 is an output (pin defaults 0x1014010) (bitmask 1)
09:178 00:043 HDA:  |  Widget @ 0xD (type 0x2)
09:224 00:045 HDA:  |  Widget @ 0x3 (type 0x0)
09:270 00:046 HDA:  | Port widget @ 0x15 is an output (pin defaults 0x1011012) (bitmask 2)
09:303 00:033 HDA:  |  Widget @ 0xE (type 0x2)
09:349 00:045 HDA:  |  Widget @ 0x4 (type 0x0)
09:377 00:027 HDA:  | Port widget @ 0x16 is an output (pin defaults 0x1016011) (bitmask 4)
09:410 00:033 HDA:  |  Widget @ 0xC (type 0x2)
09:456 00:045 HDA:  |  Widget @ 0x2 (type 0x0)
09:484 00:027 HDA:  | Port widget @ 0x18 is an output (pin defaults 0x1A19050) (bitmask 8)
09:535 00:051 HDA:  |  Widget @ 0xC (type 0x2)
09:563 00:028 HDA:  |  Widget @ 0x2 (type 0x0)
09:592 00:028 HDA:  | Port widget @ 0x19 is an output (pin defaults 0x2A19060) (bitmask 16)
09:643 00:051 HDA:  |  Widget @ 0xC (type 0x2)
09:671 00:028 HDA:  |  Widget @ 0x2 (type 0x0)
09:717 00:045 HDA:  | Port widget @ 0x1A is an output (pin defaults 0x181305F) (bitmask 32)
09:750 00:032 HDA:  |  Widget @ 0xC (type 0x2)
09:778 00:028 HDA:  |  Widget @ 0x2 (type 0x0)
09:806 00:028 HDA:  | Port widget @ 0x1B is an output (pin defaults 0x2214020) (bitmask 64)
09:863 00:056 HDA:  |  Widget @ 0x6 (type 0x0)
09:909 00:045 HDA:  | Port widget @ 0x1E is an output (pin defaults 0x1456140) (bitmask 128)
09:937 00:028 HDA: Codec protocols installed
09:965 00:028 HDA: Codec initialized
10:011 00:045 HDA: Connecting codec 0x2
10:062 00:051 HDA:  | Codec ID: 0x8086:0x2816
10:113 00:051 HDA:  | Codec name: Intel (Unknown)
10:146 00:032 HDA:  | Codec contains 1 function groups, start @ 0x1, end @ 0x1
10:179 00:033 HDA:  | Function group @ 0x1 is of type 0x1
10:233 00:053 HDA:  | Function group @ 0x1 output amp capabilities: 0x0
10:289 00:056 HDA:  | Function group @ 0x1 GPIO capabilities: 0x0
10:322 00:033 HDA:  | Function group @ 0x1 contains 2 widgets, start @ 0x3, end @ 0x4
10:459 00:136 HDA:  | Widget @ 0x4 output amp capabilities: 0x80000000
10:517 00:058 HDA:  |  Widget @ 0x3 (type 0x0)
10:546 00:028 HDA:  | Port widget @ 0x4 is an output (pin defaults 0x18560010) (bitmask 1)
10:597 00:051 HDA: Codec protocols installed
10:625 00:028 HDA: Codec initialized
10:677 00:051 OC: Connecting drivers done...
10:705 00:028 OC: Found 4 pointer devices - Success
10:733 00:027 OCJS: PartitionInfo is Success
10:779 00:046 OCJS: Got APFS super block for 3B0EA268-9376-244B-96EC-6A2C922AFDEB
10:808 00:028 OCJS: Block (P:1|F:0) read req 354856C -> 1AA42B60 of 1000 (mask 0, mul 8) - Success
10:860 00:052 OCJS: APFS driver 2142081001000000/20221221 found for 3B0EA268-9376-244B-96EC-6A2C922AFDEB, required >= 1600000000000000/20210101, allow
10:889 00:028 OCABC: Recovering trashed GetMemoryMap pointer
10:917 00:028 OCJS: Connecting normally APFS driver on handle 917D9718
10:980 00:063 OCC: Installing GOP (Unsupported) on ConsoleOutHandle...
11:027 00:046 OC: Requested resolution is 0x0@0 (max: 1, force: 0) from Max
11:072 00:045 OCC: Requesting 0x0@0 (max: 1) resolution, curr 3, total 8
11:100 00:027 OCC: Current FB at 0x4000000000 (0x300000), format 1, res 1024x768 scan 1024
11:129 00:028 OCC: Mode 0 - 1920x1080:1
11:157 00:028 OCC: Mode 1 - 640x480:1
11:203 00:046 OCC: Mode 2 - 800x600:1
11:249 00:045 OCC: Mode 3 - 1024x768:1
11:277 00:028 OCC: Mode 4 - 1280x1024:1
11:306 00:028 OCC: Mode 5 - 1400x1050:1
11:334 00:028 OCC: Mode 6 - 1280x960:1
11:380 00:046 OCC: Mode 7 - 1280x720:1
11:409 00:028 OCC: Setting mode 0 with 1920x1080 resolution
11:482 00:072 OCC: Changed resolution mode to 0
11:510 00:028 OC: Changed resolution to 0x0@0 (max: 1, force: 0) from Max - Success
11:538 00:028 OC: Selected UIScale 1 based on 1920x1080 resolution
11:585 00:047 OC: Setting UIScale to 1 - Success
11:614 00:028 OCC: Using builtin text renderer scale 1 mode 1
11:655 00:041 OCC: Install console control (80ACA0B0/0/0), current - Success
11:684 00:028 OCC: Setup ASCII Output - Success
11:712 00:028 OC: Requested console mode is 0x0 (max: 0) from 
11:766 00:054 OC: Requested not to use audio
11:795 00:028 OC: OcMiscLoadSystemReport...
11:836 00:041 OC: OcLoadAcpiSupport...
11:865 00:028 OCA: Found 26 ACPI tables
11:893 00:028 OCA: Detected table FACP (50434146) (OEM 00002049204D2041) at 9852E000 of 276 bytes at index 0
11:921 00:028 OCA: Detected DSDT at 984D7000 of 353986 bytes at index 0
11:963 00:041 OCA: Detected table MCFG (4746434D) (OEM 00002049204D2041) at 9852F000 of 60 bytes at index 1
12:004 00:041 OCA: Detected table FIDT (54444946) (OEM 00000049204D2041) at 984D6000 of 156 bytes at index 2
12:032 00:028 OCA: Detected table FPDT (54445046) (OEM 00000000004C4B52) at 98383000 of 68 bytes at index 3
12:061 00:028 OCA: Detected table SSDT (54445353) (OEM 0074647353757043) at 984D2000 of 9704 bytes at index 4
12:089 00:028 OCA: Detected table SSDT (54445353) (OEM 0020746473536153) at 984CD000 of 17502 bytes at index 5
12:131 00:042 OCA: Detected table SSDT (54445353) (OEM 7464735378666749) at 984C9000 of 13005 bytes at index 6
12:172 00:040 OCA: Detected table HPET (54455048) (OEM 00002049204D2041) at 984C8000 of 56 bytes at index 7
12:201 00:028 OCA: Detected table APIC (43495041) (OEM 00002049204D2041) at 984C7000 of 356 bytes at index 8
12:229 00:028 OCA: Detected table SSDT (54445353) (OEM 7076525F72656854) at 984C6000 of 3686 bytes at index 9
12:257 00:028 OCA: Detected table SSDT (54445353) (OEM 3475736B725F6878) at 984C4000 of 6377 bytes at index 10
12:299 00:041 OCA: Detected table NHLT (544C484E) (OEM 00002049204D2041) at 984C3000 of 45 bytes at index 11
12:327 00:028 OCA: Detected table LPIT (5449504C) (OEM 00002049204D2041) at 984C1000 of 204 bytes at index 12
12:368 00:041 OCA: Detected table SSDT (54445353) (OEM 4365707954746254) at 984BF000 of 3516 bytes at index 13
12:397 00:028 OCA: Detected table SSDT (54445353) (OEM 6376654464697450) at 984BC000 of 10016 bytes at index 14
12:438 00:041 OCA: Detected table DBGP (50474244) (OEM 00002049204D2041) at 984BB000 of 52 bytes at index 15
12:480 00:041 OCA: Detected table DBG2 (32474244) (OEM 00002049204D2041) at 984BA000 of 84 bytes at index 16
12:508 00:028 OCA: Detected table SSDT (54445353) (OEM 6C62615443627355) at 984B9000 of 1763 bytes at index 17
12:550 00:041 OCA: Detected table DMAR (52414D44) (OEM 20202020324B4445) at 984B8000 of 80 bytes at index 18
12:578 00:028 OCA: Detected table SSDT (54445353) (OEM 6C62615462654441) at 984B7000 of 324 bytes at index 19
12:606 00:028 OCA: Detected table VFCT (54434656) (OEM 00002049204D2041) at 984A8000 of 59524 bytes at index 20
12:648 00:041 OCA: Detected table WPBT (54425057) (OEM 00000049204D2041) at 98386000 of 60 bytes at index 21
12:676 00:028 OCA: Detected table TPM2 (324D5054) (OEM 00002049204D2041) at 98385000 of 76 bytes at index 22
12:718 00:041 OCA: Detected table BGRT (54524742) (OEM 00002049204D2041) at 984A7000 of 56 bytes at index 23
12:746 00:028 OCA: Detected table PTDT (54445450) (OEM 00002049204D2041) at 98384000 of 3312 bytes at index 24
12:774 00:028 OCA: Detected table WSMT (544D5357) (OEM 00002049204D2041) at 984C0000 of 40 bytes at index 25
12:816 00:041 OCA: FACS signature is 0 (0)
12:844 00:028 OCA: Allocated new table SSDT at 9858F000
12:885 00:041 OCA: Inserted table SSDT (54445353) (OEM 0000000043415741) of 73 bytes into ACPI at index 26
12:914 00:028 OCA: Allocated new table SSDT at 9858E000
12:942 00:028 OCA: Inserted table SSDT (54445353) (OEM 0067756C50757043) of 112 bytes into ACPI at index 27
12:970 00:028 OCA: Allocated new table SSDT at 9858D000
13:012 00:041 OCA: Inserted table SSDT (54445353) (OEM 0066664F62756852) of 325 bytes into ACPI at index 28
13:053 00:041 OCA: Allocated new table SSDT at 9858C000
13:082 00:028 OCA: Inserted table SSDT (54445353) (OEM 7862735574647353) of 217 bytes into ACPI at index 29
13:110 00:028 OCA: Exposing XSDT table table FACP (50434146) (OEM 00002049204D2041) at 9852E000 of 276 bytes at index 0
13:152 00:041 OCA: Exposing XSDT table table MCFG (4746434D) (OEM 00002049204D2041) at 9852F000 of 60 bytes at index 1
13:193 00:041 OCA: Exposing XSDT table table FIDT (54444946) (OEM 00000049204D2041) at 984D6000 of 156 bytes at index 2
13:234 00:041 OCA: Exposing XSDT table table FPDT (54445046) (OEM 00000000004C4B52) at 98383000 of 68 bytes at index 3
13:263 00:028 OCA: Exposing XSDT table table SSDT (54445353) (OEM 0074647353757043) at 984D2000 of 9704 bytes at index 4
13:291 00:028 OCA: Exposing XSDT table table SSDT (54445353) (OEM 0020746473536153) at 984CD000 of 17502 bytes at index 5
13:319 00:028 OCA: Exposing XSDT table table SSDT (54445353) (OEM 7464735378666749) at 984C9000 of 13005 bytes at index 6
13:361 00:041 OCA: Exposing XSDT table table HPET (54455048) (OEM 00002049204D2041) at 984C8000 of 56 bytes at index 7
13:389 00:028 OCA: Exposing XSDT table table APIC (43495041) (OEM 00002049204D2041) at 984C7000 of 356 bytes at index 8
13:431 00:041 OCA: Exposing XSDT table table SSDT (54445353) (OEM 7076525F72656854) at 984C6000 of 3686 bytes at index 9
13:459 00:028 OCA: Exposing XSDT table table SSDT (54445353) (OEM 3475736B725F6878) at 984C4000 of 6377 bytes at index 10
13:487 00:028 OCA: Exposing XSDT table table NHLT (544C484E) (OEM 00002049204D2041) at 984C3000 of 45 bytes at index 11
13:529 00:041 OCA: Exposing XSDT table table LPIT (5449504C) (OEM 00002049204D2041) at 984C1000 of 204 bytes at index 12
13:557 00:028 OCA: Exposing XSDT table table SSDT (54445353) (OEM 4365707954746254) at 984BF000 of 3516 bytes at index 13
13:598 00:041 OCA: Exposing XSDT table table SSDT (54445353) (OEM 6376654464697450) at 984BC000 of 10016 bytes at index 14
13:627 00:028 OCA: Exposing XSDT table table DBGP (50474244) (OEM 00002049204D2041) at 984BB000 of 52 bytes at index 15
13:655 00:028 OCA: Exposing XSDT table table DBG2 (32474244) (OEM 00002049204D2041) at 984BA000 of 84 bytes at index 16
13:696 00:041 OCA: Exposing XSDT table table SSDT (54445353) (OEM 6C62615443627355) at 984B9000 of 1763 bytes at index 17
13:725 00:028 OCA: Exposing XSDT table table DMAR (52414D44) (OEM 20202020324B4445) at 984B8000 of 80 bytes at index 18
13:766 00:041 OCA: Exposing XSDT table table SSDT (54445353) (OEM 6C62615462654441) at 984B7000 of 324 bytes at index 19
13:795 00:028 OCA: Exposing XSDT table table VFCT (54434656) (OEM 00002049204D2041) at 984A8000 of 59524 bytes at index 20
13:823 00:028 OCA: Exposing XSDT table table WPBT (54425057) (OEM 00000049204D2041) at 98386000 of 60 bytes at index 21
13:864 00:041 OCA: Exposing XSDT table table TPM2 (324D5054) (OEM 00002049204D2041) at 98385000 of 76 bytes at index 22
13:906 00:041 OCA: Exposing XSDT table table BGRT (54524742) (OEM 00002049204D2041) at 984A7000 of 56 bytes at index 23
13:947 00:041 OCA: Exposing XSDT table table PTDT (54445450) (OEM 00002049204D2041) at 98384000 of 3312 bytes at index 24
13:975 00:027 OCA: Exposing XSDT table table WSMT (544D5357) (OEM 00002049204D2041) at 984C0000 of 40 bytes at index 25
14:003 00:028 OCA: Exposing XSDT table table SSDT (54445353) (OEM 0000000043415741) at 9858F000 of 73 bytes at index 26
14:032 00:028 OCA: Exposing XSDT table table SSDT (54445353) (OEM 0067756C50757043) at 9858E000 of 112 bytes at index 27
14:073 00:041 OCA: Exposing XSDT table table SSDT (54445353) (OEM 0066664F62756852) at 9858D000 of 325 bytes at index 28
14:115 00:041 OCA: Exposing XSDT table table SSDT (54445353) (OEM 7862735574647353) at 9858C000 of 217 bytes at index 29
14:143 00:028 OCA: Exposing RSDT table table FACP (50434146) (OEM 00002049204D2041) at 9852E000 of 276 bytes at index 0
14:172 00:028 OCA: Exposing RSDT table table MCFG (4746434D) (OEM 00002049204D2041) at 9852F000 of 60 bytes at index 1
14:200 00:028 OCA: Exposing RSDT table table FIDT (54444946) (OEM 00000049204D2041) at 984D6000 of 156 bytes at index 2
14:242 00:041 OCA: Exposing RSDT table table FPDT (54445046) (OEM 00000000004C4B52) at 98383000 of 68 bytes at index 3
14:270 00:028 OCA: Exposing RSDT table table SSDT (54445353) (OEM 0074647353757043) at 984D2000 of 9704 bytes at index 4
14:311 00:040 OCA: Exposing RSDT table table SSDT (54445353) (OEM 0020746473536153) at 984CD000 of 17502 bytes at index 5
14:339 00:028 OCA: Exposing RSDT table table SSDT (54445353) (OEM 7464735378666749) at 984C9000 of 13005 bytes at index 6
14:368 00:028 OCA: Exposing RSDT table table HPET (54455048) (OEM 00002049204D2041) at 984C8000 of 56 bytes at index 7
14:409 00:041 OCA: Exposing RSDT table table APIC (43495041) (OEM 00002049204D2041) at 984C7000 of 356 bytes at index 8
14:437 00:028 OCA: Exposing RSDT table table SSDT (54445353) (OEM 7076525F72656854) at 984C6000 of 3686 bytes at index 9
14:479 00:041 OCA: Exposing RSDT table table SSDT (54445353) (OEM 3475736B725F6878) at 984C4000 of 6377 bytes at index 10
14:507 00:028 OCA: Exposing RSDT table table NHLT (544C484E) (OEM 00002049204D2041) at 984C3000 of 45 bytes at index 11
14:535 00:028 OCA: Exposing RSDT table table LPIT (5449504C) (OEM 00002049204D2041) at 984C1000 of 204 bytes at index 12
14:590 00:054 OCA: Exposing RSDT table table SSDT (54445353) (OEM 4365707954746254) at 984BF000 of 3516 bytes at index 13
14:618 00:028 OCA: Exposing RSDT table table SSDT (54445353) (OEM 6376654464697450) at 984BC000 of 10016 bytes at index 14
14:659 00:040 OCA: Exposing RSDT table table DBGP (50474244) (OEM 00002049204D2041) at 984BB000 of 52 bytes at index 15
14:687 00:028 OCA: Exposing RSDT table table DBG2 (32474244) (OEM 00002049204D2041) at 984BA000 of 84 bytes at index 16
14:715 00:028 OCA: Exposing RSDT table table SSDT (54445353) (OEM 6C62615443627355) at 984B9000 of 1763 bytes at index 17
14:744 00:028 OCA: Exposing RSDT table table DMAR (52414D44) (OEM 20202020324B4445) at 984B8000 of 80 bytes at index 18
14:785 00:041 OCA: Exposing RSDT table table SSDT (54445353) (OEM 6C62615462654441) at 984B7000 of 324 bytes at index 19
14:826 00:041 OCA: Exposing RSDT table table VFCT (54434656) (OEM 00002049204D2041) at 984A8000 of 59524 bytes at index 20
14:855 00:028 OCA: Exposing RSDT table table WPBT (54425057) (OEM 00000049204D2041) at 98386000 of 60 bytes at index 21
14:883 00:028 OCA: Exposing RSDT table table TPM2 (324D5054) (OEM 00002049204D2041) at 98385000 of 76 bytes at index 22
14:911 00:028 OCA: Exposing RSDT table table BGRT (54524742) (OEM 00002049204D2041) at 984A7000 of 56 bytes at index 23
14:953 00:041 OCA: Exposing RSDT table table PTDT (54445450) (OEM 00002049204D2041) at 98384000 of 3312 bytes at index 24
14:995 00:041 OCA: Exposing RSDT table table WSMT (544D5357) (OEM 00002049204D2041) at 984C0000 of 40 bytes at index 25
15:023 00:028 OCA: Exposing RSDT table table SSDT (54445353) (OEM 0000000043415741) at 9858F000 of 73 bytes at index 26
15:051 00:028 OCA: Exposing RSDT table table SSDT (54445353) (OEM 0067756C50757043) at 9858E000 of 112 bytes at index 27
15:080 00:028 OCA: Exposing RSDT table table SSDT (54445353) (OEM 0066664F62756852) at 9858D000 of 325 bytes at index 28
15:121 00:041 OCA: Exposing RSDT table table SSDT (54445353) (OEM 7862735574647353) at 9858C000 of 217 bytes at index 29
15:150 00:028 OC: OcLoadPlatformSupport...
15:191 00:041 OCSMB: Found DMI Anchor 99D61000 v3.3 Table Address 99D5D000 Length 1462
15:219 00:028 OCSMB: Found DMI Anchor 99D60000 v3.3 Table Address 99D5D000 Length 1462
15:261 00:041 OCSMB: Current SMBIOS System Product Name (TUF GAMING Z590-PLUS made by ASUSTeK COMPUTER INC.)
15:302 00:041 OC: PlatformInfo auto 1 OEM SN 0 OEM UUID 0 OEM MLB 0 OEM ROM 0 - Success
15:331 00:028 OC: New SMBIOS: Acidanthera model iMac20,2
15:373 00:041 OCSMB: Post-override BIOS vendor Acidanthera 0
15:401 00:027 OCSMB: Number of CPU cache entries is 4
15:429 00:028 OCSMB: Number of CPU cache entries is 4
15:470 00:041 OCSMB: Number of CPU cache entries is 4
15:499 00:028 OCSMB: CPU1 display frequency is 3500MHz
15:540 00:041 OCSMB: Applying 2352 (1) prev 99D61000 (5218/31), 99D60000 (5218/24)
15:568 00:028 OCSMB: Patched 9653A000 v3.2 Table Address 9653B000 Length 0930 1E 28
15:598 00:030 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:name (9) - Success
15:640 00:041 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:Model (18) - Success
15:669 00:028 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:SystemSerialNumber (26) - Success
15:710 00:041 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:system-id (16) - Success
15:739 00:028 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:board-id (21) - Success
15:767 00:028 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:board-rev (1) - Success
15:796 00:028 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:StartupPowerEvents (8) - Success
15:837 00:041 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:InitialTSC (8) - Success
15:879 00:041 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:FSBFrequency (8) - Success
15:908 00:028 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:DevicePathsSupported (4) - Success
15:936 00:028 OCDH: Setting DataHub 64517CC8-6561-4051-B03C-5964B60F4C7A:RPlt (8) - Success
15:978 00:042 OC: Setting HW_BID Mac-AF89B6D9451A490B - Success
16:021 00:042 OC: Setting HW_ROM 24:AB:81:ED:E6:44 - Success
16:063 00:042 OC: Setting ROM 24:AB:81:ED:E6:44 - Success
16:092 00:029 OC: Setting HW_MLB C02036270GU00008C - Success
16:121 00:029 OC: Setting MLB C02036270GU00008C - Success
16:150 00:029 OC: Setting HW_SSN C02DCEYL046M - Success
16:192 00:042 OC: Setting SSN C02DCEYL046M - Success
16:221 00:029 OC: Setting system-id 2F772788-966B-414E-A26A-E3ED0F779405 - Success
16:263 00:042 OC: Setting FirmwareFeatures FFB3F066 - Success
16:293 00:029 OC: Setting ExtendedFirmwareFeatures 00000008FFB3F066 - Success
16:322 00:029 OC: Setting FirmwareFeaturesMask FFFFFFFF - Success
16:364 00:042 OC: Setting ExtendedFirmwareFeaturesMask 00000008FFFFFFFF - Success
16:393 00:028 OC: OcLoadDevPropsSupport...
16:434 00:041 OC: Setting devprop PciRoot(0x0)/Pci(0x1C,0x4)/Pci(0x0,0x0):device-id - Success
16:463 00:028 OC: OcMiscLateInit...
16:491 00:028 OC: Translated HibernateMode None to 0
16:533 00:041 OC: Hibernation activation - Invalid Parameter, hibernation wake - no
16:561 00:028 OC: Panic log does not exist
16:603 00:041 OC: OcLoadKernelSupport...
16:631 00:028 OC: All green, starting boot management...
16:659 00:028 OC: Handing off to external boot controller
16:701 00:041 OC: Ready for takeoff in 0 us
16:756 00:055 OCUI: Failed to load image (1/1) Resources\Image\Acidanthera\GoldenGate\Background.icns prefix:Acidanthera\GoldenGate icon:0 - Not Found
16:825 00:069 OCUI: Failed to load image (1/2) Resources\Image\Acidanthera\GoldenGate\Apple.icns prefix:Acidanthera\GoldenGate icon:1 - Not Found
16:876 00:050 OCUI: Failed to load image (2/2) Resources\Image\Acidanthera\GoldenGate\ExtWindows.icns prefix:Acidanthera\GoldenGate icon:1 - Not Found
16:916 00:039 OCUI: Failed to load image (1/2) Resources\Image\Acidanthera\GoldenGate\Other.icns prefix:Acidanthera\GoldenGate icon:1 - Not Found
16:945 00:028 OCUI: Failed to load image (2/2) Resources\Image\Acidanthera\GoldenGate\ExtTool.icns prefix:Acidanthera\GoldenGate icon:1 - Not Found
16:987 00:041 OCUI: Failed to load image (1/2) Resources\Image\Acidanthera\GoldenGate\ResetNVRAM.icns prefix:Acidanthera\GoldenGate icon:1 - Not Found
17:028 00:041 OCUI: Failed to load image (2/2) Resources\Image\Acidanthera\GoldenGate\ExtShell.icns prefix:Acidanthera\GoldenGate icon:1 - Not Found
17:067 00:038 OCUI: Info->fontSize 10 Info->bitField 192 Info->charSet 0 Info->stretchH 100 Info->aa 1
17:095 00:028 OCUI: Info->paddingUp 0 Info->paddingRight 0 Info->paddingDown 0 Info->paddingLeft 0
17:123 00:028 OCUI: Info->spacingHoriz 1 Info->spacingVert 1 Info->outline 0 Info->fontName 
17:165 00:041 OCB: Adding fs 91CA6518 (E:1|L:1|P:Success) - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)
17:193 00:028 OCB: Adding fs 917D9F98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(1,GPT,EBE52667-21BA-4A94-9B9A-2664DF3BED87,0x28,0x64000)
17:235 00:041 OCB: Adding fs 912D9B98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x2,0xFFFF,0x0)/HD(2,GPT,0006A568-636F-412C-BCA0-59A91A5D5C5D,0x8000,0x3E800000)
17:263 00:028 OCB: Adding fs 912DE798 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)
17:291 00:028 OCB: Adding fs 912DAB18 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(3,GPT,3D3E30BD-27A2-425C-86FF-30712200CDAC,0x3A800,0xED08800)
17:333 00:041 OCB: Adding fs 91281C98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(4,GPT,57335A2E-92C0-4B91-85C7-10A7AF5E5180,0xED43000,0x138800)
17:361 00:028 OCB: Adding fs 8F3A2D18 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)
17:403 00:041 OCB: Adding fs 8F3DCE98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,17EA1CDC0F050546BE02F5B7E6008DA8)
17:431 00:028 OCB: Adding fs 8F375918 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,0E9F7767C83E3243BF2766D280447698)
17:459 00:028 OCB: Adding fs 8F35BF18 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,9BFB0C06B0902B468B05F6FCE219D4D2)
17:514 00:054 OCB: Adding fs 8F36EB98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,51AEF34105193C49A55A98D8D7C4F6CE)
17:542 00:028 OCB: Adding fs 8F336F98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,31DFCFD21385BD4FAAD71AC671085FC8)
17:584 00:041 OCB: Found 12 potentially bootable filesystems
17:613 00:028 OCB: Found 2 BootOrder entries with BootNext excluded
17:641 00:028 OCB: efi-boot-device-data = PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/SasEx(0x010000003A5A2703,0xC0002AE77074616C,0x0,NoTopology,0,0,0)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
17:669 00:028 OCB: efi-boot-next-data - Not Found
17:710 00:041 OCB: efi-backup-boot-device-data - Not Found
17:752 00:041 OCB: efi-apple-recovery-data - Not Found
17:780 00:028 OCB: Dumping BootOrder
17:809 00:028 OCB: 0 -> Boot0080 = PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/SasEx(0x010000003A5A2703,0xC0002AE77074616C,0x0,NoTopology,0,0,0)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
17:837 00:028 OCB: 1 -> Boot0000 = HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
17:879 00:041 OCB: Parsing predefined list...
17:920 00:041 OCB: 0 -> Boot0080 = PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/SasEx(0x010000003A5A2703,0xC0002AE77074616C,0x0,NoTopology,0,0,0)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
17:948 00:028 OCB: 1 -> Boot0081 = Ata(Primary,Slave,0x0)/HD(2,GPT,17AFACC3-29F6-45AF-BF2D-B843ECFFFD23,0x64028,0x55A870)
17:976 00:028 OCB: Adding fs 2007C5F5 for 2 custom entries and BEP (aux hidden)
18:005 00:028 OCB: Building entry from Boot0080
18:047 00:041 OCB: Fixed DP - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
18:075 00:028 OCB: Assuming DP is full-form or lacks suffix
18:116 00:041 OCB: Expanded DP - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
18:144 00:028 OCB: Expanded DP remainder - \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
18:186 00:041 OCB: Matched fs 8F3A2D18
18:227 00:041 OCB: Adding entry type (T:2|F:0|G:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
18:256 00:028 OCB: Trying to get label from \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\.contentDetails
18:297 00:041 OCB: Trying to get label from \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\.disk_label.contentDetails
18:326 00:028 OCB: Registering entry macOS Installer [Apple] (T:2|F:0|G:0|E:0|B:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
18:354 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)
18:395 00:041 OCBP: APFS Volume Info - 8F42A818 (131072, 906F1F26-C562-430E-A8B7-5CB3FA664ACB, 16)
18:423 00:028 OCBP: APFS Container Info - 901BEE18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
18:465 00:041 OCBP: BlessedFileHEX (1/5 260) - 02 01 0C 00 D0 41 03 0A 00 00 00 00 01 01 06 00 00 06 01 01 06 00 00 00 03 17 10 00 01 00 00 00 3A 5A 27 03 C0 00 2A E7 04 01 2A 00 02 00 00 00 28 40 06 00 00 00 00 00 60 D2 97 3B 00 00 00 00
18:493 00:028 OCBP: BlessedFileHEX (2/5 260) - 5F 42 A5 94 FD A0 25 46 88 DA 8B 28 25 44 E7 E0 02 02 04 03 24 00 F7 FC 74 BE 7C 0B F3 49 91 47 01 F4 04 2E 68 42 26 1F 6F 90 62 C5 0E 43 A8 B7 5C B3 FA 66 4A CB 04 04 8A 00 5C 00 44 00 43 00
18:522 00:028 OCBP: BlessedFileHEX (3/5 260) - 31 00 43 00 45 00 41 00 31 00 37 00 2D 00 30 00 35 00 30 00 46 00 2D 00 34 00 36 00 30 00 35 00 2D 00 42 00 45 00 30 00 32 00 2D 00 46 00 35 00 42 00 37 00 45 00 36 00 30 00 30 00 38 00 44 00
18:563 00:041 OCBP: BlessedFileHEX (4/5 260) - 41 00 38 00 5C 00 63 00 6F 00 6D 00 2E 00 61 00 70 00 70 00 6C 00 65 00 2E 00 69 00 6E 00 73 00 74 00 61 00 6C 00 6C 00 65 00 72 00 5C 00 62 00 6F 00 6F 00 74 00 2E 00 65 00 66 00 69 00 00 00
18:592 00:028 OCBP: BlessedFileHEX (5/5 260) - 7F FF 04 00
18:633 00:041 OCBP: BlessedFileDP - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
18:661 00:028 OCBP: Blessed file is valid
18:689 00:028 OCBP: 12 filesystems for APFS - Success
18:722 00:032 OCBP: APFS Volume Info - 8F41CC18 (131072, 906F1F26-C562-430E-A8B7-5CB3FA664ACB, 16)
18:763 00:041 OCBP: APFS Container Info - 8F41CB98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
18:805 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 7 of 12 - 1
18:833 00:028 OCBP: Missing partition 906F1F26-C562-430E-A8B7-5CB3FA664ACB on preboot - Not Found
18:861 00:028 OCBP: No APFS booter 7 of 12 for 906F1F26-C562-430E-A8B7-5CB3FA664ACB - Not Found
18:903 00:041 OCBP: APFS Volume Info - 8F41CB98 (131072, DC1CEA17-050F-4605-BE02-F5B7E6008DA8, 64)
18:944 00:041 OCBP: APFS Container Info - 901BED18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
18:986 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 8 of 12 - 1
19:014 00:028 OCBP: Found partition DC1CEA17-050F-4605-BE02-F5B7E6008DA8 on preboot
19:042 00:028 OCBP: Want predefined list for APFS 16 at DC1CEA17-050F-4605-BE02-F5B7E6008DA8
19:070 00:028 OCBP: Predefined DC1CEA17-050F-4605-BE02-F5B7E6008DA8 \System\Library\CoreServices\boot.efi is missing - Not Found
19:112 00:041 OCBP: Predefined DC1CEA17-050F-4605-BE02-F5B7E6008DA8 \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
19:140 00:028 OCBP: No APFS booter 8 of 12 for DC1CEA17-050F-4605-BE02-F5B7E6008DA8 - Not Found
19:181 00:041 OCBP: APFS Volume Info - 8F41CE18 (131072, 67779F0E-3EC8-4332-BF27-66D280447698, 4)
19:210 00:028 OCBP: APFS Container Info - 8F41BB18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
19:238 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 9 of 12 - 1
19:280 00:041 OCBP: Missing partition 67779F0E-3EC8-4332-BF27-66D280447698 on preboot - Not Found
19:308 00:028 OCBP: No APFS booter 9 of 12 for 67779F0E-3EC8-4332-BF27-66D280447698 - Not Found
19:349 00:041 OCBP: APFS Volume Info - 8F41CB98 (131072, 060CFB9B-90B0-462B-8B05-F6FCE219D4D2, 1)
19:377 00:028 OCBP: APFS Container Info - 901BED18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
19:405 00:027 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 10 of 12 - 1
19:446 00:041 OCBP: Missing partition 060CFB9B-90B0-462B-8B05-F6FCE219D4D2 on preboot - Not Found
19:475 00:028 OCBP: No APFS booter 10 of 12 for 060CFB9B-90B0-462B-8B05-F6FCE219D4D2 - Not Found
19:516 00:041 OCBP: APFS Volume Info - 8F41A898 (131072, 41F3AE51-1905-493C-A55A-98D8D7C4F6CE, 192)
19:545 00:028 OCBP: APFS Container Info - 8F41A918 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
19:573 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 11 of 12 - 1
19:615 00:041 OCBP: Missing partition 41F3AE51-1905-493C-A55A-98D8D7C4F6CE on preboot - Not Found
19:656 00:041 OCBP: No APFS booter 11 of 12 for 41F3AE51-1905-493C-A55A-98D8D7C4F6CE - Not Found
19:698 00:041 OCBP: APFS Volume Info - 8F41BC98 (131072, D2CFDF31-8513-4FBD-AAD7-1AC671085FC8, 8)
19:726 00:027 OCBP: APFS Container Info - 901BED98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
19:754 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 12 of 12 - 1
19:782 00:028 OCBP: Missing partition D2CFDF31-8513-4FBD-AAD7-1AC671085FC8 on preboot - Not Found
19:824 00:041 OCBP: No APFS booter 12 of 12 for D2CFDF31-8513-4FBD-AAD7-1AC671085FC8 - Not Found
19:865 00:041 OCBP: APFS bless for 68A20E3B-7693-4B24-96EC-6A2C922AFDEB:<null string> is Not Found
19:894 00:028 OCB: Adding entry type (T:2|F:0|G:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
19:922 00:028 OCB: Discarding already present DP
19:950 00:028 OCB: Building entry from Boot0000
19:992 00:041 OCB: Assuming DP is short-form (prefix)
20:020 00:027 OCB: Expanded DP - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
20:062 00:041 OCB: Expanded DP remainder - \EFI\Microsoft\Boot\bootmgfw.efi
20:090 00:028 OCB: Matched fs 912DE798
20:127 00:036 OCB: Adding entry type (T:32|F:0|G:0) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
20:177 00:050 OCB: Trying to get label from \EFI\Microsoft\Boot\.contentDetails
20:212 00:035 OCB: Trying to get label from \EFI\Microsoft\Boot\.disk_label.contentDetails
20:260 00:047 OCB: Registering entry Windows [Windows] (T:32|F:0|G:0|E:0|B:0) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
20:288 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)
20:319 00:030 OCBP: Blessed file is missing
20:373 00:054 OCBP: Blessed folder is missing
20:404 00:030 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
20:449 00:045 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi was found
20:480 00:030 OCB: Adding entry type (T:32|F:0|G:0) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
20:514 00:034 OCB: Discarding already present DP
20:543 00:028 OCB: Processing blessed list
20:586 00:043 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)
20:628 00:041 OCBP: Blessed file is missing
20:656 00:028 OCBP: Blessed folder is missing
20:684 00:028 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
20:713 00:028 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
20:754 00:041 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI was found
20:796 00:041 OCB: Adding entry type (T:1|F:0|G:1) - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)/\EFI\BOOT\BOOTX64.EFI
20:824 00:028 OCB: Trying to get label from \EFI\BOOT\.contentDetails
20:852 00:027 OCB: Trying to get label from \EFI\BOOT\.disk_label.contentDetails
20:880 00:028 OCB: Trying to detect Microsoft BCD
20:922 00:041 OCB: Registering entry MONTEREY [Auto] (T:1|F:0|G:1|E:1|B:0) - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)/\EFI\BOOT\BOOTX64.EFI
20:950 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(1,GPT,EBE52667-21BA-4A94-9B9A-2664DF3BED87,0x28,0x64000)
20:991 00:041 OCBP: Blessed file is missing
21:020 00:028 OCBP: Blessed folder is missing
21:061 00:041 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
21:103 00:041 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
21:131 00:028 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI was found
21:172 00:041 OCB: Adding entry type (T:1|F:0|G:1) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(1,GPT,EBE52667-21BA-4A94-9B9A-2664DF3BED87,0x28,0x64000)/\EFI\BOOT\BOOTX64.EFI
21:201 00:028 OCB: Trying to get label from \EFI\BOOT\.contentDetails
21:230 00:028 OCB: Trying to get label from \EFI\BOOT\.disk_label.contentDetails
21:271 00:041 OCB: Trying to detect Microsoft BCD
21:300 00:028 OCB: Registering entry EFI [Auto] (T:1|F:0|G:1|E:0|B:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(1,GPT,EBE52667-21BA-4A94-9B9A-2664DF3BED87,0x28,0x64000)/\EFI\BOOT\BOOTX64.EFI
21:342 00:042 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x2,0xFFFF,0x0)/HD(2,GPT,0006A568-636F-412C-BCA0-59A91A5D5C5D,0x8000,0x3E800000)
21:370 00:028 OCBP: Blessed file is missing
21:399 00:028 OCBP: Blessed folder is missing
21:440 00:041 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
21:469 00:028 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
21:510 00:041 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI is missing - Not Found
21:539 00:029 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(3,GPT,3D3E30BD-27A2-425C-86FF-30712200CDAC,0x3A800,0xED08800)
21:568 00:028 OCBP: Blessed file is missing
21:597 00:029 OCBP: Blessed folder is missing
21:639 00:041 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
21:680 00:041 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
21:709 00:028 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI is missing - Not Found
21:737 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(4,GPT,57335A2E-92C0-4B91-85C7-10A7AF5E5180,0xED43000,0x138800)
21:779 00:041 OCBP: Blessed file is missing
21:820 00:041 OCBP: Blessed folder is missing
21:861 00:041 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
21:890 00:028 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
21:918 00:028 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI is missing - Not Found
21:946 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,17EA1CDC0F050546BE02F5B7E6008DA8)
21:988 00:041 OCBP: APFS Volume Info - 901F4D98 (131072, DC1CEA17-050F-4605-BE02-F5B7E6008DA8, 64)
22:016 00:028 OCBP: APFS Container Info - 8F3F4318 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
22:058 00:041 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,0E9F7767C83E3243BF2766D280447698)
22:086 00:028 OCBP: APFS Volume Info - 8F3F4818 (131072, 67779F0E-3EC8-4332-BF27-66D280447698, 4)
22:114 00:028 OCBP: APFS Container Info - 901F4D98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
22:156 00:041 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,9BFB0C06B0902B468B05F6FCE219D4D2)
22:185 00:028 OCBP: APFS Volume Info - 901F4198 (131072, 060CFB9B-90B0-462B-8B05-F6FCE219D4D2, 1)
22:226 00:041 OCBP: APFS Container Info - 8F3F4818 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
22:254 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,51AEF34105193C49A55A98D8D7C4F6CE)
22:282 00:028 OCBP: APFS Volume Info - 901F4E18 (131072, 41F3AE51-1905-493C-A55A-98D8D7C4F6CE, 192)
22:324 00:041 OCBP: APFS Container Info - 901F4198 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
22:352 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,31DFCFD21385BD4FAAD71AC671085FC8)
22:394 00:041 OCBP: APFS Volume Info - 8F3F4618 (131072, D2CFDF31-8513-4FBD-AAD7-1AC671085FC8, 8)
22:422 00:028 OCBP: APFS Container Info - 901F4E18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
22:450 00:028 OCB: Not adding hidden auxiliary entry OpenShell.efi (tool|B:0) -> OpenShell.efi
22:492 00:041 OCB: Not adding hidden auxiliary entry CleanNvram.efi (tool|B:0) -> CleanNvram.efi
22:533 00:041 BEP: Reset NVRAM entry, preserve boot 0, apple 0
22:575 00:041 OCB: Not adding hidden auxiliary entry Reset NVRAM (os|B:1) -> <null string>
22:603 00:028 OCB: Showing menu... 
22:632 00:029 OCHK: InitHotKeys
22:660 00:028 OCKM: Allocated key repeat context 8F3F4618 8F3F4698 8F3F4C98
22:702 00:041 OCAE: Set screen resolution to 1920x1080 - Success
22:743 00:041 OCTY: Registered handler
22:772 00:028 OCAE: Set screen resolution to 1920x1080 - Success
22:800 00:028 OCUI: Console attributes: 0
22:828 00:028 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
22:870 00:041 OCB: Trying to get image from .VolumeIcon.icns
22:898 00:028 OCB: OcGetBootEntryIcon - MONTEREY in <null string> (volume icon) - Not Found
22:940 00:041 OCUI: Console attributes: 0
22:968 00:028 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
22:996 00:028 OCB: Trying to get image from .VolumeIcon.icns
23:038 00:042 OCB: OcGetBootEntryIcon - EFI in <null string> (volume icon) - Not Found
23:066 00:028 OCUI: Console attributes: 0
23:107 00:040 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
23:136 00:028 OCB: Trying to get image from .VolumeIcon.icns
23:171 00:034 OCB: OcGetBootEntryIcon - Windows in <null string> (volume icon) - Not Found
23:225 00:054 OCUI: Using flavour icon, custom: 0
23:253 00:028 OCUI: Console attributes: 0
23:295 00:041 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
23:323 00:028 OCB: Trying to get image from DC1CEA17-050F-4605-BE02-F5B7E6008DA8\.VolumeIcon.icns
23:351 00:028 OCB: Trying to get image from .VolumeIcon.icns
23:379 00:027 OCB: OcGetBootEntryIcon - macOS Installer in DC1CEA17-050F-4605-BE02-F5B7E6008DA8\ (volume icon) - Not Found
24:628 01:249 OCHK: FreeHotKeys
24:670 00:041 OCTY: Unregistered handler
24:698 00:028 OCKM: Freeing key repeat context 8F3F4618 8F3F4698 8F3F4C98
24:727 00:028 OCB: Adding fs 91CA6518 (E:1|L:1|P:Success) - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)
24:755 00:028 OCB: Adding fs 917D9F98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(1,GPT,EBE52667-21BA-4A94-9B9A-2664DF3BED87,0x28,0x64000)
24:797 00:041 OCB: Adding fs 912D9B98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x2,0xFFFF,0x0)/HD(2,GPT,0006A568-636F-412C-BCA0-59A91A5D5C5D,0x8000,0x3E800000)
24:838 00:041 OCB: Adding fs 912DE798 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)
24:866 00:028 OCB: Adding fs 912DAB18 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(3,GPT,3D3E30BD-27A2-425C-86FF-30712200CDAC,0x3A800,0xED08800)
24:894 00:028 OCB: Adding fs 91281C98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(4,GPT,57335A2E-92C0-4B91-85C7-10A7AF5E5180,0xED43000,0x138800)
24:923 00:028 OCB: Adding fs 8F3A2D18 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)
24:964 00:041 OCB: Adding fs 8F3DCE98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,17EA1CDC0F050546BE02F5B7E6008DA8)
24:993 00:028 OCB: Adding fs 8F375918 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,0E9F7767C83E3243BF2766D280447698)
25:034 00:041 OCB: Adding fs 8F35BF18 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,9BFB0C06B0902B468B05F6FCE219D4D2)
25:063 00:028 OCB: Adding fs 8F36EB98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,51AEF34105193C49A55A98D8D7C4F6CE)
25:104 00:041 OCB: Adding fs 8F336F98 (E:0|L:0|P:Success) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,31DFCFD21385BD4FAAD71AC671085FC8)
25:146 00:041 OCB: Found 12 potentially bootable filesystems
25:174 00:028 OCB: Adding fs 2007C5F5 for 2 custom entries and BEP (aux shown)
25:215 00:041 OCB: Building entry from Boot0080
25:244 00:028 OCB: Fixed DP - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
25:272 00:028 OCB: Assuming DP is full-form or lacks suffix
25:313 00:041 OCB: Expanded DP - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
25:342 00:028 OCB: Expanded DP remainder - \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
25:383 00:041 OCB: Matched fs 8F3A2D18
25:412 00:028 OCB: Adding entry type (T:2|F:0|G:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
25:440 00:028 OCB: Trying to get label from \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\.contentDetails
25:482 00:041 OCB: Trying to get label from \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\.disk_label.contentDetails
25:510 00:028 OCB: Registering entry macOS Installer [Apple] (T:2|F:0|G:0|E:0|B:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
25:552 00:041 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)
25:580 00:028 OCBP: APFS Volume Info - 8F46C718 (131072, 906F1F26-C562-430E-A8B7-5CB3FA664ACB, 16)
25:608 00:028 OCBP: APFS Container Info - 93741D98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
25:636 00:028 OCBP: BlessedFileHEX (1/5 260) - 02 01 0C 00 D0 41 03 0A 00 00 00 00 01 01 06 00 00 06 01 01 06 00 00 00 03 17 10 00 01 00 00 00 3A 5A 27 03 C0 00 2A E7 04 01 2A 00 02 00 00 00 28 40 06 00 00 00 00 00 60 D2 97 3B 00 00 00 00
25:678 00:041 OCBP: BlessedFileHEX (2/5 260) - 5F 42 A5 94 FD A0 25 46 88 DA 8B 28 25 44 E7 E0 02 02 04 03 24 00 F7 FC 74 BE 7C 0B F3 49 91 47 01 F4 04 2E 68 42 26 1F 6F 90 62 C5 0E 43 A8 B7 5C B3 FA 66 4A CB 04 04 8A 00 5C 00 44 00 43 00
25:719 00:041 OCBP: BlessedFileHEX (3/5 260) - 31 00 43 00 45 00 41 00 31 00 37 00 2D 00 30 00 35 00 30 00 46 00 2D 00 34 00 36 00 30 00 35 00 2D 00 42 00 45 00 30 00 32 00 2D 00 46 00 35 00 42 00 37 00 45 00 36 00 30 00 30 00 38 00 44 00
25:747 00:028 OCBP: BlessedFileHEX (4/5 260) - 41 00 38 00 5C 00 63 00 6F 00 6D 00 2E 00 61 00 70 00 70 00 6C 00 65 00 2E 00 69 00 6E 00 73 00 74 00 61 00 6C 00 6C 00 65 00 72 00 5C 00 62 00 6F 00 6F 00 74 00 2E 00 65 00 66 00 69 00 00 00
25:776 00:028 OCBP: BlessedFileHEX (5/5 260) - 7F FF 04 00
25:817 00:041 OCBP: BlessedFileDP - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
25:859 00:041 OCBP: Blessed file is valid
25:900 00:041 OCBP: 12 filesystems for APFS - Success
25:933 00:032 OCBP: APFS Volume Info - 901BEC18 (131072, 906F1F26-C562-430E-A8B7-5CB3FA664ACB, 16)
25:961 00:028 OCBP: APFS Container Info - 93736518 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
25:989 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 7 of 12 - 1
26:031 00:041 OCBP: Missing partition 906F1F26-C562-430E-A8B7-5CB3FA664ACB on preboot - Not Found
26:059 00:028 OCBP: No APFS booter 7 of 12 for 906F1F26-C562-430E-A8B7-5CB3FA664ACB - Not Found
26:100 00:041 OCBP: APFS Volume Info - 901BEC18 (131072, DC1CEA17-050F-4605-BE02-F5B7E6008DA8, 64)
26:129 00:028 OCBP: APFS Container Info - 93736518 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
26:158 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 8 of 12 - 1
26:199 00:041 OCBP: Found partition DC1CEA17-050F-4605-BE02-F5B7E6008DA8 on preboot
26:228 00:028 OCBP: Want predefined list for APFS 16 at DC1CEA17-050F-4605-BE02-F5B7E6008DA8
26:269 00:041 OCBP: Predefined DC1CEA17-050F-4605-BE02-F5B7E6008DA8 \System\Library\CoreServices\boot.efi is missing - Not Found
26:297 00:028 OCBP: Predefined DC1CEA17-050F-4605-BE02-F5B7E6008DA8 \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
26:326 00:028 OCBP: No APFS booter 8 of 12 for DC1CEA17-050F-4605-BE02-F5B7E6008DA8 - Not Found
26:367 00:041 OCBP: APFS Volume Info - 93736818 (131072, 67779F0E-3EC8-4332-BF27-66D280447698, 4)
26:395 00:027 OCBP: APFS Container Info - 8F3F4998 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
26:436 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 9 of 12 - 1
26:465 00:028 OCBP: Missing partition 67779F0E-3EC8-4332-BF27-66D280447698 on preboot - Not Found
26:493 00:028 OCBP: No APFS booter 9 of 12 for 67779F0E-3EC8-4332-BF27-66D280447698 - Not Found
26:534 00:041 OCBP: APFS Volume Info - 93736818 (131072, 060CFB9B-90B0-462B-8B05-F6FCE219D4D2, 1)
26:576 00:041 OCBP: APFS Container Info - 8F3F4998 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
26:617 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 10 of 12 - 1
26:646 00:028 OCBP: Missing partition 060CFB9B-90B0-462B-8B05-F6FCE219D4D2 on preboot - Not Found
26:674 00:028 OCBP: No APFS booter 10 of 12 for 060CFB9B-90B0-462B-8B05-F6FCE219D4D2 - Not Found
26:702 00:028 OCBP: APFS Volume Info - 93736818 (131072, 41F3AE51-1905-493C-A55A-98D8D7C4F6CE, 192)
26:744 00:041 OCBP: APFS Container Info - 8F3F4998 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
26:785 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 11 of 12 - 1
26:814 00:028 OCBP: Missing partition 41F3AE51-1905-493C-A55A-98D8D7C4F6CE on preboot - Not Found
26:843 00:028 OCBP: No APFS booter 11 of 12 for 41F3AE51-1905-493C-A55A-98D8D7C4F6CE - Not Found
26:871 00:028 OCBP: APFS Volume Info - 93736818 (131072, D2CFDF31-8513-4FBD-AAD7-1AC671085FC8, 8)
26:913 00:041 OCBP: APFS Container Info - 8F3F4998 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
26:941 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 12 of 12 - 1
26:982 00:041 OCBP: Missing partition D2CFDF31-8513-4FBD-AAD7-1AC671085FC8 on preboot - Not Found
27:011 00:028 OCBP: No APFS booter 12 of 12 for D2CFDF31-8513-4FBD-AAD7-1AC671085FC8 - Not Found
27:039 00:027 OCBP: APFS bless for 68A20E3B-7693-4B24-96EC-6A2C922AFDEB:<null string> is Not Found
27:080 00:041 OCB: Adding entry type (T:2|F:0|G:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,261F6F9062C50E43A8B75CB3FA664ACB)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\boot.efi
27:108 00:028 OCB: Discarding already present DP
27:150 00:041 OCBP: APFS Container Info - 901FFC98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
27:178 00:028 OCBP: 12 filesystems for APFS - Success
27:211 00:032 OCBP: APFS Volume Info - 93738F98 (131072, 906F1F26-C562-430E-A8B7-5CB3FA664ACB, 16)
27:265 00:054 OCBP: APFS Container Info - 8F3F4998 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
27:293 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 7 of 12 - 1
27:335 00:041 OCBP: Missing partition 906F1F26-C562-430E-A8B7-5CB3FA664ACB on preboot - Not Found
27:363 00:028 OCBP: No APFS booter 7 of 12 for 906F1F26-C562-430E-A8B7-5CB3FA664ACB - Not Found
27:392 00:028 OCBP: APFS Volume Info - 93738F98 (131072, DC1CEA17-050F-4605-BE02-F5B7E6008DA8, 64)
27:420 00:028 OCBP: APFS Container Info - 8F3F4998 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
27:461 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 8 of 12 - 1
27:503 00:041 OCBP: Found partition DC1CEA17-050F-4605-BE02-F5B7E6008DA8 on preboot
27:531 00:028 OCBP: Want predefined list for APFS 16 at DC1CEA17-050F-4605-BE02-F5B7E6008DA8
27:560 00:028 OCBP: Predefined DC1CEA17-050F-4605-BE02-F5B7E6008DA8 \System\Library\CoreServices\boot.efi is missing - Not Found
27:588 00:028 OCBP: Predefined DC1CEA17-050F-4605-BE02-F5B7E6008DA8 \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
27:629 00:041 OCBP: No APFS booter 8 of 12 for DC1CEA17-050F-4605-BE02-F5B7E6008DA8 - Not Found
27:671 00:041 OCBP: APFS Volume Info - 8F3F4618 (131072, 67779F0E-3EC8-4332-BF27-66D280447698, 4)
27:699 00:028 OCBP: APFS Container Info - 93741D98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
27:727 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 9 of 12 - 1
27:755 00:028 OCBP: Missing partition 67779F0E-3EC8-4332-BF27-66D280447698 on preboot - Not Found
27:797 00:041 OCBP: No APFS booter 9 of 12 for 67779F0E-3EC8-4332-BF27-66D280447698 - Not Found
27:825 00:028 OCBP: APFS Volume Info - 8F3F4618 (131072, 060CFB9B-90B0-462B-8B05-F6FCE219D4D2, 1)
27:866 00:041 OCBP: APFS Container Info - 93741D98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
27:894 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 10 of 12 - 1
27:936 00:041 OCBP: Missing partition 060CFB9B-90B0-462B-8B05-F6FCE219D4D2 on preboot - Not Found
27:977 00:041 OCBP: No APFS booter 10 of 12 for 060CFB9B-90B0-462B-8B05-F6FCE219D4D2 - Not Found
28:006 00:028 OCBP: APFS Volume Info - 8F3F4618 (131072, 41F3AE51-1905-493C-A55A-98D8D7C4F6CE, 192)
28:047 00:041 OCBP: APFS Container Info - 93741D98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
28:075 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 11 of 12 - 1
28:104 00:028 OCBP: Missing partition 41F3AE51-1905-493C-A55A-98D8D7C4F6CE on preboot - Not Found
28:145 00:041 OCBP: No APFS booter 11 of 12 for 41F3AE51-1905-493C-A55A-98D8D7C4F6CE - Not Found
28:173 00:028 OCBP: APFS Volume Info - 8F3F4618 (131072, D2CFDF31-8513-4FBD-AAD7-1AC671085FC8, 8)
28:215 00:041 OCBP: APFS Container Info - 93741D98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
28:243 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 68A20E3B-7693-4B24-96EC-6A2C922AFDEB for 12 of 12 - 1
28:272 00:028 OCBP: Missing partition D2CFDF31-8513-4FBD-AAD7-1AC671085FC8 on preboot - Not Found
28:313 00:041 OCBP: No APFS booter 12 of 12 for D2CFDF31-8513-4FBD-AAD7-1AC671085FC8 - Not Found
28:341 00:028 OCBP: APFS bless for 68A20E3B-7693-4B24-96EC-6A2C922AFDEB:DC1CEA17-050F-4605-BE02-F5B7E6008DA8\com.apple.installer\ is Not Found
28:383 00:041 OCBP: APFS Volume Info - 901FFC98 (131072, DC1CEA17-050F-4605-BE02-F5B7E6008DA8, 64)
28:411 00:028 OCBP: APFS Container Info - 8F3F4618 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
28:439 00:028 OCBP: APFS recovery info 0/12 due to 00000000-0000-0000-0000-000000000000/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/0 - Not Found
28:468 00:028 OCBP: APFS recovery info 1/12 due to 00000000-0000-0000-0000-000000000000/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/0 - Not Found
28:510 00:041 OCBP: APFS recovery info 2/12 due to 00000000-0000-0000-0000-000000000000/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/0 - Not Found
28:556 00:046 OCBP: APFS recovery info 3/12 due to 00000000-0000-0000-0000-000000000000/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/0 - Not Found
28:584 00:028 OCBP: APFS recovery info 4/12 due to 00000000-0000-0000-0000-000000000000/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/0 - Not Found
28:613 00:028 OCBP: APFS recovery info 5/12 due to 00000000-0000-0000-0000-000000000000/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/0 - Not Found
28:654 00:041 OCBP: APFS Volume Info - 8F3F4618 (131072, 906F1F26-C562-430E-A8B7-5CB3FA664ACB, 16)
28:696 00:041 OCBP: APFS Container Info - 901FFC98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
28:737 00:041 OCBP: APFS recovery info 6/12 due to 68A20E3B-7693-4B24-96EC-6A2C922AFDEB/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/10 - Success
28:765 00:028 OCBP: APFS Volume Info - 901FFC98 (131072, DC1CEA17-050F-4605-BE02-F5B7E6008DA8, 64)
28:794 00:028 OCBP: APFS Container Info - 8F3F4618 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
28:822 00:028 OCBP: APFS recovery info 7/12 due to 68A20E3B-7693-4B24-96EC-6A2C922AFDEB/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/40 - Success
28:864 00:041 OCBP: APFS Volume Info - 8F3F4618 (131072, 67779F0E-3EC8-4332-BF27-66D280447698, 4)
28:892 00:028 OCBP: APFS Container Info - 901FFC98 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
28:933 00:041 OCBP: APFS recovery info 8/12 due to 68A20E3B-7693-4B24-96EC-6A2C922AFDEB/68A20E3B-7693-4B24-96EC-6A2C922AFDEB/4 - Success
28:962 00:028 OCFS: Filename \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\ has trailing slash
28:990 00:028 OCFS: Filename \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\ has trailing slash
29:032 00:041 OCB: Matched fs 8F375918
29:060 00:028 OCB: Adding entry type (T:1|F:1|G:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,0E9F7767C83E3243BF2766D280447698)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\
29:101 00:041 OCFS: Filename \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\ has trailing slash
29:129 00:028 OCFS: Filename \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\ has trailing slash
29:158 00:028 AAPL: FileSetPosition:3108: FileSetPosition: attempt to set position for directory to 18446744073709551615
29:199 00:041 OCB: Trying to get label from \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\.contentDetails
29:227 00:028 OCB: Trying to get label from \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\.disk_label.contentDetails
29:269 00:041 OCB: Trying to get Apple version from \DC1CEA17-050F-4605-BE02-F5B7E6008DA8\SystemVersion.plist
29:298 00:028 OCB: Registering entry Recovery [AppleRecv:Apple] (T:4|F:1|G:0|E:0|B:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,0E9F7767C83E3243BF2766D280447698)/\DC1CEA17-050F-4605-BE02-F5B7E6008DA8\
29:326 00:028 OCB: Building entry from Boot0000
29:368 00:041 OCB: Assuming DP is short-form (prefix)
29:409 00:041 OCB: Expanded DP - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
29:450 00:041 OCB: Expanded DP remainder - \EFI\Microsoft\Boot\bootmgfw.efi
29:479 00:028 OCB: Matched fs 912DE798
29:515 00:036 OCB: Adding entry type (T:32|F:0|G:0) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
29:550 00:034 OCB: Trying to get label from \EFI\Microsoft\Boot\.contentDetails
29:598 00:048 OCB: Trying to get label from \EFI\Microsoft\Boot\.disk_label.contentDetails
29:646 00:047 OCB: Registering entry Windows [Windows] (T:32|F:0|G:0|E:0|B:0) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
29:675 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)
29:705 00:030 OCBP: Blessed file is missing
29:734 00:028 OCBP: Blessed folder is missing
29:777 00:043 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
29:810 00:032 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi was found
29:853 00:043 OCB: Adding entry type (T:32|F:0|G:0) - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(1,GPT,51196A79-0E3C-4A07-8A6E-F8383EF19E20,0x800,0x32000)/\EFI\Microsoft\Boot\bootmgfw.efi
29:888 00:034 OCB: Discarding already present DP
29:916 00:027 OCBP: APFS recovery volume handle missing - \EFI\Microsoft\Boot\
29:957 00:041 OCB: APFS recovery is not present - Not Found
29:986 00:028 OCB: Processing blessed list
30:027 00:041 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)
30:055 00:028 OCBP: Blessed file is missing
30:083 00:028 OCBP: Blessed folder is missing
30:138 00:054 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
30:166 00:028 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
30:208 00:041 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI was found
30:235 00:027 OCB: Adding entry type (T:1|F:0|G:1) - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)/\EFI\BOOT\BOOTX64.EFI
30:264 00:028 OCB: Trying to get label from \EFI\BOOT\.contentDetails
30:292 00:028 OCB: Trying to get label from \EFI\BOOT\.disk_label.contentDetails
30:333 00:041 OCB: Trying to detect Microsoft BCD
30:375 00:041 OCB: Registering entry MONTEREY [Auto] (T:1|F:0|G:1|E:1|B:0) - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)/\EFI\BOOT\BOOTX64.EFI
30:403 00:028 OCBP: APFS recovery volume handle missing - \EFI\BOOT\
30:431 00:028 OCB: APFS recovery is not present - Not Found
30:460 00:028 OCB: Got recovery dp PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)/\com.apple.recovery.boot\
30:502 00:041 OCB: Adding entry type (T:4|F:1|G:0) - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)/\com.apple.recovery.boot\
30:543 00:040 OCFS: Filename \com.apple.recovery.boot\ has trailing slash
30:571 00:028 OCFS: Filename \com.apple.recovery.boot\ has trailing slash
30:599 00:028 OCB: Trying to get label from \com.apple.recovery.boot\.contentDetails
30:632 00:032 OCB: Trying to get label from \com.apple.recovery.boot\.disk_label.contentDetails
30:673 00:041 OCB: Registering entry MONTEREY [AppleRecv:Apple] (T:4|F:1|G:0|E:1|B:0) - PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)/USB(0x2,0x0)/HD(1,GPT,394F4767-1C29-4489-ACB5-A5BDFC7933AB,0x800,0xE8D7DF)/\com.apple.recovery.boot\
30:702 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(1,GPT,EBE52667-21BA-4A94-9B9A-2664DF3BED87,0x28,0x64000)
30:743 00:041 OCBP: Blessed file is missing
30:772 00:028 OCBP: Blessed folder is missing
30:813 00:041 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
30:855 00:041 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
30:883 00:028 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI was found
30:924 00:041 OCB: Adding entry type (T:1|F:0|G:1) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(1,GPT,EBE52667-21BA-4A94-9B9A-2664DF3BED87,0x28,0x64000)/\EFI\BOOT\BOOTX64.EFI
30:953 00:028 OCB: Trying to get label from \EFI\BOOT\.contentDetails
30:981 00:028 OCB: Trying to get label from \EFI\BOOT\.disk_label.contentDetails
31:023 00:041 OCB: Trying to detect Microsoft BCD
31:051 00:028 OCB: Registering entry EFI [Auto] (T:1|F:0|G:1|E:0|B:0) - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(1,GPT,EBE52667-21BA-4A94-9B9A-2664DF3BED87,0x28,0x64000)/\EFI\BOOT\BOOTX64.EFI
31:093 00:041 OCBP: APFS recovery volume handle missing - \EFI\BOOT\
31:121 00:028 OCB: APFS recovery is not present - Not Found
31:150 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x2,0xFFFF,0x0)/HD(2,GPT,0006A568-636F-412C-BCA0-59A91A5D5C5D,0x8000,0x3E800000)
31:192 00:041 OCBP: Blessed file is missing
31:220 00:028 OCBP: Blessed folder is missing
31:261 00:041 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
31:289 00:028 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
31:318 00:028 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI is missing - Not Found
31:352 00:034 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(3,GPT,3D3E30BD-27A2-425C-86FF-30712200CDAC,0x3A800,0xED08800)
31:394 00:041 OCBP: Blessed file is missing
31:435 00:041 OCBP: Blessed folder is missing
31:464 00:028 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
31:492 00:028 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
31:534 00:041 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI is missing - Not Found
31:575 00:041 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x17,0x0)/Sata(0x4,0xFFFF,0x0)/HD(4,GPT,57335A2E-92C0-4B91-85C7-10A7AF5E5180,0xED43000,0x138800)
31:616 00:041 OCBP: Blessed file is missing
31:645 00:028 OCBP: Blessed folder is missing
31:673 00:028 OCBP: Predefined <nil> \System\Library\CoreServices\boot.efi is missing - Not Found
31:701 00:028 OCBP: Predefined <nil> \EFI\Microsoft\Boot\bootmgfw.efi is missing - Not Found
31:743 00:041 OCBP: Predefined <nil> \EFI\BOOT\BOOTX64.EFI is missing - Not Found
31:771 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,17EA1CDC0F050546BE02F5B7E6008DA8)
31:813 00:041 OCBP: APFS Volume Info - 8F3E5518 (131072, DC1CEA17-050F-4605-BE02-F5B7E6008DA8, 64)
31:841 00:028 OCBP: APFS Container Info - 90211E18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
31:869 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,0E9F7767C83E3243BF2766D280447698)
31:911 00:041 OCBP: APFS Volume Info - 8F3E5998 (131072, 67779F0E-3EC8-4332-BF27-66D280447698, 4)
31:940 00:028 OCBP: APFS Container Info - 8F3E5518 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
31:981 00:041 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,9BFB0C06B0902B468B05F6FCE219D4D2)
32:009 00:028 OCBP: APFS Volume Info - 8F3E5F18 (131072, 060CFB9B-90B0-462B-8B05-F6FCE219D4D2, 1)
32:037 00:028 OCBP: APFS Container Info - 8F3E5998 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
32:079 00:041 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,51AEF34105193C49A55A98D8D7C4F6CE)
32:107 00:028 OCBP: APFS Volume Info - 8F3F4598 (131072, 41F3AE51-1905-493C-A55A-98D8D7C4F6CE, 192)
32:149 00:041 OCBP: APFS Container Info - 8F3E5F18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
32:177 00:028 OCB: Adding bless entry on disk - PciRoot(0x0)/Pci(0x6,0x0)/Pci(0x0,0x0)/NVMe(0x1,E7-2A-00-C0-03-27-5A-3A)/HD(2,GPT,94A5425F-A0FD-4625-88DA-8B282544E7E0,0x64028,0x3B97D260)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,31DFCFD21385BD4FAAD71AC671085FC8)
32:205 00:028 OCBP: APFS Volume Info - 8F3F4B98 (131072, D2CFDF31-8513-4FBD-AAD7-1AC671085FC8, 8)
32:247 00:041 OCBP: APFS Container Info - 8F3F4598 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
32:288 00:041 OCB: Adding custom entry OpenShell.efi (tool|B:0) -> OpenShell.efi
32:330 00:041 OCB: Registering entry OpenShell.efi [Auto] (T:128|F:0|G:0|E:0|B:0) - <nil>
32:358 00:028 OCB: Adding custom entry CleanNvram.efi (tool|B:0) -> CleanNvram.efi
32:386 00:028 OCB: Registering entry CleanNvram.efi [Auto] (T:128|F:0|G:0|E:0|B:0) - <nil>
32:415 00:028 BEP: Reset NVRAM entry, preserve boot 0, apple 0
32:456 00:041 OCB: Adding custom entry Reset NVRAM (action|B:1) -> <null string>
32:498 00:041 OCB: Registering entry Reset NVRAM [ResetNVRAM:NVRAMTool] (T:256|F:0|G:0|E:0|B:1) - <nil>
32:526 00:028 OCB: Showing menu... 
32:555 00:029 OCHK: InitHotKeys
32:583 00:028 OCKM: Allocated key repeat context 8F3E5E18 8F41BD18 8F41BD98
32:625 00:041 OCAE: Set screen resolution to 1920x1080 - Success
32:653 00:028 OCTY: Registered handler
32:694 00:041 OCAE: Set screen resolution to 1920x1080 - Success
32:723 00:028 OCUI: Console attributes: 0
32:750 00:027 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
32:792 00:041 OCB: Trying to get image from .VolumeIcon.icns
32:820 00:028 OCB: OcGetBootEntryIcon - MONTEREY in <null string> (volume icon) - Not Found
32:861 00:041 OCUI: Console attributes: 0
32:890 00:028 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
32:918 00:028 OCB: Trying to get image from .VolumeIcon.icns
32:973 00:054 OCB: OcGetBootEntryIcon - MONTEREY in <null string> (volume icon) - Not Found
33:001 00:028 OCUI: Using flavour icon, custom: 0
33:043 00:041 OCUI: Console attributes: 0
33:071 00:028 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
33:099 00:028 OCB: Trying to get image from .VolumeIcon.icns
33:128 00:028 OCB: OcGetBootEntryIcon - EFI in <null string> (volume icon) - Not Found
33:169 00:041 OCUI: Console attributes: 0
33:211 00:041 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
33:239 00:028 OCB: Trying to get image from .VolumeIcon.icns
33:274 00:034 OCB: OcGetBootEntryIcon - Windows in <null string> (volume icon) - Not Found
33:302 00:028 OCUI: Using flavour icon, custom: 0
33:343 00:041 OCUI: Console attributes: 0
33:385 00:041 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
33:413 00:028 OCB: Trying to get image from DC1CEA17-050F-4605-BE02-F5B7E6008DA8\.VolumeIcon.icns
33:441 00:028 OCB: Trying to get image from .VolumeIcon.icns
33:469 00:028 OCB: OcGetBootEntryIcon - macOS Installer in DC1CEA17-050F-4605-BE02-F5B7E6008DA8\ (volume icon) - Not Found
33:511 00:041 OCUI: Console attributes: 0
33:540 00:028 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
33:581 00:041 OCB: Trying to get image from DC1CEA17-050F-4605-BE02-F5B7E6008DA8\.VolumeIcon.icns
33:609 00:028 OCB: Trying to get image from .VolumeIcon.icns
33:651 00:041 OCB: OcGetBootEntryIcon - Recovery in DC1CEA17-050F-4605-BE02-F5B7E6008DA8\ (volume icon) - Not Found
33:692 00:041 OCUI: Using flavour icon, custom: 0
33:721 00:028 OCUI: Console attributes: 0
33:762 00:041 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
33:790 00:028 OCUI: Console attributes: 0
33:818 00:028 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
33:860 00:041 OCUI: Console attributes: 0
33:888 00:028 OCUI: UseDiskLabel: 0, UseGenericLabel: 0
35:912 02:023 OCHK: FreeHotKeys
35:940 00:028 OCTY: Unregistered handler
35:969 00:028 OCKM: Freeing key repeat context 8F3E5E18 8F41BD18 8F41BD98
36:010 00:041 OCB: Should boot from 6. Recovery (T:4|F:1|G:0|E:0|DEF:0)
36:079 00:068 OCRAM: Extent allocation of 1117627948 bytes (A) gave 100000000
46:050 09:971 OCRAM: SHA-256 Digest is: 9DF892808F1E79495E73BCCB11E91A4C91960F5CD3152D875B255BD18DDEF3D4
46:079 00:028 OCB: Found chunklist BaseSystem.chunklist for DMG BaseSystem.dmg[10]
54:281 08:201 OCDI: Built DMG DP: VenHw(957932CC-7E8E-433B-8F41-D391EA3C10F8,00000000)/MemoryMapped(0xA,0x100000000,0x100001000)/DMG_00000000429DA62C.dmg/VenMsg(004B07E8-0B9C-427E-B0D4-A466E6E57A62,2CA69D4200000000)
54:310 00:028 AAPL: APFSStart:1589: Mounting with apfs_efi_osx-2142.81.1
54:352 00:041 AAPL: efi_fusion_pairing:672: Container 91f83f1f-ecf8-4515-8ceb-7f12d6c4ad8b
54:393 00:041 AAPL: efi_fusion_pairing:677: fusion uuid: 00000000-0000-0000-0000-000000000000
54:422 00:028 AAPL: efi_container_create:914: LoadedImage->DeviceHandle = 0x0
54:450 00:028 AAPL: efi_container_create:976: Volume attached is external
54:492 00:041 AAPL: nx_dev_init:816: warning: superblock indicates jumpstart record but this driver was not loaded from that partition
54:533 00:041 AAPL: nx_mount:1219:  initializing cache w/hash_size 256 and cache size 4096
54:575 00:041 AAPL: nx_mount:1548: checkpoint search: largest xid 63, best xid 63 @ 5
54:604 00:028 AAPL: nx_mount:1575: stable checkpoint indices: desc 4 data 9
54:632 00:028 AAPL: er_state_obj_get_for_recovery:7575: No ER state object for volume Preboot - rolling is not happening, nothing to recover.
54:661 00:028 AAPL: er_state_obj_get_for_recovery:7575: No ER state object for volume macOS Base System - rolling is not happening, nothing to recover.
54:702 00:041 OCJS: Matched device path
54:730 00:027 OCJS: Matched device path
54:772 00:041 OCJS: Got APFS super block for 1F3FF891-F8EC-1545-8CEB-7F12D6C4AD8B
54:800 00:028 OCJS: Block (P:1|F:0) read req E2F -> 7178 of 1000 (mask 0, mul 8) - Success
54:834 00:033 OCJS: APFS driver 1934141002000000/20220809 found for 1F3FF891-F8EC-1545-8CEB-7F12D6C4AD8B, required >= 1600000000000000/20210101, allow
54:875 00:041 OCABC: Recovering trashed GetMemoryMap pointer
54:904 00:028 OCJS: Connecting normally APFS driver on handle 8E2B3618
54:945 00:041 OCJS: Matched device path
54:973 00:028 OCJS: Matched device path
55:002 00:028 OCBP: APFS Volume Info - 8E25C898 (131072, 7751D6E0-C824-4823-B08B-3C6DC57699A9, 16)
55:043 00:041 OCBP: APFS Container Info - 8E25B218 (1, 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B)
55:072 00:028 OCBP: BlessedFileHEX (1/6 366) - 01 04 18 00 CC 32 79 95 8E 7E 3B 43 8F 41 D3 91 EA 3C 10 F8 00 00 00 00 01 03 18 00 0A 00 00 00 00 00 00 00 01 00 00 00 00 10 00 00 01 00 00 00 04 04 36 00 44 00 4D 00 47 00 5F 00 30 00 30 00
55:113 00:041 OCBP: BlessedFileHEX (2/6 366) - 30 00 30 00 30 00 30 00 30 00 30 00 34 00 32 00 39 00 44 00 41 00 36 00 32 00 43 00 2E 00 64 00 6D 00 67 00 00 00 03 0A 1C 00 E8 07 4B 00 9C 0B 7E 42 B0 D4 A4 66 E6 E5 7A 62 2C A6 9D 42 00 00
55:141 00:028 OCBP: BlessedFileHEX (3/6 366) - 00 00 04 01 2A 00 01 00 00 00 22 00 00 00 00 00 00 00 00 00 22 00 00 00 00 00 E6 A4 F0 3E DB FA EE 48 BD F1 58 48 91 7F AE A7 02 02 04 03 24 00 F7 FC 74 BE 7C 0B F3 49 91 47 01 F4 04 2E 68 42
55:170 00:028 OCBP: BlessedFileHEX (4/6 366) - E0 D6 51 77 24 C8 23 48 B0 8B 3C 6D C5 76 99 A9 04 04 9A 00 5C 00 33 00 31 00 39 00 31 00 36 00 34 00 30 00 43 00 2D 00 45 00 34 00 37 00 41 00 2D 00 34 00 31 00 32 00 31 00 2D 00 41 00 42 00
55:211 00:041 OCBP: BlessedFileHEX (5/6 366) - 39 00 33 00 2D 00 39 00 44 00 42 00 41 00 33 00 36 00 37 00 39 00 37 00 36 00 38 00 33 00 5C 00 53 00 79 00 73 00 74 00 65 00 6D 00 5C 00 4C 00 69 00 62 00 72 00 61 00 72 00 79 00 5C 00 43 00
55:253 00:041 OCBP: BlessedFileHEX (6/6 366) - 6F 00 72 00 65 00 53 00 65 00 72 00 76 00 69 00 63 00 65 00 73 00 5C 00 62 00 6F 00 6F 00 74 00 2E 00 65 00 66 00 69 00 00 00 7F FF 04 00
55:294 00:041 OCBP: BlessedFileDP - VenHw(957932CC-7E8E-433B-8F41-D391EA3C10F8,00000000)/MemoryMapped(0xA,0x100000000,0x100001000)/DMG_00000000429DA62C.dmg/VenMsg(004B07E8-0B9C-427E-B0D4-A466E6E57A62,2CA69D4200000000)/HD(1,GPT,3EF0A4E6-FADB-48EE-BDF1-5848917FAEA7,0x22,0x220000)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,E0D6517724C82348B08B3C6DC57699A9)/\3191640C-E47A-4121-AB93-9DBA36797683\System\Library\CoreServices\boot.efi
55:322 00:027 OCBP: Blessed file is valid
55:350 00:028 OCBP: 14 filesystems for APFS - Success
55:383 00:032 OCBP: APFS Volume Info - 8E25B398 (131072, 906F1F26-C562-430E-A8B7-5CB3FA664ACB, 16)
55:424 00:041 OCBP: APFS Container Info - 8E25BA18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
55:466 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B for 7 of 14 - 0
55:494 00:028 OCBP: APFS Volume Info - 8E25B398 (131072, DC1CEA17-050F-4605-BE02-F5B7E6008DA8, 64)
55:522 00:028 OCBP: APFS Container Info - 8E25BA18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
55:551 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B for 8 of 14 - 0
55:593 00:041 OCBP: APFS Volume Info - 8E25B398 (131072, 67779F0E-3EC8-4332-BF27-66D280447698, 4)
55:621 00:028 OCBP: APFS Container Info - 8E25BA18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
55:662 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B for 9 of 14 - 0
55:690 00:027 OCBP: APFS Volume Info - 8E25B398 (131072, 060CFB9B-90B0-462B-8B05-F6FCE219D4D2, 1)
55:718 00:028 OCBP: APFS Container Info - 8E25BA18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
55:759 00:041 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B for 10 of 14 - 0
55:788 00:028 OCBP: APFS Volume Info - 8E25B398 (131072, 41F3AE51-1905-493C-A55A-98D8D7C4F6CE, 192)
55:829 00:041 OCBP: APFS Container Info - 8E25BA18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
55:858 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B for 11 of 14 - 0
55:886 00:028 OCBP: APFS Volume Info - 8E25B398 (131072, D2CFDF31-8513-4FBD-AAD7-1AC671085FC8, 8)
55:941 00:054 OCBP: APFS Container Info - 8E25BA18 (1, 68A20E3B-7693-4B24-96EC-6A2C922AFDEB)
55:969 00:028 OCBP: APFS match container 68A20E3B-7693-4B24-96EC-6A2C922AFDEB vs 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B for 12 of 14 - 0
56:010 00:041 OCBP: APFS Volume Info - 8E25B398 (131072, 7751D6E0-C824-4823-B08B-3C6DC57699A9, 16)
56:038 00:028 OCBP: APFS Container Info - 8E25BA18 (1, 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B)
56:067 00:028 OCBP: APFS match container 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B vs 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B for 13 of 14 - 1
56:095 00:028 OCBP: Missing partition 7751D6E0-C824-4823-B08B-3C6DC57699A9 on preboot - Not Found
56:136 00:041 OCBP: No APFS booter 13 of 14 for 7751D6E0-C824-4823-B08B-3C6DC57699A9 - Not Found
56:178 00:041 OCBP: APFS Volume Info - 8E25B398 (131072, 3191640C-E47A-4121-AB93-9DBA36797683, 1)
56:206 00:028 OCBP: APFS Container Info - 8E25BA18 (1, 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B)
56:235 00:028 OCBP: APFS match container 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B vs 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B for 14 of 14 - 1
56:263 00:028 OCBP: Found partition 3191640C-E47A-4121-AB93-9DBA36797683 on preboot
56:305 00:041 OCBP: Want predefined list for APFS 16 at 3191640C-E47A-4121-AB93-9DBA36797683
56:346 00:041 OCBP: Predefined 3191640C-E47A-4121-AB93-9DBA36797683 \System\Library\CoreServices\boot.efi was found
56:374 00:028 OCBP: Found APFS booter 14 of 14 for 3191640C-E47A-4121-AB93-9DBA36797683 (87F742C0)
56:402 00:028 OCBP: APFS bless for 91F83F1F-ECF8-4515-8CEB-7F12D6C4AD8B:<null string> is Success
56:431 00:028 OCSB: Disabling secure boot for Apple images
56:472 00:041 OCB: Perform boot Recovery to dp VenHw(957932CC-7E8E-433B-8F41-D391EA3C10F8,00000000)/MemoryMapped(0xA,0x100000000,0x100001000)/DMG_00000000429DA62C.dmg/VenMsg(004B07E8-0B9C-427E-B0D4-A466E6E57A62,2CA69D4200000000)/HD(1,GPT,3EF0A4E6-FADB-48EE-BDF1-5848917FAEA7,0x22,0x220000)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,E0D6517724C82348B08B3C6DC57699A9)/\3191640C-E47A-4121-AB93-9DBA36797683\System\Library\CoreServices\boot.efi (0/0)
56:501 00:028 OCABC: EfiBootRt candidate - VenHw(957932CC-7E8E-433B-8F41-D391EA3C10F8,00000000)/MemoryMapped(0xA,0x100000000,0x100001000)/DMG_00000000429DA62C.dmg/VenMsg(004B07E8-0B9C-427E-B0D4-A466E6E57A62,2CA69D4200000000)/HD(1,GPT,3EF0A4E6-FADB-48EE-BDF1-5848917FAEA7,0x22,0x220000)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842,E0D6517724C82348B08B3C6DC57699A9)/\3191640C-E47A-4121-AB93-9DBA36797683\System\Library\CoreServices\boot.efi
56:542 00:041 OCABC: IsEfiBootRt 0 (BP 1, Apple 0)
56:570 00:028 OCSB: Direct booting for DMG image
56:612 00:041 OCB: Arch filtering 8E19C018(723512)->8E19C018(723512) caps 4 - Success
56:653 00:041 OCB: Matching <>/0[0] args on type 4
56:682 00:028 OCABC: Recovering trashed GetMemoryMap pointer
56:723 00:041 OCABC: VMware Mac installed on 8E25B718 - Success
56:753 00:029 OCABC: Patching safe mode sur-2 at off 1F0B
56:781 00:028 OCABC: MMIO devirt start
56:822 00:041 OCABC: MMIO devirt 0xE0000000 (0x10000 pages, 0x8000000000000001) skip 0
56:851 00:028 OCABC: MMIO devirt 0xFE000000 (0x11 pages, 0x8000000000000001) skip 0
56:892 00:041 OCABC: MMIO devirt 0xFEC00000 (0x1 pages, 0x8000000000000001) skip 0
56:920 00:028 OCABC: MMIO devirt 0xFED00000 (0x1 pages, 0x8000000000000001) skip 0
56:949 00:028 OCABC: MMIO devirt 0xFEE00000 (0x1 pages, 0x8000000000000001) skip 0
56:991 00:041 OCABC: MMIO devirt 0xFF000000 (0x1000 pages, 0x800000000000100D) skip 0
57:019 00:028 OCABC: MMIO devirt end, saved 278608 KB
57:060 00:041 OCABC: All slides are usable! You can disable ProvideCustomSlide!
57:089 00:028 AAPL: #[EB.H.IS|!] Err(0xE) <- RT.GV boot-signature 7C436110-AB2A-4BBB-A880-FE41995C9F82
57:117 00:028 AAPL: #[EB.H.IS|!] Err(0xE) <- RT.GV boot-image-key 7C436110-AB2A-4BBB-A880-FE41995C9F82
57:145 00:028 AAPL: #[EB|H:IS] 0
57:187 00:041 AAPL: #[EB|LOG:INIT] 2023-03-20T08:25:46
57:228 00:041 AAPL: #[EB|VERSION] <"bootbase.efi 540.120.3~22 (Official), built 2022-08-09T02:59:17-0700">
57:257 00:028 AAPL: #[EB|BUILD] <"BUILD-INFO[308]:{"DisplayName":"bootbase.efi","DisplayVersion":"540.120.3~22","RecordUuid":"F0E4536D-66BD-4683-8B36-C38D7CA34143","BuildTime":"2022-08-09T02:59:17-0700","ProjectName":"efiboot","ProductName":"bootbase.efi","SourceVersion":"540.120.3","BuildVersion":"22","BuildConfiguration":"Release","BuildType":"Official"}">
57:285 00:028 AAPL: #[EB.CFG.DEV|!] Err(0xE) <- RT.GV booter-strict-xmlparser 7C436110-AB2A-4BBB-A880-FE41995C9F82
57:327 00:041 AAPL: #[EB|CFG:DEV] r5 0x0 0x0
57:369 00:042 AAPL: #[EB|H:IS] 0
57:410 00:041 AAPL: #[EB|WL:MODE] 0
57:438 00:028 AAPL: #[EB|CFG:ARG] boot-save-log 0x0000000000000002 (0x0000000000000002 < 0xFFFFFFFFFFFFFFFF) default
57:466 00:028 AAPL: #[EB|CFG:ARG] wake-save-log 0x0000000000000002 (0x0000000000000002 < 0x0000000000000002) default
57:495 00:028 AAPL: #[EB|CFG:ARG] console       0x0000000000000001 (0x0000000000000001 < 0x0000000000000001) default
57:536 00:041 AAPL: #[EB|CFG:ARG] serial        0x0000000000000001 (0x0000000000000001 < 0x0000000000000000) default
57:564 00:028 AAPL: #[EB|CFG:ARG] preoslog      0x0000000000000001 (0x0000000000000001 < 0xFFFFFFFFFFFFFFFF) default
57:606 00:041 AAPL: #[EB|CFG:ARG] timestamps    0x0000000000000000 (0x0000000000000000 < 0xFFFFFFFFFFFFFFFF) default
57:634 00:028 AAPL: #[EB|CFG:ARG] log-level     0x0000000000000001 (0x0000000000000001 & 0x0000000000000021) default
57:663 00:028 AAPL: #[EB|CFG:ARG] breakpoint    0x0000000000000000 (0x0000000000000000 & 0x0000000000000000) default
57:704 00:041 AAPL: #[EB|CFG:ARG] kc-read-size  0x0000000000100000 (0x0000000000100000 < 0xFFFFFFFFFFFFFFFF) default
57:733 00:028 AAPL: #[EB|H:IS] 0
57:774 00:041 AAPL: #[EB|WL] 0 0 0x01 0x01   0 0x00
57:802 00:028 AAPL: #[EB|BRD:NV] Mac-AF89B6D9451A490B
57:830 00:028 OCOS: OS set: <null> macOS 11.0
57:872 00:041 OCOS: OS set: Apple Inc. macOS 11.0
57:900 00:028 AAPL: #[EB|B:VAw]
57:942 00:041 AAPL: #[EB|B:IAw]
57:970 00:028 AAPL: #[EB|WL] 0 0 0x01 0x01   2 0x00
57:999 00:028 AAPL: #[EB.BST.IDT|+]
58:040 00:041 AAPL: #[EB|BM] J185FAP
58:082 00:041 AAPL: #[EB.BST.IDT|-]
58:123 00:041 AAPL: #[EB|WL] 0 0 0x01 0x01   3 0x00
58:152 00:028 AAPL: #[EB|WL] 0 0 0x01 0x01   4 0x00
58:180 00:028 AAPL: #[EB|BRD:NV] Mac-AF89B6D9451A490B
58:208 00:027 AAPL: #[EB|WL] 0 0 0x01 0x01   5 0x00
58:249 00:041 AAPL: #[EB.H.CHK|BM] 0x0000000000000000
58:291 00:041 AAPL: #[EB.H.LV|!] Err(0xE) <- RT.GV boot-signature 7C436110-AB2A-4BBB-A880-FE41995C9F82
58:319 00:028 AAPL: #[EB|WL] 0 0 0x01 0x01  23 0x0E
58:348 00:028 AAPL: #[EB.H.LV|!] Err(0xE) <- RT.GV boot-image-key 7C436110-AB2A-4BBB-A880-FE41995C9F82
58:376 00:028 AAPL: #[EB|WL] 0 0 0x01 0x01  24 0x0E
58:417 00:041 AAPL: #[EB.H.LV|!] Err(0xE) <- RT.GV boot-image 7C436110-AB2A-4BBB-A880-FE41995C9F82
58:446 00:029 AAPL: #[EB.H.LV|!] Err(0xE) <- RT.SV- boot-signature 7C436110-AB2A-4BBB-A880-FE41995C9F82
58:489 00:042 AAPL: #[EB.H.LV|!] Err(0xE) <- RT.SV- boot-image-key 7C436110-AB2A-4BBB-A880-FE41995C9F82
58:518 00:029 AAPL: #[EB.H.LV|!] Err(0xE) <- RT.SV- boot-image 7C436110-AB2A-4BBB-A880-FE41995C9F82
58:546 00:028 AAPL: #[EB|H:NOT]
58:588 00:041 AAPL: #[EB|SB:P] 0x0
58:617 00:028 AAPL: #[EB|LIMG:DP] VenMedia(957932CC-7E8E-433B-8F41-D391EA3C10F8)/MemMap(10:100000000-100001000)/DMG_00000000429DA62C.dmg/VenMedia(004B07E8-0B9C-427E-B0D4-A466E6E57A62)/HD(Part1,Sig3EF0A4E6-FADB-48EE-BDF1-5848917FAEA7)/VenMedia(BE74FCF7-0B7C-49F3-9147-01F4042E6842)
58:658 00:041 AAPL: #[EB|LIMG:FP] \3191640C-E47A-4121-AB93-9DBA36797683\System\Library\CoreServices\boot.efi
58:687 00:028 AAPL: #[EB|LIMG:OPT] 
58:715 00:028 AAPL: #[EB.B.OBV|BM:+DMG]
58:770 00:054 AAPL: #[EB.B.OBV|BM:+ROS]
58:798 00:028 AAPL: #[EB.OPT.LXF|F] <"\\3191640C-E47A-4121-AB93-9DBA36797683\\System\\Library\\CoreServices\\com.apple.Boot.plist">
58:839 00:041 AAPL: #[EB.LD.LF|IN] 0 1 <"\\3191640C-E47A-4121-AB93-9DBA36797683\\System\\Library\\CoreServices\\com.apple.Boot.plist"> <"0">
58:868 00:028 AAPL: #[EB.LD.OFS|OPEN!] Err(0xE) <"\\3191640C-E47A-4121-AB93-9DBA36797683\\System\\Library\\CoreServices\\com.apple.Boot.plist">
58:896 00:028 AAPL: #[EB.OPT.LXF|LF!] Err(0xE)
58:924 00:028 AAPL: #[EB.OPT.LXF|F] <"Library\\Preferences\\SystemConfiguration\\com.apple.Boot.plist">
58:965 00:041 AAPL: #[EB.LD.LF|IN] 0 1 <"Library\\Preferences\\SystemConfiguration\\com.apple.Boot.plist"> <"0">
59:006 00:041 AAPL: #[EB|KF] <"">
59:035 00:028 AAPL: #[EB|MBA:CL] <"">
59:063 00:028 AAPL: #[EB|MBA:NV] <"-v debug=0x100 keepsyms=1 alcid=7">
59:091 00:028 AAPL: #[EB|MBA:KF] <"">
59:133 00:041 AAPL: #[EB|MBA:OUT] <"-v debug=0x100 keepsyms=1 alcid=7">
59:174 00:041 AAPL: #[EB|LOG:VERBOSE] 2023-03-20T08:25:48
59:203 00:028 AAPL: #[EB|OPT:BM] 0x8a1182
59:231 00:028 AAPL: #[EB.OPT.LXF|F] <"\\3191640C-E47A-4121-AB93-9DBA36797683\\System\\Library\\CoreServices\\PlatformSupport.plist">
59:259 00:027 AAPL: #[EB.LD.LF|IN] 0 1 <"\\3191640C-E47A-4121-AB93-9DBA36797683\\System\\Library\\CoreServices\\PlatformSupport.plist"> <"0">
59:300 00:041 AAPL: #[EB.B.MN|BM:ROS]
59:329 00:028 AAPL: #[EB|WL] 0 0 0x01 0x01  19 0x0E
59:370 00:041 AAPL: #[EB.CS.CSKSD|+]
59:400 00:029 AAPL: #[EB.G.CS|-?] Ok(0)
59:452 00:052 AAPL: #[EB.LD.LF|IN] 0 1 <"<null string>"> <"1">
59:496 00:043 AAPL: #[EB.B.SBS|SZ] 723512
59:533 00:036 AAPL: #[EB|B:SHA] <966d5e3bc8a58fe6f354f044a21095ae05081193>
59:581 00:048 AAPL: #[EB.WL.PWLFNV|!] Err(0xE) <- RT.GV wake-failure 7C436110-AB2A-4BBB-A880-FE41995C9F82
59:612 00:031 AAPL: #[EB.WL.DT|!] Err(0xE) <- EB.WL.PWLFNV
59:643 00:030 AAPL: #[EB|WL:DT] 0xb70ce90e
59:691 00:048 AAPL: #[EB.LD.LKC|R.1] <"boot\System\Library\KernelCollections\BootKernelExtensions.kc">
59:992 00:300 OC: Kext reservation size info 571000 exe 2D9000
60:047 00:055 OC: Trying 64-bit XNU hook on boot\System\Library\KernelCollections\BootKernelExtensions.kc
60:181 00:133 OC: Result of 64-bit XNU hook on boot\System\Library\KernelCollections\BootKernelExtensions.kc (F443C4D2) is Success
60:215 00:034 OCAK: Read kernel version 21.6.0 (210600)
60:258 00:043 OCAK: Zeroing _xcpm_core_scope_msrs 0xE2 applicable CPUs (76)
60:287 00:028 OCAK: Zeroing _xcpm_core_scope_msrs 0xE2 applicable CPUs (406416)
60:328 00:041 OCAK: Zeroing _xcpm_core_scope_msrs 0xE2 applicable CPUs (16384)
60:357 00:029 OCAK: 64-bit XcpmCfgLockRel replace count - 2
60:385 00:028 OCAK: [OK] Success XcpmCfgLock patch
60:429 00:043 OCAK: 64-bit PanicKextDump replace count - 1
60:471 00:041 OCAK: [OK] Patch success kext dump
60:513 00:042 OCAK: [OK] Patch success CPUID release
60:541 00:028 OCAK: 64-bit PowerStateTimeout replace count - 1
60:570 00:028 OCAK: [OK] Patch success inline power state
60:613 00:042 OCAK: [OK] Found jettisoning fileset
60:707 00:094 OCAK: Patching invalid size 6000 with 2834000 for com.apple.driver.AppleRTC
60:748 00:041 OCAK: 64-bit DisableRtcChecksum64 replace count - 4
60:777 00:028 OCAK: [OK] Patch success com.apple.driver.AppleRTC DisableRtcChecksum
60:821 00:043 OCAK: Local relocs 689 on FFFFFF8004265000
60:850 00:029 OC: Prelinked injection Lilu.kext (Lilu.kext) - Success
60:892 00:041 OC: Prelinked injection Lilu.kext v1.6.4
60:923 00:030 OCAK: Patching invalid size 2D000 with 142F000 for com.apple.iokit.IOPCIFamily
60:969 00:046 OCAK: Patching invalid size E000 with DF9000 for com.apple.kec.Libm
61:001 00:032 OCAK: Local relocs 703 on FFFFFF8004294000
61:032 00:030 OC: Prelinked injection RadeonSensor.kext (RadeonSensor.kext) - Success
61:073 00:041 OC: Prelinked injection RadeonSensor.kext v0.3.2
61:104 00:030 OCAK: Patching invalid size 1000 with FA5000 for com.apple.driver.AppleUSBHostMergeProperties
61:147 00:043 OCAK: Local relocs 309 on FFFFFF80042A8000
61:176 00:029 OC: Prelinked injection USBToolBox.kext (USBToolBox.kext) - Success
61:205 00:028 OC: Prelinked injection USBToolBox.kext v1.1.1
61:247 00:041 OC: Prelinked injection UTBMap.kext (UTBMap.kext) - Success
61:275 00:028 OC: Prelinked injection UTBMap.kext v1.1
61:320 00:045 OCAK: Local relocs 1869 on FFFFFF80042B1000
61:354 00:033 OC: Prelinked injection WhateverGreen.kext (WhateverGreen.kext) - Success
61:382 00:028 OC: Prelinked injection WhateverGreen.kext v1.6.4
61:434 00:051 OCAK: Local relocs 5746 on FFFFFF8004332000
61:500 00:066 OC: Prelinked injection AppleALC.kext (AppleALC.kext) - Success
61:542 00:041 OC: Prelinked injection AppleALC.kext v1.7.9
61:572 00:030 OCAK: Patching invalid size 2000 with 18D8000 for com.apple.iokit.IOACPIFamily
61:604 00:032 OCAK: Local relocs 515 on FFFFFF80044DA000
61:635 00:030 OC: Prelinked injection VirtualSMC.kext (VirtualSMC.kext) - Success
61:676 00:041 OC: Prelinked injection VirtualSMC.kext v1.3.0
61:721 00:044 OCAK: Local relocs 325 on FFFFFF80044F4000
61:750 00:029 OC: Prelinked injection SMCProcessor.kext (SMCProcessor.kext) - Success
61:779 00:028 OC: Prelinked injection SMCProcessor.kext v1.3.0
61:811 00:031 OCAK: Local relocs 307 on FFFFFF8004503000
61:853 00:042 OC: Prelinked injection SMCRadeonGPU.kext (SMCRadeonGPU.kext) - Success
61:882 00:028 OC: Prelinked injection SMCRadeonGPU.kext v0.3.2
61:926 00:044 OCAK: Local relocs 2168 on FFFFFF8004512000
61:965 00:038 OC: Prelinked injection SMCSuperIO.kext (SMCSuperIO.kext) - Success
61:994 00:028 OC: Prelinked injection SMCSuperIO.kext v1.3.0
62:038 00:044 OCAK: Local relocs 611 on FFFFFF8004533000
62:069 00:030 OC: Prelinked injection CPUFriend.kext (CPUFriend.kext) - Success
62:110 00:041 OC: Prelinked injection CPUFriend.kext v1.2.6
62:139 00:028 OC: Prelinked injection CPUFriendDataProvider.kext (CPUFriendDataProvider.kext) - Success
62:167 00:028 OC: Prelinked injection CPUFriendDataProvider.kext v1.0.0
62:221 00:054 OC: Prelink size 71163904 kext offset 68177920 reserved 2985984
62:250 00:028 OCAK: KC TEXT is 65536 bytes with 64096 Mach-O headers need 808
62:393 00:143 OC: Prelinked status - Success
62:533 00:139 AAPL: #[EB.LD.LKFS|-?] Ok(0)
62:563 00:029 AAPL: #[EB.LD.LKC|-?] Ok(0)
62:594 00:031 AAPL: #[EB|BST:REV1]
62:637 00:043 AAPL: #[EB|CSR:IN] 0x00000040
62:680 00:043 AAPL: #[EB|CSR:OUT] 0x00000040
62:710 00:029 AAPL: #[EB.BST.FBS|+]
62:740 00:030 AAPL: #[EB|GIP:PHS.1] Boot 3
62:771 00:030 AAPL: #[EB.BST.FBS|ADSZ] 0
62:814 00:043 AAPL: #[EB.BST.FBS|KSSZ] 0
62:858 00:043 AAPL: #[EB|SB:SBGMFNS] j185fap.im4m
62:889 00:031 AAPL: #[EB|RH:PF] usr\standalone\OS.dmg.root_hash
62:923 00:033 AAPL: #[EB|RH:MF] <"usr\\standalone\\OS.dmg.root_hash.j185fap.im4m">
62:956 00:033 AAPL: #[EB.LD.LF|IN] 0 1 <"usr\\standalone\\OS.dmg.root_hash"> <"0">
63:003 00:047 AAPL: #[EB.LD.OFS|OPEN!] Err(0xE) <"usr\\standalone\\OS.dmg.root_hash">
63:034 00:031 AAPL: #[EB.RH.LRH|P!] Err(0xE) <- EB.LD.LF
63:079 00:044 AAPL: #[EB.BST.FBS|!] Err(0xE) <- EB.RH.LRH
63:107 00:028 OCSMC: SmcReadValue Key 4D535463 Size 1
63:149 00:041 OCSMC: SmcReadValue Key 4D534163 Size 2
63:193 00:044 AAPL: #[EB|LOG:DT] 2023-03-20T08:25:52
63:225 00:032 AAPL: #[EB|LOG:EXITBS:START] 2023-03-20T08:25:52</pre>
</details>

<details>
<summary>Example LogCheck Output</summary>
  <pre>{
  "oc_version": "DBG-090-2023-03-06",
  "booted_os": "Apple Inc. macOS 11.0",
  "booted_kernel": "21.6.0",
  "cpus": [
    {
      "name": "11th Gen Intel(R) Core(TM) i9-11900K @ 3.50GHz",
      "apple_processor_type": "10 -> 1009",
      "cores_threads": "8/16"
    }
  ],
  "current_smbios": "System Product Name (TUF GAMING Z590-PLUS made by ASUSTeK COMPUTER INC.)",
  "target_smbios": "Acidanthera model iMac20,2",
  "boot-args": "-v debug=0x100 keepsyms=1 alcid=7",
  "cfg_lock": false,
  "mat_support": true,
  "secure_boot_model": {
    "j185f": "level 1"
  },
  "mmio_devirt": [
    "0xE0000000 (3758096384)",
    "0xFE000000 (4261412864)",
    "0xFEC00000 (4273995776)",
    "0xFED00000 (4275044352)",
    "0xFEE00000 (4276092928)",
    "0xFF000000 (4278190080)"
  ],
  "all_slides": true,
  "audio_controllers": {
    "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x1)": {
      "Codec 0x0": [
        "Codec ID: 0x1002:0xAA01",
        "Codec name: AMD (Unknown)",
        "Output at bit-0 (bitmask 1)",
        "Output at bit-1 (bitmask 2)",
        "Output at bit-2 (bitmask 4)",
        "Output at bit-3 (bitmask 8)",
        "Output at bit-4 (bitmask 16)",
        "Output at bit-5 (bitmask 32)"
      ]
    },
    "PciRoot(0x0)/Pci(0x1F,0x3)": {
      "Codec 0x0": [
        "Codec ID: 0x10EC:0xB00",
        "Codec name: Realtek (Unknown)",
        "Output at bit-0 (bitmask 1)",
        "Output at bit-1 (bitmask 2)",
        "Output at bit-2 (bitmask 4)",
        "Output at bit-3 (bitmask 8)",
        "Output at bit-4 (bitmask 16)",
        "Output at bit-5 (bitmask 32)",
        "Output at bit-6 (bitmask 64)",
        "Output at bit-7 (bitmask 128)"
      ],
      "Codec 0x2": [
        "Codec ID: 0x8086:0x2816",
        "Codec name: Intel (Unknown)",
        "Output at bit-0 (bitmask 1)"
      ]
    }
  },
  "acpi_add": [
    "SSDT -> AWAC",
    "SSDT -> CpuPlug",
    "SSDT -> RhubOff",
    "SSDT -> SsdtUsbx"
  ],
  "booter_quirks": [
    "AllowRelocationBlock -> 0",
    "AvoidRuntimeDefrag -> 1",
    "DevirtualiseMmio -> 1",
    "DisableSingleUser -> 0",
    "DisableVariableWrite -> 0",
    "DiscardHibernateMap -> 0",
    "EnableSafeModeSlide -> 1",
    "EnableWriteUnprotector -> 0",
    "ForceBooterSignature -> 0",
    "ForceExitBootServices -> 0",
    "ProtectMemoryRegions -> 0",
    "ProtectSecureBoot -> 0",
    "ProtectUefiServices -> 1",
    "ProvideCustomSlide -> 1",
    "ProvideMaxSlide -> 0",
    "RebuildAppleMemoryMap -> 1",
    "ResizeAppleGpuBars -> -1",
    "ResizeUsePciRbIo -> 0",
    "SetupVirtualMap -> 1",
    "SignalAppleOS -> 0",
    "SyncRuntimePermissions -> 1"
  ],
  "device_properties_add": {
    "PciRoot(0x0)/Pci(0x1C,0x4)/Pci(0x0,0x0)": [
      "device-id"
    ]
  },
  "kernel_add": {
    "Lilu.kext": "v1.6.4",
    "RadeonSensor.kext": "v0.3.2",
    "USBToolBox.kext": "v1.1.1",
    "UTBMap.kext": "v1.1",
    "WhateverGreen.kext": "v1.6.4",
    "AppleALC.kext": "v1.7.9",
    "VirtualSMC.kext": "v1.3.0",
    "SMCProcessor.kext": "v1.3.0",
    "SMCRadeonGPU.kext": "v0.3.2",
    "SMCSuperIO.kext": "v1.3.0",
    "CPUFriend.kext": "v1.2.6",
    "CPUFriendDataProvider.kext": "v1.0.0"
  },
  "kernel_quirks": [
    "Success XcpmCfgLock patch",
    "Patch success kext dump",
    "Patch success CPUID release",
    "Patch success inline power state",
    "Found jettisoning fileset",
    "Patch success com.apple.driver.AppleRTC DisableRtcChecksum"
  ],
  "emulated_nvram": false,
  "nvram_add": {
    "4D1EDE05-38C7-4A6A-9CC6-4BCCA8B38C14": [
      "DefaultBackgroundColor"
    ],
    "4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102": [
      "rtc-blacklist"
    ],
    "7C436110-AB2A-4BBB-A880-FE41995C9F82": [
      "ForceDisplayRotationInEFI",
      "SystemAudioVolume",
      "boot-args",
      "csr-active-config",
      "prev-lang:kbd",
      "run-efi-updater"
    ]
  },
  "nvram_delete": {
    "4D1EDE05-38C7-4A6A-9CC6-4BCCA8B38C14": [
      "DefaultBackgroundColor"
    ],
    "4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102": [
      "rtc-blacklist"
    ],
    "7C436110-AB2A-4BBB-A880-FE41995C9F82": [
      "boot-args",
      "ForceDisplayRotationInEFI"
    ]
  },
  "uefi_drivers": [
    "HfsPlus.efi",
    "OpenRuntime.efi",
    "ResetNvramEntry.efi",
    "AudioDxe.efi",
    "OpenCanopy.efi"
  ],
  "picker_entries": [
    "macOS Installer [Apple]",
    "Windows [Windows]",
    "MONTEREY [Auto]",
    "EFI [Auto]",
    "Recovery [AppleRecv:Apple]",
    "MONTEREY [AppleRecv:Apple]",
    "OpenShell.efi [Auto]",
    "CleanNvram.efi [Auto]",
    "Reset NVRAM [ResetNVRAM:NVRAMTool]"
  ],
  "booted_entry": "6. Recovery"
}</pre>
</details>
