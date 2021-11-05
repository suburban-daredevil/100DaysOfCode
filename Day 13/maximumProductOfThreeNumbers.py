# https://leetcode.com/problems/maximum-product-of-three-numbers/

def maximumProduct(nums):
    # sort the list
    nums.sort()

    # find the product of the last 3 numbers
    result1 = nums[-1]*nums[-2]*nums[-3]

    # find the product of first 2 and last 1 number
    result2 = nums[0]*nums[1]*nums[-1]

    # return max from the above steps
    result = max(result1, result2)

    return result

def main():
    nums = [-100,-98,-1,2,3,4]
    print(maximumProduct(nums))

main()
