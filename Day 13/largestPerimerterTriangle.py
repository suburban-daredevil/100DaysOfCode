# https://leetcode.com/problems/largest-perimeter-triangle/

def isValidTriangle(a, b, c):
    if a+b > c and b+c > a and c+a > b:
        return True
    return False

def largestPerimeter(nums):
    # sort the array
    # keep selecting the last three elements of the array, such that it forms a valid triangle

    nums.sort()

    result = 0

    for i in range(len(nums)-1, 0, -1):
        if i >= 2 and isValidTriangle(nums[i], nums[i-1], nums[i-2]):
            result = nums[i] + nums[i-1] + nums[i-2]
            return result
    
    return result
    
def main():
    nums = [3,6,2,3]
    print(largestPerimeter(nums))

main()