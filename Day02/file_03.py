"""
디렉터리 안에 특정 확장자를 가진 파일만 가져오기
"""

import os

dir_path = "Day01"
all_files = os.listdir(dir_path)

# 임시로 저장하고 나중에 재사용
txt_files = []

for file in all_files:
    if file.endswith(".txt"): #"()안에 있는걸로 끝나면~" 이라는 조건
        txt_files.append(file)

print(txt_files)
