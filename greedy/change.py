def get_change(m):
    coins = [10,5,1]
    current = m
    n=0
    for i in range(3):
        n+=current//coins[i]
        current = current%coins[i]
    return n

m = int(input())
print(get_change(m))