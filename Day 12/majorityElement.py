# https://leetcode.com/problems/majority-element/

import math

# returns the frequency of the ith element
def getFreq(nums, i):
    # checks and maintains a count as to how many elements are similar to ith element

    x = nums[i]

    count = 1

    i += 1

    while i < len(nums):
        if nums[i] == x:
            count += 1
            i += 1
        else:
            break
            
    return count

# TLE
def majorityElement(nums):
    # sort the nums array, all the similar elements will be grouped together
    # we can calculate the frequency from that

    nums.sort()

    for i in range(len(nums)):
        freq = getFreq(nums, i)

        # print(nums[i], freq)

        if freq > math.floor(len(nums)/2):
            # nums[i] is our answer
            return nums[i]

def majorityElement1(nums):
    # we can actually use a hashmap for this problem

    d = {}

    for i in nums:
        if i not in d:
            d[i] = 0
        d[i] = d[i] + 1

    for x in d:
        if d[x] > len(nums)//2:
            return x

def main():
    nums = [2,2,1,1,1,2,2]
    print(majorityElement1(nums))

main()
