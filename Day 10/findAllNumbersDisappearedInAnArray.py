# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

def cyclic_sort(arr):
    i = 0

    while i < len(arr):
        correct = arr[i] - 1

        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1


def findDisappearedNumbers(nums):
    # apply cyclic sort on the array
    # all the numbers that are not in place after applying cyclic sort are our answers

    cyclic_sort(nums)

    result = []

    # find out the elements that are not in place in nums
    # after applying cyclic sort on nums

    for i in range(len(nums)):
        if nums[i] != i+1:
            result.append(i+1)

    return result

def main():
    nums = [1,1]
    print(findDisappearedNumbers(nums))

main()