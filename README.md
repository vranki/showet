# showet

Demo viewer using Pouet.net's metadata

Consider this "MAME for demos"

##Idea
* Browse and search demos using pouet.net's database
* Select a demo, it will be downloaded and set up
* Easily run the demo natively or using emulator or wine
* Support windows .exe (wine), Amiga (UAE), C64 (Vice) etc demos
* Smart autodetection as far as possible
* When autodetection fails, allow per-demo metadata to define how it should be run

##Current implementation
* Proof of concept python script that can download & run demos
* Supported platforms: windows .exe

##Example

To see MFX's Deities (http://www.pouet.net/prod.php?which=24487) 

Run:

```
./showet.py 24487
```

Make sure you have python3, unzip and wine installed:

```
sudo apt install python3 unzip wine
```
In future debian packaging should handle these

##Todo

- [x] Proof of concept
- [x] Windows support
- [ ] Amiga support
- [ ] C64 support
- [ ] DOS support
- [ ] GUI
- [x] unzip decompress
- [ ] LhA decompress
- [ ] Design metadata format to fix non-working demos
- [ ] Disk change support (C64/Amiga)
- [ ] debian packaging
- [ ] Whitelist & blacklist of known working & broken demos

Pull requests welcome, although this is still in very early development.

