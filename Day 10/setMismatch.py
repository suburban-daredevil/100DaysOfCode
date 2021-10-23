# https://leetcode.com/problems/set-mismatch/

def cyclic_sort(arr):
    i = 0

    while i < len(arr):
        correct = arr[i] - 1

        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

def findErrorNums(nums):
    # apply cyclic sort on the array
    # the first mismatch is the repeated element and its index + 1 is the actual element

    cyclic_sort(nums)

    result = []

    for i in range(len(nums)):
        if nums[i] != i+1:
            result.append(nums[i])
            result.append(i+1)
            return result

def main():
    nums = [1,7,5,4,6,6,2,3]
    print(findErrorNums(nums))

main()