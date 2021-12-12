def get_majority_element(a, left, right):
    a.sort()
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = left + (right-left)//2
    k=0
    for i in range(len(a)):
        if a[i]==a[mid]: k+=1

    if k > right/2 : return k

    return -1


n = int(input())
a = list(map(int, input().split()))
if get_majority_element(a, 0, n) != -1:
    print(1)
else:
    print(0)
