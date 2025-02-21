import requests
import json



'''For now we are just assuming all binaries are given in the form of tar.gz'''



repos = "https://raw.githubusercontent.com/Nareshix/repos/refs/heads/main/apps.json"

response = requests.get(repos)
data = json.loads(response.text)


def show_error():
    print(f"Failed to retrieve the file. Status code: {response.status_code}")


def get_download_link(app):
    if response.status_code == 200:
        return data[app]["download_link"]
    else:
        show_error()

def get_symlink(app):
    if response.status_code == 200:
        return data[app]["symlink"]
    else:
        show_error()

def check_multiple_files(app):
    if response.status_code == 200:
        return data[app]["multiple_files"]
    else:
        show_error()


