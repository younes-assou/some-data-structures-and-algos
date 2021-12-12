from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key = lambda i: i[1])
    points = []
    n=len(segments)
    k = 0
    while k<n:
        r=segments[k][1]
        while k<n and segments[k][0]<=r:
            k+=1
        points.append(r)
    return points

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
segments = [Segment(x[0], x[1])for x in data]
points = optimal_points(segments)
print(len(points))
print(*points)