my_list = []

my_list = [10, 20, 30, 40, 50]
my_list.append(6) # add "6" at the end of my_list
print(my_list)

my_list.insert(1, 9)  # insert"9" at index 1
print(my_list)

my_list.remove(20)  #데이터를 날린다.
print(my_list)

del my_list[0]  # 첫 번째 인덱스 기준 요소 삭제
print(my_list)