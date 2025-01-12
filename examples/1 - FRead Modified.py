import json

print("Freakifest Validator for FreakyBrowse")
print("Warning! If you do not have F.json in the same directory, or its not set up properly, your Freakifest will not work.")
try:
    with open('F.fest', 'r') as file:
        data = json.load(file)
        print("Freakifest Version: " + data['f_ver'])
        print("Name: " + data['name'])
        print("Software Version: " + data['soft_ver'])
        print("Description: " + data['description'])
        print("Minimum FreakyBrowse Version: " + data['MinFBVersion'])
        print("Success! ✅")
        file.close()
except:
    print("Validation failed! ❌")