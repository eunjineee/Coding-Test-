n = int(input())
a = [0,0,0]
num = 0
while a != [n,0,0]:
    if a[2] != 59:
        a[2] += 1
    else:
        a[2] = 0
        if a[1] != 59:
            a[1] += 1
        else:
            a[1] = 0
            a[0] += 1
    if '3' in str(a[0]) + str(a[1]) + str(a[2]):
        num += 1
        print(a)
print(num)