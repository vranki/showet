# showet

Demo viewer using Pouet.net's metadata

Consider this "MAME for demos"

Developed on Ubuntu 17.10, other platforms may work.

![Screenshot](screenshot.png?raw=true "Screenshot of the GUI")

## Idea

* Browse and search demos using pouet.net's database
* Select a demo, it will be downloaded and set up
* Easily run the demo natively or using emulator or wine
* Support at least linux, windows .exe (wine), Amiga (UAE), C64 (Vice) demos
* Smart autodetection as far as possible
* Support per-demo metadata to define how it should be run if autodetection fails

## Current implementation
* Python script that can download & run demos
* Supported platforms: windows .exe, Amiga (.adf, .dms, .lha), C64 (.prg, .d64)
* GUI frontend

## Usage

* Install the debian package (available in github releases page)
* Launch showet from menu
* Search for a production and click run to run it
* Alt-F4 quits from emulators

### Amiga Notes ###

For Amiga demos you'll need kickstart rom files. See
http://fs-uae.net/docs/kickstarts on how to obtain and install those.

Setup fs-uae default settings to your liking - it'll be used as
base for launching amiga demos.

### C64 Notes ###

Vice shipped with Ubuntu doesn't contain kernal files due to
copyright reasons.

* Go to http://vice-emu.sourceforge.net/index.html#download and download
the source tarball.
* Create directory ~/.vice
* Copy everything from tarball's data/ directory to ~/.vice

You can configure vice / x64 any way you want. Showet starts it
with -fullscreen by default

Use Alt-N to cycle disk sides for multi-disk demos.

## Todo

- [x] Proof of concept
- [x] Windows support
- [x] Amiga support
- [x] C64 support
- [ ] DOS support
- [ ] Linux support
- [x] GUI
- [x] unzip decompress
- [x] LhA decompress
- [ ] Design metadata format to fix non-working demos
- [ ] Disk change support (C64/Amiga)
- [x] debian packaging
- [ ] Whitelist & blacklist of known working & broken demos

Pull requests welcome.

## Command line examples

You can use the command line tool to quickly test running any demos.

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
C64/.d64 Comaland by Censor Design & Oxyron (http://www.pouet.net/prod.php?which=64283)
```
./showet.py 64283
```

To build debian package, run:
```
debuild -us -uc -b
```
[![asciicast](https://asciinema.org/a/sXH854ysSs5Ya5C9EGRQB0TzV.png)](https://asciinema.org/a/sXH854ysSs5Ya5C9EGRQB0TzV)

Install the package to get dependencies.

## Authors: 

Code:        Ville Ranki
Logo & Icon: Manu / Fit 
