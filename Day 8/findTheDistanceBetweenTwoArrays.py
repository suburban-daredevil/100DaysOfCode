# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

# returns True if we are able to fins an element in the range of [x-d, x+d]
# else returns False
def find(arr, x, d):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start)//2

        if arr[mid] >= x-d and arr[mid] <= x+d:
            return True

        if arr[mid] > x+d:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return False

def findTheDistanceValue(arr1, arr2, d):
    # sort arr2
    arr2.sort()

    result = len(arr1)

    for x in arr1:
        isPresent = find(arr2, x, d)

        if isPresent:
            result -= 1
    
    return result

def main():
    arr1 = [2,1,100,3]
    arr2 = [-5,-2,10,-3,7]
    d = 6

    print(findTheDistanceValue(arr1, arr2, d))

main()

