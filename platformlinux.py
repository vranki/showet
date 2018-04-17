from platformcommon import PlatformCommon
import os
import stat

class PlatformLinux(PlatformCommon):
    def run(self):
        exes = self.find_executable_files()

        if len(exes) == 0 :
            print("Didn't find any executable binaries.")
            exit(-1)

        os.chdir(self.datadir)
        if len(exes) > 1:
            print("Found executables: ", exes, " - not sure which one to run!")
        else:
            print("Running ", exes[0])
        os.system(exes[0])

    def supported_platforms(self):
        return ['linux']

# Tries to identify d64 files by any magic necessary
    def find_executable_files(self):
        exe_files = []
        for file in self.prod_files:
            mode = os.stat(file).st_mode
            if stat.S_IXUSR & mode:
                exe_files.append(file)
        return exe_files
