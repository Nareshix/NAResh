import os
from package.fetchData import get
import subprocess

home_dir = os.path.expanduser('~')
STORAGE_FOLDER_PATH = home_dir + '/' + '.naresh' # $HOME/.naresh

ALIAS = {
    "codium": "vscodium"
}

def createBinary(app):
    if app in ALIAS:
        app = ALIAS[app]

    if get(app,"official_ppa"):  #if offical ppa exists, use that instead
        for command in get(app,"download"):
            subprocess.run(command, shell=True, check=True)
        return
    




#     if not os.path.exists(STORAGE_FOLDER_PATH):
#         os.makedirs(STORAGE_FOLDER_PATH)
        
#     APP_PATH = STORAGE_FOLDER_PATH + '/' + app
#     if not os.path.exists(APP_PATH):
#         os.makedirs(APP_PATH)

#     website_url = get(app,"download_link")

#     #Downloads file
#     subprocess.run(['wget',  website_url ])

#     fileName = website_url.split('/')[-1]

#     #extracts the file to local binary
#     subprocess.run(["sudo", "tar", "-xvzf",fileName , "-C", APP_PATH])
    
#     os.remove(fileName)     

#     #Create a symlink (available to use anywhere in terminal)
#     symlink = get(app,'symlink')
#     subprocess.run(['sudo', 'ln', '-s', f'{APP_PATH}/{symlink}' , f"/usr/local/bin/{symlink}"])  