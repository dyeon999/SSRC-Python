from faker import Faker

fake = Faker("ko_KR") # 한국어 어쩌구...

for _ in range(20): # 그냥 20번 반복한다는 뜻. 보통 i같은걸 쓰고 i를 for안에서 사용했는데 지금은 i를 안쓴다 이거지.
    print(fake.name())
    print(fake.address())
    print(fake.email())
    print(fake.phone_number())
    print("-------------------------------")