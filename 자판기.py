menu = {"콜라":500, "커피":400, "사이다":300, "율무차":200}
keys = list(menu.keys())
values = list(menu.values())
money = int(input("금액을 넣어주세요: "))

while True:
    print("[이화네 음료수]")
    print("현재금액: %d" %(money))
    for i in range(4):
        print(i+1 , "." , keys[i], "-", values[i], "원" ) 

    pick = int(input("음료를 선택해주세요: "))

    if money - values[pick-1] < 0:
        print("금액이 부족합니다.")
        break
        
    elif money ==  values[pick-1] :
        print("잔액은 0원입니다. 이용해주셔서 감사합니다.")
        break
        
    elif  money > values[pick-1] :
        money = money-values[pick-1]
        print("잔액은 %d 입니다." %(money))

    answer = input("추가로 구매하시겠습니까?(Y/N): ")

    if answer == "N":
        break
