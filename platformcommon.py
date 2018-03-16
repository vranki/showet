import os
import os.path

class PlatformCommon:
    def __init__(self):
        self.datadir = None
        self.prod_platform = None

    def setup(self, datadir, prod_platform):
        self.datadir = datadir
        self.prod_platform = prod_platform

    def supported_platforms(self):
        return None

    def find_files_with_extension(self, extension):
        files = [f for f in os.listdir(self.datadir) if os.path.isfile(os.path.join(self.datadir, f))]

        foundfiles = [f for f in files if (f.lower().endswith(extension) or f.lower().endswith(extension))]
        return foundfiles
