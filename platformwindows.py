from platformcommon import PlatformCommon
from os import listdir
import os.path

class PlatformWindows(PlatformCommon):
    def run(self):
        wineprefix = self.showetdir + '/wineprefix'

        exefiles = self.find_files_with_extension('exe')

        if len(exefiles) == 0:
            print("Didn't find any exe files.")
            exit(-1)

        exefile = exefiles[0]

        print("Guessed executable file: " + exefile)

        exepath = self.datadir + "/" + exefile

        # Setup wine if needed

        os.putenv("WINEPREFIX", wineprefix)

        if not os.path.exists(wineprefix):
            os.makedirs(wineprefix)
            print("Creating wine prefix: " + str(wineprefix))
            os.system('WINEARCH="win32" winecfg')

        # Run the demo

        print("Running " + exepath + "...")
        os.chdir(self.datadir)
        os.system('wine ' + exefile)

    def supported_platforms(self):
        return ['windows']
