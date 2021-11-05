# https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(nums):
    arr = []
    for i in nums:
        arr.append(i**2)

    arr.sort()
    return arr

def main():
    nums = [-7,-3,2,3,11]
    print(sortedSquares(nums))

main()
        