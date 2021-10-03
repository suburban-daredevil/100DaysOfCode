# https://leetcode.com/problems/find-a-peak-element-ii/


def checkPeakElement(arr, i, j):
    rows = len(arr)
    cols = len(arr[0])

    # element is in intersection of first row and first col
    if i == 0 and j == 0:
        if arr[i][j] > arr[i][j+1] and arr[i][j] > arr[i+1][j]:
            return True

    # element is in intersection of first row and last column
    if i == 0 and j == cols-1:
        if arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i+1][j]:
            return True

    # element is in intersection of last row and first column
    if i == rows-1 and j == 0:
        if arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i][j+1]:
            return True

    # element is in intersection of last row and last column
    if i == rows-1 and j == cols-1:
        if arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i-1][j]:
            return True

    # element is in first row
    if i == 0:
        if arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j+1]:
            return True

    # element is in first column
    if j == 0:
        if arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i][j+1] and arr[i][j] > arr[i+1][j]:
            return True

    # element is in last row
    if i == rows - 1:
        if arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i-1][j] and arr[i][j+1]:
            return True

    # element is in last column
    if j == cols - 1:
        if (arr[i][j] > arr[i][j-1]) and (arr[i][j] > arr[i-1][j]) and (arr[i][j] > arr[i+1][j]):
            return True

    # general case
    # element is somewhere in the middle of the array
    if i+1<rows and i-1>=0 and j+1<=cols and j-1>=0:
        if arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i][j+1]:
            return True

    return False

def findPeakGrid(mat):
    # for each row in the matrix, find the peak element, since the row is a mountain array
    # check if that peak element is stricly greater than its neighbours
    # return ans

    rows = len(mat)
    cols = len(mat[0])

    result = [-1,-1]
    for i in range(rows):
        for j in range(cols):
            # print(mat[i][j])
            if checkPeakElement(mat, i, j):
                result = [i, j]
                break
    return result
        

arr = [[72,85,92,63,20,25,38,28,8,75,95,70,8,96,41,8,7,75,62,65,68,21,8,66,11],[24,9,77,9,87,31,52,16,73,32,75,77,6,80,11,54,85,73,67,41,34,27,86,92,41],[31,34,51,17,86,83,39,59,41,97,10,2,59,73,13,10,69,28,65,34,17,45,9,32,48],[37,21,57,70,91,39,79,84,68,2,86,71,39,85,14,18,34,15,14,96,71,20,35,37,78],[27,92,44,27,88,82,34,65,63,33,7,12,82,55,36,6,1,43,99,17,82,34,21,95,57],[71,91,55,72,2,15,10,89,20,70,5,48,75,71,19,56,17,6,40,47,6,46,27,88,32],[86,14,46,100,72,53,80,96,31,21,23,53,4,23,95,43,53,86,95,32,35,21,90,14,49],[5,61,29,26,59,45,40,30,29,4,85,25,52,43,36,9,99,36,45,83,66,52,87,69,43],[4,15,34,23,75,34,5,14,77,56,45,94,41,56,78,66,15,50,74,25,33,6,91,56,1],[67,69,88,93,95,86,26,47,56,9,86,43,80,41,85,16,93,39,65,40,86,53,42,52,90],[38,71,17,25,54,49,87,96,23,79,73,39,52,71,1,39,37,27,56,75,78,84,60,57,87],[28,66,61,95,22,85,11,37,66,85,82,80,43,12,97,31,87,40,29,26,19,4,6,32,61],[79,99,10,59,54,81,74,25,92,90,50,64,52,32,19,84,89,1,97,99,14,100,55,29,23],[90,67,60,7,72,32,16,59,18,60,86,68,72,77,41,97,57,79,93,65,55,71,58,21,96],[61,58,34,97,32,82,36,99,100,67,63,81,31,36,57,10,92,37,31,35,43,41,70,11,18],[20,30,50,89,20,91,28,9,54,53,43,70,60,54,8,27,54,50,99,75,90,3,98,74,49],[62,1,46,39,97,50,54,69,96,95,70,78,29,63,29,35,56,63,4,50,44,86,87,52,93],[22,60,17,80,69,4,51,76,73,85,4,11,83,55,18,60,24,7,34,49,42,28,59,42,44],[98,49,36,97,54,33,11,61,3,96,70,7,45,29,84,9,100,84,6,97,4,32,26,3,80],[20,31,17,61,86,15,73,28,60,90,33,99,48,22,78,96,92,15,100,21,40,14,75,4,40],[74,87,49,51,92,26,10,76,89,81,32,14,90,99,39,88,77,16,73,6,45,69,55,85,48],[9,65,83,44,2,54,63,14,56,47,82,59,91,20,56,23,94,67,84,35,79,100,62,60,56],[94,76,35,42,32,12,36,58,32,97,60,73,79,86,49,44,4,64,42,24,63,28,46,34,44],[36,77,90,36,72,2,67,25,11,31,93,53,63,72,98,31,89,61,83,92,58,3,12,38,29]]
print(findPeakGrid(arr))