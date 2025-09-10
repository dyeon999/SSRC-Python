#while 반복 while True 사용
#메뉴를 선택한다. (여러개의 메뉴를 선택 한다.)
#구매한 메뉴를 리스트로 보관도 해야 한다.
#현금을 넣는다.
#구매한후에 거스름돈을 받는다.
#구매했던 리스트와 총 구매가격? 출력!!!

menus = {"Americano":4000, "Cafe latte":4500, "Cappuccino":5000}

order_list = []
total_price = 0

print("======== MENU ========")

for menu, price in menus.items():
    print(f"{menu} : {price}won")
print()

while True:
    selected_menu = input("Enter the Menu : ")
    price = menus.get(selected_menu,0)

    if price != 0:
        order_list.append(selected_menu)
        total_price += price
    elif selected_menu == "":
        break
    else:
        print("No Menu.")

money = int(input("\nEnter the money : "))
change = money - total_price

if change >= 0:
    print(f"You've chosen {order_list}. Change is {change} Won")
else:
    print("Not enough money.")