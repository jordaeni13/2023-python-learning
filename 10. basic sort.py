##Bubble Sort
input_list = input().split()
for i in range(len(input_list)): #0부터 n-1까지
    input_list[i] = int(input_list[i])

for i in range(len(input_list) - 1): #n-1회 반복
    for j in range(len(input_list) - i - 1): #n-i-1회 반복
        if input_list[j]>input_list[j+1]:
            input_list[j], input_list[j+1] = input_list [j+1], input_list[j]
    #print(input_list) #주석 제거를 통해 정렬 과정 관찰

print(input_list)

##Selection Sort
input_list = list(map(int, input().split())) #정수형

for i in range(len(input_list) - 1):
    min, min_index = input_list[-1], -1 #변수 초기화
    for j in range(i, len(input_list)):
        if input_list[j] < min:
            min, min_index = input_list[j], j

    input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

print(input_list)

##Insertion sort
input_list = list(map(int,input().split()))

for i in range(1, len(input_list)): #정렬 범위 설정, 1 ~ n-1
    for j in reversed(range(0, i)): #정렬된 리스트에 적절하게 삽입하기. j = i-1 ~ 0
        if input_list[j]>input_list[j + 1]:
            input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

print(input_list)