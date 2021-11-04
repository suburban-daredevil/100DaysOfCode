# https://leetcode.com/problems/intersection-of-two-arrays/

def intersection(nums1, nums2):
    # convert the arrays to sets
    nums1 = set(nums1)
    nums2 = set(nums2)

    # calculate the set difference of the two sets
    result = nums1.difference(nums2)

    # perform subtraction with set1 and set difference of the two sets
    my_result = nums1.difference(result)

    return list(my_result)

def main():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    print(intersection(nums1, nums2))

main()