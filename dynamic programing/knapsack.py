def optimal_weight(W, w):
    # write your code here
    V = [[0 for _ in range(len(w)+1)] for _ in range(W+1)]

    for i in range(1,len(w)+1):
        for wei in range(1,W+1):
            V[wei][i] = V[wei][i-1]
            if w[i-1]<=wei:
                v = V[wei-w[i-1]][i-1]+w[i-1]
                if V[wei][i]<v:
                    V[wei][i] = v
    return V[W][-1]

W, n = list(map(int, input().split()))
w = list(map(int, input().split()))
print(optimal_weight(W, w))
