# showet

Demo viewer using Pouet.net's metadata

Consider this "MAME for demos"

Developed on Ubuntu 17.10, other platforms may work.

## Idea
* Browse and search demos using pouet.net's database
* Select a demo, it will be downloaded and set up
* Easily run the demo natively or using emulator or wine
* Support at least windows .exe (wine), Amiga (UAE), C64 (Vice) demos
* Smart autodetection as far as possible
* Support per-demo metadata to define how it should be run if autodetection fails

## Current implementation
* Proof of concept python script that can download & run demos
* Supported platforms: windows .exe, Amiga (.adf, .dms, .lha)

## Examples

Windows: MFX's Deities (http://www.pouet.net/prod.php?which=24487) 
```
./showet.py 24487
```
Amiga/dms Origin by Complex (http://www.pouet.net/prod.php?which=3741)
```
./showet.py 3741
```
Amiga/lha Tint by TBL (http://www.pouet.net/prod.php?which=701)
```
./showet.py 701
```

Make sure you have dependencies installed:
```
sudo apt install python3 unzip wine fs-uae lhasa
```
In future debian packaging should handle these

For Amiga demos you'll need kickstart rom files. See
http://fs-uae.net/docs/kickstarts on how to obtain and install those.
Only DMS and ADF packed single disk demos are supported for now.

## Todo

- [x] Proof of concept
- [x] Windows support
- [x] Amiga support
- [ ] C64 support
- [ ] DOS support
- [ ] GUI
- [x] unzip decompress
- [x] LhA decompress
- [ ] Design metadata format to fix non-working demos
- [ ] Disk change support (C64/Amiga)
- [ ] debian packaging
- [ ] Whitelist & blacklist of known working & broken demos

Pull requests welcome, although this is still in very early development.

