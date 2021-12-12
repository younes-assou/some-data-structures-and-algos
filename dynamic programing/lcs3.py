def lcs3(a, b, c):
    #write your code here
    return min(len(a), len(b), len(c))

n = input()
a = list(map(int, input().split()))
m = input()
b = list(map(int, input().split()))
p = input()
c = list(map(int, input().split()))

print(lcs3(a, b, c))
