import json

dirs = []
dir_to_find = ".vagrant"

with open("./result.json", "r") as f_read:
    data = json.load(f_read)

    for line in data:
        if dir_to_find in line['path']:
            dirs.append(line['path'])

dirs.sort()
print(dirs)