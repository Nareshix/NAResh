import requests
import json



'''For now we are just assuming all binaries are given in the form of tar.gz'''



repos = "https://raw.githubusercontent.com/Nareshix/repos/refs/heads/main/apps.json"
delete_repos = "https://raw.githubusercontent.com/Nareshix/repos/refs/heads/main/delete_apps.json"



def get(app,attribute):
    response = requests.get(repos)
    data = json.loads(response.text)

    if response.status_code == 200:
        return data[app][attribute]
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")

def delete(app):
    response = requests.get(delete_repos)
    data = json.loads(response.text)

    if response.status_code == 200:
        return data[app]
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")
