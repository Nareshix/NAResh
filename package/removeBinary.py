import os
from package.fetchData import delete
import subprocess
import pathlib
home_dir = os.path.expanduser('~')
STORAGE_FOLDER_PATH = home_dir + '/' + '.naresh' # $HOME/.naresh


# HANDLING ppa for now
def removeBinary(app):
    APP_PATH = STORAGE_FOLDER_PATH + '/' + app

    if os.path.exists(APP_PATH):
        for command in  delete(app):
            subprocess.run(command, shell=True, check=True)
        
        #rmdir (rm empty dir) as these files r used only for tracking
        pathlib.Path.rmdir(APP_PATH)
    return