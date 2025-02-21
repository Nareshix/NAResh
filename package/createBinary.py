import os
from package.fetchData import get
import subprocess

home_dir = os.path.expanduser('~')
STORAGE_FOLDER_PATH = home_dir + '/' + '.naresh' # $HOME/.naresh

def createBinary(app):
    if not os.path.exists(STORAGE_FOLDER_PATH):
        os.makedirs(STORAGE_FOLDER_PATH)
        
    APP_PATH = STORAGE_FOLDER_PATH + '/' + app
    if not os.path.exists(APP_PATH):
        os.makedirs(APP_PATH)

    website_url = get(app,"download_link")

    #Downloads file
    subprocess.run(['wget',  website_url ])

    fileName = website_url.split('/')[-1]

    #extracts the file to local binary
    subprocess.run(["sudo", "tar", "-xvzf",fileName , "-C", APP_PATH])
    
    os.remove(fileName)     

    #Create a symlink (available to use anywhere in terminal)
    subprocess.run(['ln', '-s', APP_PATH, get(app,'symlink')])  