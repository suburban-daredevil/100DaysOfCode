# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

def findSum(x, a):
    return a*x - a*(a+1)//2

def maxValue(n: int, index: int, maxSum: int) -> int:
    # the max value can range from 1 to maxSum
    # apply BS on the range [1, maxSum]

    start = 1
    end = maxSum

    # number of elements to the left of mid excluding mid
    leftCount = index

    # number fo elements to the right of mid exculding mid
    rightCount = n - index - 1

    ans = -1

    while start <= end:
        mid = start + (end-start)//2

        # calculate left sum and right sum

        # leftsum is the sum of elements from mid-1 + mid-2 + mid -3+ ..
        # but mid - 1at some stage can become zero. But the array must contain only positive numbers
        # so such entries must be 1
        # initially calculating leftSum excluding such ones
        leftSum = findSum(mid, min(mid-1, leftCount))

        # adding up for the number of such ones
        leftSum += max(0, index - mid + 1)

        # similar approach for the right side of mid
        rightSum = findSum(mid, min(mid-1, rightCount))
        rightSum += max(0, n - index - mid)

        
        if mid + leftSum + rightSum <= maxSum:
            # mid is a potential ans
            # but there might be some element, greater then mid and still be an answer
            # update ans and search in the right side of mid
            ans = mid
            start = mid + 1
        
        else:
            # search in the left side of mid
            end = mid - 1

    return ans


def main():
    n = 4
    index = 2
    maxSum = 6
    print(maxValue(n, index, maxSum))

main()

    

    

    
