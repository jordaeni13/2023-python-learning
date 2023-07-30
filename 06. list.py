stu1 = input()
stu2 = input()
stu3 = input()
#stu1, stu2, stu3 = input().split()와 같이 작성해도 괜찮다.

average_grade = (int(stu1) + int(stu2) + int(stu3)) / 3


import statistics

a = []
i = 1

while i<=100:
    a.append(int(input()))
    i+=1

n = len(a)
print("Mean: ", sum(a)/n)
print("Median: ", a[(n+1)//2] if n%2==1 else (a[n//2]+a[n//2 + 1])/2)
print("Mode: ", statistics.mode(a))

prime_10 = [2, 3, 5, 7]

print(prime_10[0])
print(prime_10[1])
print(prime_10[2])
print(prime_10[3])

example = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

example[1] = 100 #리스트 내 원소는 변수와 비슷한 관점으로 봐도 좋다.
print(example)

last_element = example[-1] #인덱스의 마지막은 -1로도 접근이 가능하다.
print(last_element)

del example[2] #del을 통해 원소를 삭제할 수 있다.
print(example)


example = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

partial_ex1 = example[3:] #[3:]는 3번째 원소를 포함한 이후의 모든 원소를 지칭한다.
print(partial_ex1)

partial_ex2 = example[:7] #[:7]는 7번째 원소를 포함하지 않는 이전의 모든 원소들을 지칭한다.
print(partial_ex2)

partial_ex3 = example[3:7] #[3:7]는 인덱스가 3 이상이고 7 미만인 모든 원소들을 지칭한다.
print(partial_ex3)


grade = [68, 86, 48, 27, 39]
grade.sort(reverse=True)
print(grade)