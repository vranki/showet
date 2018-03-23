#!/usr/bin/env python3
import urllib.request, json
import os
import sys
from platformwindows import PlatformWindows
from platformamiga import PlatformAmiga

# Note: This is still early proof of concept, but seems to work.

if len(sys.argv) != 2:
    print("Usage: ./showet.py <pouet id>")
    exit(-1)

prod_id = int(sys.argv[1])

if(prod_id < 1):
    print("Invalid prod id!")
    exit(-1)

prod_url = "http://api.pouet.net/v1/prod/?id=" + str(prod_id)

datadir = "data/"+str(prod_id)
prod_download_url = None
prod_download_filename = None
prod_json = None
prod_json_filename = datadir + "/pouet.json"

print("Prod URL: " + prod_url)

# Get the json data:
if os.path.exists(prod_json_filename):
    print("Json already downloaded")
    with open(prod_json_filename, 'r') as f:
        prod_json = f.read()
else:
    if not os.path.exists(datadir):
        os.makedirs(datadir)
    with urllib.request.urlopen(prod_url) as url:
        prod_json = url.read().decode()
    with open(prod_json_filename, 'w') as f:
        f.write(prod_json)
        f.close()

print(prod_json)

data = json.loads(prod_json)

platforms = data['prod']['platforms'].values()

# Just pick one:
prod_platform = None
for p in platforms:
    prod_platform = p['slug']

print("\tName: " + data['prod']['name'])
try:
    print("\tBy: " + data['prod']['groups'][0]['name'])
except IndexError:
    pass
print("\tType: " + data['prod']['type'])
print("\tReleased: " + data['prod']['releaseDate'])
print("\tPlatform: " + prod_platform)

platorm_runners = [PlatformAmiga(), PlatformWindows()]
runner = None

for r in platorm_runners:
    if prod_platform in r.supported_platforms():
        runner = r

if not runner:
    print("Platform " + prod_platform + " not supported (yet!).")
    exit(-1)

# Get necessary fields from the data

prod_download_url = data['prod']['download']
prod_download_url = prod_download_url.replace("https://files.scene.org/view", "https://files.scene.org/get")
prod_download_filename = prod_download_url.split('/')
prod_download_filename = datadir + "/" +prod_download_filename[len(prod_download_filename)-1]

# Download the prod if needed
if not prod_download_filename:
    print("Error: couldn't get filename")
    exit(-1)

if os.path.exists(datadir + "/_FILES_DOWNLOADED"):
    print("File already downloaded")
else:
    print("Downloading prod file from " + prod_download_url + "...")
    filedata = urllib.request.urlopen(prod_download_url)
    datatowrite = filedata.read()

    with open(prod_download_filename, 'wb') as f:
        f.write(datatowrite)

    print("Downloaded ", prod_download_filename)


    # Decompress the file if needed
    if prod_download_filename.endswith(".zip"):
        print("Unzipping", prod_download_filename)
        ret = os.system("unzip -u -d " + datadir + " " + prod_download_filename)
        if ret == 0:
            # Delete the original file
            os.remove(prod_download_filename)
        else:
            print("Unzipping file failed!")

    if prod_download_filename.endswith(".lha"):
        print("Extracting lha ", prod_download_filename)
        ret = os.system("lha xw=" + datadir + " " + prod_download_filename)
        if ret == 0:
            # Delete the original file
            os.remove(prod_download_filename)
        else:
            print("Unzipping file failed!")

    open(datadir + "/_FILES_DOWNLOADED", 'a').close()

runner.setup(datadir, prod_platform)
runner.run()
