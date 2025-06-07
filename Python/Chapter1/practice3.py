import os

# Specify the directory path
directory = 'C:\\Users\\aakan\\OneDrive\\Desktop\\Python\\Chapter1'  # Current directory; you can change this to any path

# List all files and directories
entries = os.listdir(directory)

# Filter and list only files
files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]

print("Files in directory:", directory)
for file in files:
    print(file)