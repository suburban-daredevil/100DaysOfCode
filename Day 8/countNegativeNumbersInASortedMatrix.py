# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

def getFirstOccurence(arr):
    # arr is sorted in reverse order
    # returns the index of first occurence of a negative number

    ans = -1
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end-start) // 2

        if arr[mid] < 0:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return ans

def getLastOccurence(arr):
    # arr is sorted in reverse order
    # returns the index of last occurence of a negative number

    ans = -1
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end-start) // 2

        if arr[mid] < 0:
            ans = mid
            start = mid + 1
        else:
            start = mid + 1
    
    return ans

def countNegatives(grid):
    # for each row find the number of negatives
    # number of negatives in a row = (index of last occurence of a negative) - (index of first occurence of a negtive) + 1

    rows = len(grid)
    count = 0

    for i in range(rows):
        left = getFirstOccurence(grid[i])

        if left != -1:
            right = getLastOccurence(grid[i])            
            count += (right - left) + 1

    return count

def main():
    grid = [[-1]]
    print(countNegatives(grid))

main()