def minTimeToVisitAllPoints(points):
    cost = 0
    
    i = 0
    n = len(points) - 1
    while i < n:
        dx = abs(points[i][0] - points[i+1][0])
        dy = abs(points[i][1] - points[i+1][1])
        
        cost += max(dx, dy)
        i += 1
        
    return cost

points = [[1,1],[3,4],[-1,0]]
print(minTimeToVisitAllPoints(points))