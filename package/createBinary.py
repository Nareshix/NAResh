import os
from package.fetchData import check_multiple_files, get_download_link
import subprocess


LOCAL_BIN_PATH = r'/usr/local/bin'

def createBinary(app):
    BINARY_PATH = f'{LOCAL_BIN_PATH}/{app}'

    # if not os.path.exists(LOCAL_BIN_PATH):
    #     os.makedirs(LOCAL_BIN_PATH)

    
    subprocess.run(['sudo', 'mkdir', BINARY_PATH])

    website_url = get_download_link(app)

    #Downloads file
    subprocess.run(['wget',  website_url ])

    fileName = website_url.split('/')[-1]

    #extracts the file to local binary
    subprocess.run(["sudo", "tar", "-xvzf",fileName , "-C", BINARY_PATH])
    
    os.remove(fileName)       