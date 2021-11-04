# https://leetcode.com/problems/third-maximum-number/

import sys

def thirdMax(nums):
    # convert the list to a set
    # get the current maximum
    # remove the current maximum
    # repeat the process for 3 times

    nums = set(nums)

    times = 0
    cur_max = -1*sys.maxsize
    first_max = -1*sys.maxsize

    while times < 3 and len(nums) > 0:
        cur_max = max(nums)

        if first_max == -1*sys.maxsize:
            first_max = cur_max

        nums.discard(cur_max)
        times += 1
    
    if times == 3:
        return cur_max
    return first_max

def main():
    nums = [2,2,3,1]
    print(thirdMax(nums))

main()
    
    

        