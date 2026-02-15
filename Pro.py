import os

# specify the directory you want to list
directory_path = "/New folder"  # change this to the directory you want

try:
    # get the list of all files and folders in the directory
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied!")
 