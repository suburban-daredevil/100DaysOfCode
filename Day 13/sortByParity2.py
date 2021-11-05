# https://leetcode.com/problems/sort-array-by-parity-ii/

def sortByParity1(nums):
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

def sortArrayByParity2(nums):
    # apply sort by parity 1
    # get all the even elements to the left and odd elements to the right
    sortByParity1(nums)

    # apply two pointer algorithm
    start = 0
    end = len(nums) - 1

    while start <= end:
        # condition to move start pointer
        # if start index is even and element at start index is also even, move start
        if start % 2 == 0 and nums[start] % 2 == 0:
            start += 1

        # condition to move end pointer
        # if end index is odd and element at end index is also odd, move end
        elif end % 2 != 0 and nums[end] % 2 != 0:
            end -= 1

        # condition for swapping
        else:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    return nums

def main():
    nums = [2,3]
    print(sortArrayByParity2(nums))

main()