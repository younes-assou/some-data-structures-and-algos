def bestSum(target, nbrs, memo={}):
    if target in memo: return memo[target]
    if target == 0:return []
    if target < 0:return None

    shortest = None
    
    for nbr in nbrs:
        remainderCombination = bestSum(target - nbr, nbrs, memo)
        if remainderCombination != None:
            combination = [*remainderCombination, nbr]
            if shortest == None:
                shortest = combination
            elif len(combination)<len(shortest):
                shortest = combination

    memo[target] = shortest
    return shortest
        
target = int(input('enter target number :'))
nbrs = list(map(int, input('enter a list of numbers :').split()))

print(bestSum(target,nbrs))