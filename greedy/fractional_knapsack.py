def get_optimal_value(capacity, weights, values):
    value = 0.
    W = capacity
    fract = [v/w for v,w in zip(values,weights)]

    for j in range(n):
        if W==0: return value
        i = fract.index(max(fract))
        a = min(weights[i],W)
        value+=a*fract[i]
        weights[i]-=a
        W-=a
        fract[i] = 0
    return value

n, capacity = map(int, input().split())
values = []
weights = []
for _ in range(n):
    v,w = map(int, input().split())
    values.append(v)
    weights.append(w)
opt_value = get_optimal_value(capacity, weights, values)
print("{:.5f}".format(opt_value))