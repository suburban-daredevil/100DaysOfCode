# https://leetcode.com/problems/matrix-cells-in-distance-order/

def myFunc(x, rCenter, cCenter):
    dist = abs(x[0] - rCenter) + abs(x[1] - cCenter)
    return dist

def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int):
    # get all the coordinates of the matrix
    mat = []
    for i in range(rows):
        for j in range(cols):
            temp = [i,j]
            mat.append(temp)

    # sort the coordinates based upon the diatance from [rCenter,cCenter]
    mat.sort(key = lambda x : myFunc(x,rCenter, cCenter))
    return mat

def main():
    rows = 2
    cols = 3
    rCenter = 1
    cCenter = 2
    print(allCellsDistOrder(rows, cols, rCenter, cCenter))

main()