# https://leetcode.com/problems/missing-number/

def missingNumber(nums):
    # find the expected sum and the actual sum of the array
    # their difference would be the missing number

    n = len(nums)

    expected_sum = int(n*(n+1)/2)

    acutal_sum = sum(nums)

    return expected_sum - acutal_sum

def missingNumber2(nums):
    # we can use a hashmap to check the presence of an element in constant time

    map = {}

    for i in range(len(nums)):
        map[nums[i]] = -1

    for i in range(len(nums) + 1):
        if i not in map:
            return i

def missingNumber3(nums):
    # apply cyclic sort
    # after increasing the size of the array by 1
    # index = value
    
    nums.append(-1)

    i = 0

    ans = -1

    while i < len(nums):
        correct = nums[i]

        if nums[i] == -1 or nums[i] == nums[correct]:
            if nums[i] == -1:
                ans = i
            i += 1

        else:
            nums[i], nums[correct] = nums[correct], nums[i]
    
    # the index of -1 will be the result

    return ans

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]

        if correct >= len(nums) or nums[i] == nums[correct]:
            i += 1
        else:
            nums[i], nums[correct] = nums[correct], nums[i]

# best of my submissions
def missingNumber4(nums):
    # we can use cyclic sort without needing to append any extra element
    # we can ignore the element that is greater than or equal to the size of the array
    # the first misplaced element is our answer

    cyclic_sort(nums)

    print(nums)

    for i in range(len(nums)):
        if i != nums[i]:
            return i
    
    # this return executes, when all the elements from 0 to n-1 is present
    # n is our result in this case
    return len(nums)


def main():
    arr = [3,0,1]
    print(missingNumber4(arr))

main()