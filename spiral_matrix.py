matrix = [[1,2,3],[4,5,6],[7,8,9]]


def spiral_order(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())

        if matrix:
            res += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))

    return res


print(spiral_order(matrix))




