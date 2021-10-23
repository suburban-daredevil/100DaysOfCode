# https://leetcode.com/problems/contains-duplicate/

def cyclic_sort(nums):

    i = 0
    while i < len(nums):

        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

def containsDuplicate(nums):
    # apply cyclic sort
    # check if there exists any element at the wrong index
    # If so, return true
    # else return False

    cyclic_sort(nums)

    for i in range(len(nums)):
        
        if nums[i] != i+1:
            # duplicate exists
            return True
    
    # no duplicate element can be found
    return False

def main():
    nums = [1,2,3,1]
    print(containsDuplicate(nums))

main()