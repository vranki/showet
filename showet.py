#!/usr/bin/env python3
import urllib.request, json
import os.path
from os import listdir
import sys

# Note: This is still early proof of concept, but seems to work.

if len(sys.argv) != 2:
    print("Usage: ./shouet.py <pouet id>")
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
wineprefix = os.getcwd() + '/wineprefix'

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

data = json.loads(prod_json)

# Get necessary fields from the data

prod_download_url = data['prod']['download']
prod_download_url = prod_download_url.replace("https://files.scene.org/view", "https://files.scene.org/get")
prod_download_filename = prod_download_url.split('/')
prod_download_filename = prod_download_filename[len(prod_download_filename)-1]

# Download the prod if needed
if not prod_download_filename:
    print("Error: couldn't get filename")
    exit(-1)

if os.path.exists(prod_download_filename):
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
    if ret != 0:
        print("Unzipping file failed!")

else:
    print("TODO: Currently only zipped files supported..")
    exit(-1)

# Delete the original file
os.remove(prod_download_filename)

# Guess which file to execute
files = [f for f in listdir(datadir) if os.path.isfile(os.path.join(datadir, f))]

exefiles = [f for f in files if (f.lower().endswith(".exe") or f.lower().endswith(".EXE")) ]

if len(exefiles) == 0:
    print("Didn't find any exe files.")
    exit(-1)

exefile = exefiles[0]

print("Guessed executable file: " + exefile)

exepath = datadir + "/" + exefile

# Setup wine if needed

os.putenv("WINEPREFIX", wineprefix)

if not os.path.exists(wineprefix):
    os.makedirs(wineprefix)
    print("Creating wine prefix: " + str(wineprefix))
    os.system('WINEARCH="win32" winecfg')

# Run the demo

print("Running " + exepath + "...")
os.chdir(datadir)
os.system('wine ' + exefile)
