# https://leetcode.com/problems/sort-array-by-increasing-frequency/
from sys import maxsize as INF

def myFunc(freq, x):
    return freq[x]

def frequencySort(nums):
    # create a freq map
    # sort the elements of the array based upon the entry from the frequency map
    # if 2 elements have the same frequency, sort them based upon inf - x

    freq = {}
    for i in nums:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1

    nums.sort(key = lambda x : (myFunc(freq, x), INF-x))
    return nums

def main():
    nums = [2,3,1,3,2]
    print(frequencySort(nums))

main()
        