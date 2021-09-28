# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Approach
# find the pivot index
# check if element at pivot index is equal to target => return True
# apply BS from (start, pivot-1)
# apply BS from (pivot+1, end)


# return the pivot index of an rotated sorted array with duplicate elements
def getPivot(arr):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end-start)//2
        # 4 cases over here

        # case 1
        # element at mid > element at mid+1 => obvious
        # this is our answer => we have found out the pivot
        if mid < end and arr[mid] > arr[mid+1]:
            return mid

        # case 2
        # element at mid is < element at mid-1
        # then our answer is element at mid-1 => pivot
        if mid > start and arr[mid] < arr[mid-1]:
            return mid-1

        if arr[mid] == arr[start] and arr[mid] == arr[end]:
            # we can ignore start and end in this case
            # if they are not pivots

            if start < end and arr[start] > arr[start + 1]:
                return start
            
            start += 1

            if end > start and arr[end] < arr[end-1]:
                return end-1

            end -= 1
        
        # left side is sorted, so pivot should be in the right
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1  
        else:
            end = mid - 1
    
    # pivot not found
    return -1

def binarySearch(arr, target, start, end):

    while start <= end:
        mid = start + (end-start)//2

        if arr[mid] == target:
            return True

        elif target > arr[mid]:
            start = mid + 1
        
        else:
            end = mid - 1
    
    return False
    
def search(nums, target):

    n = len(nums)

    if n == 0:
        return False
    
    if n == 1:
        if nums[0] == target:
            return True
        return False

    # get the pivot index
    pivot = getPivot(nums)

    # if the array is not rotated
    if pivot == -1:
        return binarySearch(nums, target, 0, n-1)

    # if element at pivot index == target, return True
    if nums[pivot] == target:
        return True
    
    # search for the target in the range of (0, pivot-1)
    firstTry = binarySearch(nums, target, 0, pivot-1)

    # if target is present return True
    if firstTry:
        return firstTry
    
    # if target is not present in the left side of pivot, search for target in the right side of pivot
    secondTry = binarySearch(nums, target, pivot+1, n-1)
    return secondTry

def main():
    arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    target = 2

    print(search(arr, target))

main()