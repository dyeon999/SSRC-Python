'''file_03에서 기능 추가 - txt파일들 내용 출력'''

import os

dir_path = "Day01"
all_files = os.listdir(dir_path)

# 임시로 저장하고 나중에 재사용
txt_files = []

for file in all_files:
    if file.endswith(".txt"): #"()안에 있는걸로 끝나면~" 이라는 조건
        txt_files.append(file)

# # read file
# for filename in txt_files:
#     #file_path = 'Day01/' + filename
#     file_path = os.path.join(dir_path, filename)
#     with open(file_path, 'r', encoding='utf-8') as file:
#         print(f"{filename} : ", file.read())
#         print("*"*30)

'''기능 추가: read lines로 줄 단위 검사
    파일 앞쪽에 # 나 // 로 주석처리 된 것 찾아서 프린트 startswith("#")'''

for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"Content of '{filename}'")
        lines = file.readlines()
        for line in lines:
            if line.startswith("#") or line.startswith("//"): print(line.strip())
        print("-"*50)
