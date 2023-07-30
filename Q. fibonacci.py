a = [1, 1]
while len(a)<=50:
    a.append(a[-1]+a[-2])

print(a[-1])