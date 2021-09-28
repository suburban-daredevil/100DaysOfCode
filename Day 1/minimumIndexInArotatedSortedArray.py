# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# approach
# find the pivot index in the array
# return arr[(pivot+1)%n] which will be the minimum index in the array


def getPivot(arr):
    # apply modifed Binary Search to get the pivot index

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end-start)//2

        # there are 4 cases here
        # case 1
        if mid < end and arr[mid] > arr[mid+1]:
            return mid
        
        # case 2
        if mid > start and arr[mid] < arr[mid-1]:
            return mid-1

        # case 3 and case 4 for moving the start and end pointers
        if arr[mid] <= arr[start]:
            end = mid - 1
        
        if arr[mid] > arr[start]:
            start = mid + 1

    return -1

def findMin(nums):
    pivot = getPivot(nums)
    n = len(nums)

    # the array has not been rotated
    if pivot == -1:
        pivot == n-1
        
    return nums[(pivot+1)%n]

def main():
    arr = [11,13,15,17]
    print(findMin(arr))

main()