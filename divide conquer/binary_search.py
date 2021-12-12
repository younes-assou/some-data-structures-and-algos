def binary_search(keys, query, l, r):
    # write your code here
    if r<l :
        return -1
    
    m = l + (r-l)//2
    if keys[m]==query:
        return m
    elif keys[m]<query:
        return binary_search(keys,query, m+1, r)
    elif keys[m]>query:
        return binary_search(keys,query, l, m-1)

n = int(input())
input_keys = list(map(int, input().split()))
assert len(input_keys) == n
k = int(input())
input_queries = list(map(int, input().split()))
assert len(input_queries) == k

for q in input_queries:
    print(binary_search(input_keys, q, 0, n-1), end=' ')