prime_10 = [2, 3, 5, 7]
example_str = "Hello World"

print(sum(prime_10)) #리스트의 원소 합 출력
print(len(prime_10)) #리스트의 크기 출력
print(list(reversed(prime_10))) #내림차순 정렬

print(len(example_str)) #문자열의 크기 출력
print(list((sorted(example_str)))) #Ascii code 기준 오름차순으로 정렬.

iter_prime_10 = iter(prime_10)
print(iter_prime_10.__next__())
print(iter_prime_10.__next__())
print(iter_prime_10.__next__())
print(iter_prime_10.__next__())
#print(iter_prime_10.__next__())


prime_10 = [2, 3, 5, 7]

try:
    iter_prime_10 = iter(prime_10)
    print(iter_prime_10.__next__())
    print(iter_prime_10.__next__())
    print(iter_prime_10.__next__())
    print(iter_prime_10.__next__())
    #print(iter_prime_10.__next__())
    print("flag")
except StopIteration:
    print("StopIteration error occurred")

example_sequence = [53, 27, 38, 10, 85, 96, 44]
i = 1
while i <= len(example_sequence):
    print(example_sequence[i-1])
    i += 1

example_sequence = [53, 27, 38, 10, 85, 96, 44]
try:
    iter_sequence = iter(example_sequence)
    while True:
        i = iter_sequence.__next__()
        print(i)
except StopIteration:
    pass

example_range = range(0,10) #0부터 9까지 정수
sum = 0
try:
    iter_range = iter(example_range)
    while True:
        i = iter_sequence.__next__()
        sum += i
except StopIteration:
    pass

print(sum)


example_sequence = [53, 27, 38, 10, 85, 96, 44]
for i in example_sequence: #이 과정에서 example_sequence의 iterator가 생성됨
    print(i)

example_range = range(0,10) #0부터 9까지 정수
sum = 0
for i in example_range: #example_range 대신 range(0,10)을 바로 넣어도 좋다.
    sum += i
print(sum)


#list comprehension
