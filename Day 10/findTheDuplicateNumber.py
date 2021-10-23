# https://leetcode.com/problems/find-the-duplicate-number/

def cyclic_sort(arr):
    i = 0

    while i < len(arr):
        correct = arr[i] - 1

        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

def findDuplicate(nums):
    # apply cyclic sort
    # return the first element at incorrect index

    cyclic_sort(nums)

    # first element at the incorrect index is our required duplicate element
    for i in range(len(nums)):
        if nums[i] != i+1:
            return nums[i]

def main():
    nums = [1,1,2]
    print(findDuplicate(nums))

main()
        