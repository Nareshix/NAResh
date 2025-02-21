import os
from package.fetchData import check_multiple_files, get_download_link
import subprocess


BINARY_PATH = r'/usr/local/bin'

def createBinary(app):
    if check_multiple_files(app):
        
        if not os.path.exists(BINARY_PATH):
            os.makedirs(BINARY_PATH)

        website = get_download_link(app)

        #Downloads file
        subprocess.run(['wget',  website ])

        fileName = website.split('/')[-1]

        #extracts the file to local binary
        subprocess.run(["sudo", "tar", "-xvzf",fileName , "-C", BINARY_PATH])

        os.remove(fileName)
