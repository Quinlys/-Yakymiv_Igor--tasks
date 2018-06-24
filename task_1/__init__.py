# -*- coding: utf-8 -*-
def fill_spiral_matrix(n):
    result = []
    x, y, dx, dy = 0, 0, 1, 0
    arr = [[0] * n for i in range(n)]
    for i in range(1, n**2+1):
        arr[x][y] = i
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x+dx, y+dy
    for x in list(zip(*arr)):
        result.append(list(x))
    return result

