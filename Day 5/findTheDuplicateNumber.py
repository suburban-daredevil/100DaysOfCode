# https://leetcode.com/problems/find-the-duplicate-number/

def findDuplicate(nums) -> int:
    sumArray = sum(nums)

    # ans lies in the range of [1,n]

    n = len(nums)

    start = 1
    end = n

    while start <= end:
        mid = start + (end-start)//2

        # check is mid forms a valid answer

        # if mid is the answer, then mid occurs more than once in the array
        # then the sum of remaining elements would be sumArray - mid*freqOfMid

        freq = 0
        for x in nums:
            if x == mid:
                freq += 1
        
        remainingSum = sumArray - mid*freq

        # now we need to find the actual sum of the elements excluding mid 
        actualSum = 0
        for ele in nums:
            if ele != mid:
                actualSum += ele
        

        # if the remainingSum is equal to the actualSum, then mid is our answer

        if remainingSum == actualSum and freq > 1:
            return mid
        
        # if remainingSum > actualSum, then the mid we have selected is small
        # then search in the right side of mid

        if remainingSum > actualSum:
            start = mid + 1

        # else search in the left side of mid
        else:
            end = mid

    return -1

def main():
    nums = [1,4,4,2,4]
    print(findDuplicate(nums))

main()




