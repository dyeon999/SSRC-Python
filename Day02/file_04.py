"""Write&Read text in file"""

# # Write
# with open('Day02/file_ex.txt', 'w', encoding='utf-8') as file:
#     file.write("Hello, it's Python Time!\n")
#     file.write("If you use 'with', the file will be closed automatically.\n")

# Read
with open('Day02/file_ex.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

print("="*50)

# ReadLine - read the line one by one
with open('Day02/file_ex.txt', 'r', encoding='utf-8') as file:
    print(file.readline())  # read first line and move the curser to the next line
    print(file.readline())  # read second line and move the curser to the next line


# ReadLines 
with open('Day02/file_ex.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)


