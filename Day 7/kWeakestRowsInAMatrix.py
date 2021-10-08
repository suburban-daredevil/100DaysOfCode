# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

def getSoldierCount(arr):
    '''count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            break
    
    return count'''

    # this function can be optimised
    # we can take advantage of the fact that the array is sorted and apply binary search
    # the problem now boils down to finding the leftmost index of zero = count of 1s in the array
    # if the leftmost index of 0 = -1, then return len(nums) => all the elements in the array are 1s

    start = 0
    end = len(arr) - 1

    ans = len(arr)

    while start <= end:
        mid = start + (end-start)//2

        if arr[mid] == 0:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return ans

def myfun(map, x):
    return map[x]

def kWeakestRows(mat, k: int):

    # get all the weakest rows from the matrix
    # sort the row indices based on the number of soldiers and return the first k row indices

    rows = len(mat)
    cols = len(mat[0])

    # map to store the count of number of rows to which the current row is weaker to
    # mapin which key is the row index and the value is the number of rows to which the key row is weaker to
    map = {}

    for i in range(rows):
        soldierCount1 = getSoldierCount(mat[i])
        count = 0
        for j in range(rows):
            if i != j:
                soldierCount2 = getSoldierCount(mat[j])
                
                if soldierCount1 < soldierCount2 or (soldierCount1 == soldierCount2 and i < j):
                    count += 1
        
        map[i] = count

    # myList contains numbers from [1 to row-1]
    myList = [i for i in range(rows)]
    
    # we sort myList based on the value of map[myList[i]] in reverse order
    myList.sort(key=lambda x: myfun(map, x), reverse = True)

    '''swapped = False
    for i in range(rows):
        swapped = False
        for j in range(1, rows - i):
            if map[myList[j-1]] < map[myList[j]]:
                swapped = True
                myList[j], myList[j-1] = myList[j-1], myList[j]
        
        if swapped is False:
            break'''
    
    # result list to return the required number of rows from  myList
    result = []
    for i in range(k):
        result.append(myList[i])
    
    return result

def main():
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    k = 3
    print(kWeakestRows(mat, k))

main()
        
    
                



