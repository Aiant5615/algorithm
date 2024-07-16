l = sorted(list(map(int, input().split())))

l1 = l[0] + l[1]

if l1 <= l[2]:
    print(l1*2-1)
else:
    print(l1+l[2])