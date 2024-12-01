import os

# usage: change year and run script
# folders and files will be created for each year
folder_name = "2024"

file_names = ["main.py", "data.txt", "test_data.txt"]

for day in range(1, 26):
    d = f"day_{day:02}"
    folder_path = os.path.join(folder_name, d)
    os.makedirs(folder_path, exist_ok=True)
    
    for file in file_names:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'w') as f:
            pass

print(f"Folders and Files created in folder '{folder_name}'")