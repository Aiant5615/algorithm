

N = int(input())
w = []
l = []
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    l.append(b)


W = max(w) - min(w)
L = max(l) - min(l)
print(W*L)
