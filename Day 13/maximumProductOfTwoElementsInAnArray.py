# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

def maxProduct(nums):
    # sort the array
    # find the maximum of product of first 2 numbers and last 2 numbers

    nums.sort()

    result1 = (nums[-1]-1)*(nums[-2]-1)
    result2 = (nums[0]-1)*(nums[1]-1)

    result = max(result1, result2)
    return result

def main():
    nums = [3,7]
    print(maxProduct(nums))

main()