
while True:
    divisor = []
    N = int(input())
    if N == -1:
        break
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisor.append(i)
            if i != N//i:
                divisor.append(N//i)
    divisor.sort()

    if sum(divisor[:-1]) == N:
        print(f'{N} = {" + ".join(map(str, divisor[:-1]))}')
    else:
        print(f'{N} is NOT perfect.')