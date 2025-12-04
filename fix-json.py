import json

# Read the Python dict format
with open('GSS.json', 'r') as f:
    content = f.read()

# Use eval to parse it as Python (safe here since it's your own file)
data = eval(content)

# Write it back as proper JSON
with open('GSS-fixed.json', 'w') as f:
    json.dump(data, f)

print("✅ Fixed! Saved as GSS-fixed.json")