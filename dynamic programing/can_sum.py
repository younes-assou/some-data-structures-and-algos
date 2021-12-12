def canSum(target, nbrs, memo={}):
    if target in memo: return memo[target]
    if target == 0:return True
    if target < 0:return False
    
    for nbr in nbrs:
        if canSum(target - nbr, nbrs, memo):
            memo[target] = True
            return True
        
    return False

target = int(input('enter target number :'))
nbrs = list(map(int, input('enter a list of numbers').split()))

print(canSum(target,nbrs))