# https://leetcode.com/problems/assign-cookies/

# returns the index of the cieling element in arr
# if ceil is not present, returns -1

def getCeil(arr, x):
    start = 0
    end = len(arr) - 1

    ans = -1

    while start <= end:
        mid = start + (end - start)//2

        if arr[mid] >= x:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return ans

def findContentChildren(g, s):

    count = 0

    # sort s
    s.sort()

    # for each element of g, find the ceil of that element exists or not in s (Binary Search)
    for child in g:
        index = getCeil(s, child)

        if index != -1:
        # If exists, increment count and pop that element from s
            count += 1
            s.pop(index)
    
    return count

def main():
    g = [1,2]
    s = [1,2,3]

    print(findContentChildren(g, s))

main()



