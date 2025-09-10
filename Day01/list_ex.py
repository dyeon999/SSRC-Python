# 아래는 5명의 학생들의 성적을 입력 받아서
# 최고값, 최소값, 평균값, 90점 이상의 count 프로그램
# 5명의 학생들의 성적을 입력 -> list [] 에 저장

STUDENTS = 5
lst = []
cnt = 0

for i in range(STUDENTS):
    value = int(input(f"{i+1}번째 학생의 성적을 입력하세요 : "))
    lst.append(value)

print(f"\nList = {lst}")
print()

print(f"Highest Score : {max(lst)}")
print(f"Lowest Score : {min(lst)}")
print(f"Average : {sum(lst)/len(lst)}")

for score in lst:
    if score >= 90:
        cnt += 1

print(f"{cnt} students' score has over 90")