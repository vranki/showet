from platformcommon import PlatformCommon
import os

class PlatformAmiga(PlatformCommon):
    def run(self):
        dmss = self.find_files_with_extension('dms')
        if len(dmss) == 0:
            print("Didn't find any dms files.")
            exit(-1)

        # Support only one for now..
        drive_0 = dmss[0]

        amiga_model = 'A1200'
        if self.prod_platform == 'amigaocsecs':
            amiga_model = 'A500'

        fsuae_opts = '--fullscreen --keep_aspect --floppy_drive_0=' + drive_0 + ' --amiga_model=' + amiga_model
        print("Running fs-uae with options: " + fsuae_opts)
        os.chdir(self.datadir)
        os.system('fs-uae ' + fsuae_opts)

    def supported_platforms(self):
        return ['amigaocsecs', 'amigaaga']
