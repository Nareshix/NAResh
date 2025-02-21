import requests
import json



'''For now we are just assuming all binaries are given in the form of tar.gz'''



repos = "https://raw.githubusercontent.com/Nareshix/repos/refs/heads/main/apps.json"

response = requests.get(repos)
data = json.loads(response.text)


def get(app,attribute):
    if response.status_code == 200:
        return data[app][attribute]
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")
