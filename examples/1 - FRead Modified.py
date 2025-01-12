import json

with open('F.fest', 'r') as file:
    data = json.load(file)
    print("Freakifest Version: " + data['f_ver'])
    print("Name: " + data['name'])
    print("Software Version: " + data['soft_ver'])
    print("Description: " + data['description'])
    print("Minimum FreakyBrowse Version: " + data['MinFBVersion'])
    file.close()