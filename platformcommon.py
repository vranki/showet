import os
import os.path

class PlatformCommon:
    prod_files = []

    def __init__(self):
        self.showetdir = None
        self.datadir = None
        self.prod_platform = None
        self.prod_files = []

# TODO: Change this to be relative to datadir
    def find_files_recursively(self, path):
        entries = [os.path.join(path,i) for i in os.listdir(path)]
        if len(entries) == 0:
                return

        for e in entries:
            if os.path.isfile(e):
                self.prod_files.append(os.path.realpath(e))
            elif os.path.isdir(e):
                self.find_files_recursively(e)

    def setup(self, showetdir, datadir, prod_platform):
        self.showetdir = showetdir
        self.datadir = datadir
        self.prod_platform = prod_platform
        self.find_files_recursively(self.datadir)

    def supported_platforms(self):
        return None

    def find_files_with_extension(self, extension):
        foundfiles = [f for f in self.prod_files if (f.lower().endswith(extension) or f.lower().endswith(extension))]
        return foundfiles
