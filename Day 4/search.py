# returns the row and column of the target element, if target is found
# returns -1,-1 if target is not found

def search(mat, target):

    # we keep decrementing the search space until the target is found
    # n represents the maximum column value
    n = len(mat[0])

    # row takes the minimum row value
    row = 0

    # col takes the maximum column value
    col = n - 1

    while row < len(mat) and col >= 0:
        if mat[row][col] == target:
            return row,col

        elif mat[row][col] < target:
            # all the elements to the left of row,col will still be less than target => row will be pointing to the last element of the row
            # so we skip this row
            row += 1
        
        else:
            # all the elements to the bottom of row, col will be greater than target
            # so skip this col
            col += 1
    
    return -1,-1

def main():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    target = 9
    print(search(mat, target))

main()