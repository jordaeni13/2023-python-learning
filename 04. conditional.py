#자판기
print("돈을 투입구에 넣어주세요.")
money = int(input())
if money >= 1500:
    print("어떤 음료를 구매하시겠습니까?")
    print("포카리스웨트: 1, 게토레이: 2, 제로콜라: 3")
    needs = int(input())

    if needs == 1:
        print("포카리스웨트를 구매하셨습니다.")
    if needs == 2:
        print("게토레이를 구매하셨습니다.")
    if needs == 3:
        print("제로콜라를 구매하셨습니다.")
else:
    print("돈이 부족합니다.")


print(1 >= 2) #False
print(1 >= 1) #True
print(1 >= 0) #True

print(1 <= 2) #True
print(1 <= 1) #True
print(1 <= 0) #False

print(1 != 2) #True
print(1 != 1) #False

print(1 == 2) #False
print(1 == 1) #True

grade = 85

if grade >= 90:
    print("A")
if 80 <= grade < 90:
    print("B")
if 70 <= grade < 80:
    print("C")
if 60 <= grade < 70:
    print("D")
if grade < 60:
    print("F")

if grade >= 90:
    print("A")
else:
    if grade >= 80:
        print("B")
    else:
        if grade >= 70:
            print("C")
        else:
            if grade >= 60:
                print("D")
            else:
                print("F")

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")