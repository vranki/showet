from platformcommon import PlatformCommon
import os

class PlatformAmiga(PlatformCommon):
    def run(self):
        adfs = self.find_files_with_extension('adf')
        dmss = self.find_files_with_extension('dms')
        exes = self.find_files_with_extension('exe')
        if len(dmss) == 0 and len(adfs) == 0 and len(exes) == 0:
            print("Didn't find any dms, adf or exe files.")
            exit(-1)

        fsuae_opts = '--fullscreen --keep_aspect '
        drive_0 = None
        # Support only one for now..
        if len(dmss) > 0:
            drive_0 = dmss[0]
        elif len(adfs) > 0:
            drive_0 = adfs[0]
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

        if self.prod_platform == 'amigaaaga':
            fsuae_opts += '--fast_memory=8192 '

        if drive_0:
            fsuae_opts += '--floppy_drive_0=' + drive_0 + ' '

        fsuae_opts += '--amiga_model=' + amiga_model + ' '

        print("Running fs-uae with options: " + fsuae_opts)
        os.chdir(self.datadir)
        os.system('fs-uae ' + fsuae_opts)

    def supported_platforms(self):
        return ['amigaocsecs', 'amigaaga']
