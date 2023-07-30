print("Hello World") #첫번째 출력
print("Hello World") #두번째 출력
print("Hello World") #세번째 출력
#... (생략)
print("Hello World") #아흔여덟번째 출력
print("Hello World") #아흔아홉번째 출력
print("Hello World") #백번째 출력

i = 1
while i<=100:
    print("Hello World")
    i+=1

i=1
while i<=100:
    print(i, "Hello World")
    i+=1

i=1
if i<=100: #i=1
    print(i, "Hello World")
    i+=1
if i<=100: #i=2
    print(i, "Hello World")
    i+=1
#...(생략)
if i<=100: #i=100
    print(i, "Hello World")
    i+=1
#...(생략)

import time

timer = 5

while timer > 0:
    print(timer)
    time.sleep(1)
    timer -= 1

print("Go!")
