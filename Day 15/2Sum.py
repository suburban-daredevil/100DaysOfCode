# https://leetcode.com/problems/two-sum/

# approach1 - 1
# brute force - O(n^2)
def twoSum(nums, target):
    # we pick an element from the array
    # we try to find target-element exists in the array or not
    # make sure that, element picked and the target-element are not the same element from the array

    for i in range(len(nums)):
        x = target - nums[i]
        for j in range(len(nums)):
            if i != j and nums[j] == x:
                return [i,j]

def linearSearch(nums, x, index):
    for i in range(len(nums)):
        if nums[i] == x and i != index:
            return i
    
    return -1

# apporach 2 - using linear search
def twoSum1(nums, target):
    # we pick an element from num
    # we search for target-element in num such that, index of element and target-element are different
    # use linear search for this approach

    for i in range(len(nums)):
        x = target - nums[i]

        index = linearSearch(nums, x, i)
        if index != -1:
            return [i, index]
    
    # if no such element is found
    return [-1, -1]

# approach 3 - using a hashmap
# create an hashmap with element = key and index of element = value
# pick an element, search for target - element in the hashmap 
# such that index of element and target-element are not the same

def twoSum2(nums, target):
    lookup = {}

    for i in range(len(nums)):
        if nums[i] not in lookup:
            lookup[nums[i]] = []
        lookup[nums[i]].append(i)

    for i in range(len(nums)):
        x = target - nums[i]
        if x in lookup:
            temp = lookup[x]
            for j in range(len(temp)):
                if i != temp[j]:
                    return [i, temp[j]]
    return [-1, -1]
    
def main():
    nums = [2,7,11,15]
    target = 9
    print(twoSum2(nums, target))

main()