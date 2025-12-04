import json

with open('GSS.json', 'r') as f:
    content = f.read()

data = eval(content)

with open('GSS-fixed.json', 'w') as f:
    json.dump(data, f)

print("Fixed! Saved as GSS-fixed.json")