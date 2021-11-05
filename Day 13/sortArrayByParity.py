# https://leetcode.com/problems/sort-array-by-parity/

def myFunc(x):
    return x%2

def sortArrayByParity(nums):
    # we can use the key parameter of the inbuilt sort function available
    nums.sort(key = myFunc)
    return nums

def sortArrayByParity1(nums):
    # we can use the partition function of quick sort
    # with start and end pointers to solve this question

    start = 0
    end = len(nums) - 1

    while start <= end:
        if nums[start] % 2 == 0:
            start += 1
        
        elif nums[end] % 2 != 0:
            end -= 1
        
        else:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    return nums

def main():
    nums = [3,1,2,4]
    print(sortArrayByParity1(nums))

main()