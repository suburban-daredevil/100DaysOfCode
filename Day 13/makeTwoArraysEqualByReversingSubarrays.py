# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

def search(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end-start)//2

        if arr[mid] == x:
            return True
        
        elif x > arr[mid]:
            start = mid + 1

        else:
            end = mid - 1
    
    return False

def canBeEqual(target, arr):
    # if we can find an element of target not in arr, return False
    # else return True
    arr.sort()

    for x in target:
        if not(search(arr, x)):
            return False

    return True

def main():
    target = [1,2,3,4]
    arr = [2,4,1,3]
    print(canBeEqual(target, arr))

main()