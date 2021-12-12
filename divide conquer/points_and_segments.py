def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    L = 1
    P = 2
    R = 3
    mylist = []
    for i in range(len(starts)):
        mylist.append([starts[i], L])
        mylist.append([ends[i], R])
    for i in range(len(points)):
        mylist.append([points[i], P])
    
    mylist = sorted(mylist, key = lambda x: (x[0], x[1]))
    for i in range(len(points)):
        idx = mylist.index([points[i],P])
        for p in mylist[:idx]:
            if p[1] == L:
                cnt[i]+=1
            elif p[1] == R:
                cnt[i]-=1
    return cnt

n, m = list(map(int, input().split()))
starts = []
ends   = []
for i in range(n):
    s,e = list(map(int, input().split()))
    starts.append(s)
    ends.append(e)
points = list(map(int, input().split()))
#use fast_count_segments
cnt = fast_count_segments(starts, ends, points)
for x in cnt:
    print(x, end=' ')
