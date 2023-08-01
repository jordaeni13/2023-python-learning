def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input())
result = factorial(num)
print(f"The factorial of {num} is: {result}")

def circle(r):
    return r*r*3.14

radius = int(input())
print(circle(radius))

def addition(a, b):
    return a+b

add_list = [3, 9]
print(addition(*add_list)) #리스트를 unpack해서 함수에 넣음

def many_addition(*args): #인수의 개수가 정해지지 않음
    sum = 0
    for arg in args:
        sum+=arg
    return sum

print(many_addition(1,3,5,7,9))


def factorial_recursion(n):
    if n == 1:
        return 1 #만약 이 return이 작동되면 남은 코드는 무시되고 현재 호출된 함수가 종료된다.
    return n*factorial_recursion(n-1)

print(factorial_recursion(int(input())))