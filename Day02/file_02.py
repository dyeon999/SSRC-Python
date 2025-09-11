import os

files = os.listdir('.')
print(files)

for file in files:
    print(file)

print()
print("--------------------")

files = os.walk('.') # Directory 탐색 -> 위에서 아래로 쭉 훑어내려감 & 구조 파악도 가능
print(files) # 그냥 데이터가 아니라 object형태로 묶여있음
'''
<generator object walk at 0x00000179021F7850> 
'''

for dirpath, dirnames, filenames in files:
    print(f"Found directory: {dirpath}")
    print(f"Subdir: {dirnames}")
    print(f"File: {filenames}")
    print("-"*50)

