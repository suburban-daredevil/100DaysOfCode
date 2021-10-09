# https://leetcode.com/problems/kth-missing-positive-number/

# calculate the set difference of (1,2,3...n-1) to set(arr)
# sort the result
# return result[k-1]

def findKthPositive(arr, k):

    # myset contains the numbers from 1 to max(arr)
    myset = set()
    for i in range(1,max(arr)+1):
        myset.add(i)
    
    # result contains the elements in myset but not in arr
    # result essentially conatains the missing numbers upto the max(arr)
    result = list(myset - set(arr))

    if len(result) >= k: # if result contains the required kth missing number, return result[k-1]
        result.sort() # order might have changed since we have used a hashset 
        return result[k-1]
    else: # if result does not contain the required k, kth missing number greater than the max(arr)
        return max(arr) + k - len(result)

def search(arr, x):
    start = 0
    end = len(arr)

    while start <= end:
        mid = start + (end-start) // 2

        if arr[mid] == x:
            return True

        elif x > arr[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return False
        
# approach using binary search
def findKthPositive1(arr, k):

    count = 0    
    for i in range(1, max(arr)+1):
        isPresent = search(arr, i)
        if not(isPresent):
            count += 1
        if count == k:
            return i
    
    return max(arr) + k - count

def main():
    arr = [1,2,3,4]
    k = 2
    result = findKthPositive1(arr, k)
    print(result)

main()