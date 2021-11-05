# https://leetcode.com/problems/array-partition-i/

def arrayPairSum(nums):

    # sort the array
    # keep selecting elements in pairs from the beginning of the array
    # find their minimum, add it to total
    
    nums.sort()

    total = 0

    for i in range(0, len(nums), 2):
        total += min(nums[i],nums[i+1])

    return total

def main():
    nums = [1,4,3,2]
    print(arrayPairSum(nums))

main()