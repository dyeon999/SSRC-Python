import os
current_directory = os.getcwd()
print("Current working directory: ", current_directory)

file_path = "file.txt"

if os.path.isfile(file_path):
    print(f"{file_path} is a file")
else: print(f"{file_path} is not a file")

dir_path = "Day01"

if os.path.isdir(dir_path):
    print(f"{dir_path} is a directory")
else: print(f"{dir_path} is not a directory")
