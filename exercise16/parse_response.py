parsed_response = []
string_to_find = ".DS_Store"
import json
with open("./response.json", "r") as f_read:
    data = json.load(f_read)
    for i in range(len(data)):
        if type(data[i]['json']) == list:
            for j in range(len(data[i]['json'])):
                if data[i]['json'][j]['type'] == 'file' and string_to_find in data[i]['json'][j]['path']:
                    parsed_response.append({"url": data[i]['json'][j]['url'], "sha": data[i]['json'][j]['sha']})

print(parsed_response)
