import os
from package.fetchData import get
import subprocess
import platform

home_dir = os.path.expanduser('~')
STORAGE_FOLDER_PATH = home_dir + '/' + '.naresh' # $HOME/.naresh


def createBinary(app):
    if not os.path.exists(STORAGE_FOLDER_PATH):
        os.makedirs(STORAGE_FOLDER_PATH)
    APP_PATH = STORAGE_FOLDER_PATH + '/' + app + '/'


    #if offical ppa exists, use that instead
    if get(app,"official_ppa"):  
        for command in get(app,"download"):
            subprocess.run(command, shell=True, check=True)
        
        if not os.path.exists(APP_PATH):
            os.makedirs(APP_PATH)
        return


    # creates the folder for the app
    if not os.path.exists(APP_PATH):
        os.makedirs(APP_PATH)    

    website_url = get(app,"download")


    #Directly download bin if no tar.gz
    if not website_url.endswith('.tar.gz'):
        subprocess.run(['wget', "-P", APP_PATH, website_url])
    else:
        #Downloads file
        subprocess.run(['wget',  website_url ])

        fileName = website_url.split('/')[-1]

        #extracts the file to local binary
        subprocess.run(["sudo", "tar", "-xvzf",fileName ,"--strip-components=1", "-C", APP_PATH])

        os.remove(fileName)     


    symlink = get(app,'symlink')
    BIN_PATH = APP_PATH + get(app,'bin_path')

    
    if not os.access(BIN_PATH, os.X_OK): # if not executable
        os.chmod(BIN_PATH, 0o755)  # chmod +x

    #Create a symlink
    subprocess.run(['sudo', 'ln', '-s', BIN_PATH , f"/usr/local/bin/{symlink}"])  