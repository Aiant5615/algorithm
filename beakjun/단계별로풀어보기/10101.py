a = []

for _ in range(3):
    a.append(int(input()))
a.sort()

if a[0] + a[1] + a[2] != 180:    
    print('Error')
elif a[0] == a[1] == a[2]:
    print('Equilateral')
elif a[0] == a[1] or a[1] == a[2]:
    print('Isosceles')
else:
    print('Scalene')
