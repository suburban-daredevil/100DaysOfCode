# https://leetcode.com/problems/first-missing-positive/

# using cyclic sort to solve this problem

# apply cyclic sort ignoring negatives and numbers > N

def cyclic_sort(arr):
    i = 0

    while i < len(arr):
        if arr[i] <= 0 or arr[i] > len(arr):
            i += 1
            continue

        correct = arr[i] - 1

        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

def firstMissingPositive(nums):
    cyclic_sort(nums)

    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1

    return len(nums) + 1

def main():
    nums = [3,4,-1,1]
    print(firstMissingPositive(nums))

main()