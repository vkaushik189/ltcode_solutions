def minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]):

    steps = 0
    x1,y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        steps += max(abs(x2-x1),abs(y2-y1))
        x1,y1 = x2,y2
    return steps

ans = minTimeToVisitAllPoints()
print(ans)