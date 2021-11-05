# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

def canMakeArithmeticProgression(arr):
    # sort the array
    # check if there exists a common difference between the elements of the array

    arr.sort()

    cd = arr[1] - arr[0]

    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != cd:
            return False
    
    return True

def main():
    arr = [1,2,4]
    print(canMakeArithmeticProgression(arr))

main()