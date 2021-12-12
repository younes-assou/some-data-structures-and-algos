def howSum(target, nbrs, memo={}):
    if target in memo: return memo[target]
    if target == 0:return []
    if target < 0:return None
    
    for nbr in nbrs:
        remainderResult = howSum(target - nbr, nbrs, memo)
        if remainderResult != None:
            memo[target] = [*remainderResult, nbr]
            return memo[target]
    memo[target] = None
    return None
        
target = int(input('enter target number :'))
nbrs = list(map(int, input('enter a list of numbers').split()))

print(howSum(target,nbrs))