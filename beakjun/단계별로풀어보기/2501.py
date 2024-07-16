
divisor = []

N, K = map(int, input().split())
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        divisor.append(i)
        if i != N//i:
            divisor.append(N//i)
divisor.sort()

print(divisor[K-1] if len(divisor) >= K else 0)