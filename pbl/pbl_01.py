# 랜덤 숫자 설정
# 유저: 추측값 입력
# Up/Down
# 정답 맞추면 게임 종료, 숫자 카운트
import random

answer_num = random.randint(1, 100) # Random number 1~100
cnt = 0 # number count

while True:
    user_num = int(input("숫자를 입력하세요: "))
    cnt += 1

    if user_num < answer_num:
        print("정답보다 작은 숫자를 입력하셨습니다. \n")
    elif user_num > answer_num:
        print("정답보다 큰 숫자를 입력하셨습니다. \n")
    else:
        print(f"축하합니다! {cnt}번 만에 정답을 맞추셨습니다.")
        break

