# https://leetcode.com/problems/check-if-n-and-its-double-exist/


def search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end-start)//2

        if arr[mid] == target:
            return True

        elif target > arr[mid]:
            start = mid + 1
        
        else:
            end = mid - 1

    return False

def getLeftMostIndex(arr, target):
    start = 0
    end = len(arr) - 1

    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            result = mid
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid -1

    return result

def getRightMostIndex(arr, target):
    start = 0
    end = len(arr) - 1

    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            result = mid
            start = mid + 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
            
    return result

def checkIfExist(arr):
    # sort the array
    # for every element of the array, check if twice the element is available in the array or not
    # for checking we could use Binary Search

    arr.sort()

    for x in arr:
        if x != 0:
            isPresent = search(arr, 2*x)
            if isPresent:
                return True
        else:
            left = getLeftMostIndex(arr, 0)
            right = getRightMostIndex(arr, 0)

            if left != right:
                return True        

    return False

# using a hashmap to check if the element exists or not
def checkIfExist1(arr):
    map = {}

    for i in range(len(arr)):
        map[arr[i]] = i
    
    for i in map:
        if i != 0:
            if 2*i in map:
                return True
        else:
            # if i == 0, then search the array if another zero exists or not
            # if exists return True
            for x in range(len(arr)):
                if arr[x] == 0 and x != map[i]:
                    return True

    return False


def main():
    arr = [0,0]
    print(checkIfExist1(arr))

main()