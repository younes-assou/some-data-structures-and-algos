def binary_search(keys, query):
    # write your code here
    l = 0
    r = len(keys)-1
    result = -1
    while l<=r :
        m = l + (r-l)//2
        if keys[m] == query:
            result = m
            r = m-1
        elif query <= keys[m]:
            r = m-1
        elif query > keys[m]:
            l = m+1
    return result    

n = int(input())
input_keys = list(map(int, input().split()))
assert len(input_keys) == n
k = int(input())
input_queries = list(map(int, input().split()))
assert len(input_queries) == k

for q in input_queries:
    print(binary_search(input_keys, q), end=' ')