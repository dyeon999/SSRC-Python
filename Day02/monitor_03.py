import os
import time
from datetime import datetime

dir_path = "Day01"
pre_file = set(os.listdir(dir_path))
# print(f"prefile {pre_file}")
#pre_file = 탐지를 하기 전에 파일 목록 저장

while True:
    # 날짜 체크
    now = datetime.now()
    day = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")


    current_file = set(os.listdir(dir_path))
    result_diff = current_file - pre_file
    # print(f"CURRENT FILES : {current_file}")
    # print()
    print(f"NEW FILE : {result_diff}")
    print("="*50)

    # txt file of detected files in "Day01" dir.

    for file_name in result_diff:
        with open (f'Day02/{day}_detection_report.txt', 'a', encoding='utf-8') as file: # "a"는 add로 파일 안에 추가하는것. w는 새로 덮어쓰기
            file.write(f"REPORTER: Doyeon Kim \n")
            file.write('CONTENTS: New file has detected.\n')
            file.write(f'{hour} {file_name} \n')
            file.write("="*50 + "\n")

    pre_file = current_file
    time.sleep(2)