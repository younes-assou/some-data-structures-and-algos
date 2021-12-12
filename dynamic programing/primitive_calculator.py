def optimal_sequence(n):
    T = [0]*(n+1)
    T[1] = [1]
    for i in range(2,n+1):
        if i % 3 == 0:
            s = [*T[i//3], i]
            if T[i] == 0:
                T[i] = s
            elif len(s)<len(T[i]):
                T[i] = s
        if i % 2 == 0:
            s = [*T[i//2], i]
            if T[i] == 0:
                T[i] = s
            elif len(s)<len(T[i]):
                T[i] = s
        s = [*T[i-1], i]
        if T[i] == 0:
            T[i] = s
        elif len(s)<len(T[i]):
            T[i] = s

    return T[n]

n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
print(*sequence)
