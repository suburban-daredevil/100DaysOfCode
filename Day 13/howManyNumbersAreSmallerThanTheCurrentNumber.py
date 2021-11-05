# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# similar to the retrn the rank array problem (1331)
def smallerNumbersThanCurrent(arr):
    temp = arr.copy()

    arr.sort()

    # create a hashmap containing the elements of arr1 as key and their corresponding ranks as value
    d = {}
    
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = i    
    

    for i in range(len(temp)):
        temp[i] = d[temp[i]]
    
    return temp

def main():
    nums = [7,7,7,7]
    print(smallerNumbersThanCurrent(nums))

main()