def minimum_time(points):
    res = 0
    x1, y1 = points.pop()
    # y1 = points.pop()
    print(x1, y1)
    while points:
        x2, y2 = points.pop()
        print(x2,y2)
        res += max(abs(y2-y1), abs(x2-x1))
        x1, y1 = x2, y2
    return res

points = [[1,1],[3,4],[-1,0]]
print(minimum_time(points))