#커피 주문 프로그램
#메뉴 선택하고 -> 돈을 입력하면 -> 거스름돈 계산
menus = {"Americano":4000, "Cafe latte":4500, "Cappuccino":5000}

print("======== MENU ========")

for menu, price in menus.items():
    print(f"{menu} : {price}won")

# Get Menu & Price
selected_menu = input("\nEnter the Menu : ")
money = int(input("Enter the money : "))

price = menus.get(selected_menu,0)

# Print the Result
if price == 0:
    print("No menu Selected")
else:
    change = money - price
    if change >= 0:
        print(f"You've chosen {selected_menu}. Change is {change} Won")
    else:
        print("Not enough money.")