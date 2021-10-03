# https://leetcode.com/problems/search-a-2d-matrix/

# consider a strictly sorted matrix and target element, find whether the target element exists in the array or not

# takes matrix, row in the matix in which we should search for the target
# start column and end column within which we should search for the target
# and also the target

# search in the row provided and between the columns provided

def binarySearch(mat, row, colStart, colEnd, target):
    while colStart <= colEnd:
        mid = colStart + (colEnd-colStart)//2

        if mat[row][mid] == target:
            return [row, mid]

        elif mat[row][mid] < target:
            colStart = mid + 1
        
        else:
            colEnd = mid - 1

    return [-1,-1]


def search(mat, target):
    rows = len(mat)
    cols = len(mat[0])

    if rows == 0 and cols == 0:
        # matrix is empty:
        return [-1, -1]

    if rows == 1:
        return binarySearch(mat, 0, 0, cols-1, target)
    
    # take the middle colums and perform BS on the middle column
    cMid = cols//2

    # we are eleminating rows
    rStart = 0
    rEnd = rows - 1

    # run loop till number of rows > 2
    while rStart < (rEnd-1): # while this is true, matrix will have more than 2 rows
        mid = rStart + (rEnd-rStart)//2

        if mat[mid][cMid] == target:
            return [mid, cMid]

        elif mat[mid][cMid] < target:
            rStart = mid
        
        else:
            rEnd = mid
    
    # after this only 2 rows are remainging
    # they are rStart and rStart+1 => from exiting while loop

    if mat[rStart][cMid] == target:
        return [rStart, cMid]

    if mat[rStart + 1][cMid] == target:
        return [rStart + 1, cMid]

    # search in 1 segment
    if cMid - 1 >= 0 and target <= mat[rStart][cMid-1]:
        return binarySearch(mat, rStart, 0, cMid - 1, target)

    # search in 2 segment
    if cMid + 1 >= 0 and cMid + 1 < cols and target >= mat[rStart][cMid + 1] and target <= mat[rStart][cols - 1]:
        return binarySearch(mat, rStart, cMid + 1, cols - 1, target)

    # search in 3 segment
    if cMid - 1 >= 0 and target <= mat[rStart + 1][cMid - 1]:
        return binarySearch(mat, rStart + 1, 0, cMid - 1, target)

    # search in 4 segment
    return binarySearch(mat, rStart + 1, cMid + 1, cols - 1, target)

def main():
    arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(search(arr, target))

main()







