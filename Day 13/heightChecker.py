# https://leetcode.com/problems/height-checker/

def heightChecker(heights):
    # make a copy of the original array
    arr = heights.copy()

    # sort the copy
    arr.sort()

    count = 0

    # compare the sorted array and the original array and count the number of mismatched elements
    for i in range(len(arr)):
        if arr[i] != heights[i]:
            count += 1
    
    return count

def main():
    heights = [5,1,2,3,4]
    print(heightChecker(heights))

main()
