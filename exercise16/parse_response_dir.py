import json
import requests
import os

auth_token = os.environ.get("ANSIBLE_TOKEN")

parsed_response = []
dir_to_find = ".vagrant"


with open("./response.json", "r") as f_read:
    data = json.load(f_read)
    for i in range(len(data)):
        if type(data[i]['json']) == list:
            for j in range(len(data[i]['json'])):
                if data[i]['json'][j]['type'] == 'dir':
                    url = data[i]['json'][j]['url']
                    response = requests.get(url, headers={"Authorization": "token "+auth_token})
                    # print(response.json())
                    for resp in response.json():
                        if resp['type'] == 'dir' and dir_to_find in resp['path']:
                            parsed_response.append({"url": resp["url"], "sha": resp["sha"]})
                   
print(parsed_response)
