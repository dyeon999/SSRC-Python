import os
import time

dir_path = "Day01"
pre_file = set(os.listdir(dir_path))
print(f"prefile {pre_file}")
#pre_file = 탐지를 하기 전에 파일 목록 저장

while True:
    current_file = set(os.listdir(dir_path))
    result_diff = current_file - pre_file
    print(f"CURRENT FILES : {current_file}")
    print()
    print(f"NEW FILE : {result_diff}")
    print("="*50)

    pre_file = current_file
    time.sleep(2)