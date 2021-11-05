# https://leetcode.com/problems/rank-transform-of-an-array/

def arrayRankTransform(arr):
    # create a copy of the original array
    temp = arr.copy()

    # create arr1 such that it has only the unique elements of arr
    arr1 = list(set(arr))

    arr1.sort()

    # create a hashmap containing the elements of arr1 as key and their corresponding ranks as value
    d = {}
    for i in range(len(arr1)):
        d[arr1[i]] = i+1
    
    # for each element of temp, replace it with its rank from the hashmap
    for i in range(len(temp)):
        temp[i] = d[temp[i]]
    
    return temp

def main():
    arr = [37,12,28,9,100,56,80,5,12]
    print(arrayRankTransform(arr))

main()

