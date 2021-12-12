import math
def get_change(m, denominations=[1,3,4], memo={}):
    #write your code here
    if m in memo: return memo[m]
    if m<0: return math.inf
    if m==0: return 0
    memo[m] = min(get_change(m-denominations[0])+1,get_change(m-denominations[1])+1,get_change(m-denominations[2])+1)
    return memo[m]
m = int(input())
print(get_change(m))