def bestSum(target, nbrs, memo={}):
    if target in memo: return memo[target]
    if target == 0:return []
    if target < 0:return None

    shortest = None
    
    for i in range(len(nbrs)):
        remainderCombination = bestSum(target - nbrs[i], nbrs[i+1:], memo)
        if remainderCombination != None:
            combination = [*remainderCombination, nbrs[i]]
            if shortest == None:
                shortest = combination
            elif len(combination)<len(shortest):
                shortest = combination

    memo[target] = shortest
    return shortest

def partition3(A):
    v = sum(A)
    if v%3 != 0:return 0
    s = bestSum(v//3,A)
    if s==None: return 0
    else:
        A = list(set(A).difference(set(s)))
        s = bestSum(v//3,A)
        if s==None: return 0

    return 1

n = int(input())
A = list(map(int, input().split()))
print(partition3(A))

