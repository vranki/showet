from platformcommon import PlatformCommon
import os

class PlatformAmiga(PlatformCommon):
    def run(self):
        adfs = self.find_files_with_extension('adf')
        dmss = self.find_files_with_extension('dms')
        exes = self.find_files_with_extension('exe')
        if len(exes) == 0:
            exes = self.find_magic_cookies()

        if len(dmss) == 0 and len(adfs) == 0 and len(exes) == 0:
            print("Didn't find any dms, adf or executable files.")
            exit(-1)

        fsuae_opts = '--fullscreen --keep_aspect '
        drives = []
        # Support only one for now..
        if len(dmss) > 0:
            drives = self.sort_disks(dmss)
        elif len(adfs) > 0:
            drives = self.sort_disks(adfs)
        elif len(exes) > 0:
            fsuae_opts += '--hard_drive_0=. '
            if not os.path.exists(self.datadir + "/s"):
                os.makedirs(self.datadir + "/s")
# TODO: when find_files_with_extension works with paths relative to datadir, we can simplify this
                with open(self.datadir + "/s/startup-sequence", 'w') as f:
                    exename = exes[0].split('/')
                    exename = exename[len(exename)-1]
                    f.write(exename + "\n")
                    f.close()

        amiga_model = 'A1200'
        if self.prod_platform == 'amigaocsecs':
            amiga_model = 'A500'

        if self.prod_platform == 'amigaaga':
            fsuae_opts += '--fast_memory=8192 '
# --chip_memory=2048
        if len(drives) > 0:
            fsuae_opts += '--floppy_drive_0=' + drives[0] + ' '
        if len(drives) > 1:
            fsuae_opts += '--floppy_drive_1=' + drives[1] + ' '
        if len(drives) > 2:
            fsuae_opts += '--floppy_drive_2=' + drives[2] + ' '
        if len(drives) > 3:
            fsuae_opts += '--floppy_drive_3=' + drives[3] + ' '

        fsuae_opts += '--amiga_model=' + amiga_model + ' '

        print("Running fs-uae with options: " + fsuae_opts)
        os.chdir(self.datadir)
        os.system('fs-uae ' + fsuae_opts)

    def supported_platforms(self):
        return ['amigaocsecs', 'amigaaga']

# Search demo files for amiga magic cookie (executable file)
    def find_magic_cookies(self):
        cookie_files = []
        for file in self.prod_files:
            with open(file, "rb") as fin:
                header = fin.read(4)
                if len(header) == 4:
                    # Signature for Amiga magic cookie
                    if header[0]==0 and header[1]==0 and header[2]==3 and header[3] == 243:
                        cookie_files.append(file)
        return cookie_files