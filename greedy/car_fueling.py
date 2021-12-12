def compute_min_refills(distance, tank, stops):
    road = [0]+stops+[distance]
    nbrRefills = 0
    currentTank = 0
    while currentTank <len(road)-1 :
        lastTank = currentTank
        while currentTank <len(road)-1 and road[currentTank+1]-road[lastTank]<=tank:
            currentTank+=1
        if currentTank==lastTank: return -1

        if currentTank < len(road)-1:
            nbrRefills+=1
    return nbrRefills

d = int(input())
m = int(input())
n = int(input())
stops = list(map(int, input().split()))
print(compute_min_refills(d, m, stops))
