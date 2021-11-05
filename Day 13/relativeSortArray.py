# https://leetcode.com/problems/relative-sort-array/

def myFunc(x, arr2):
    return arr2.index(x)

def relativeSortArray(arr1, arr2):
    # split the arr1 into 2
    
    # contains elements that are in arr2 also
    x1 = []

    # contains elements that are not in arr2
    x2 = []

    for i in arr1:
        if i in arr2:
            x1.append(i)
        else:
            x2.append(i)
            
    x1.sort(key = lambda x : myFunc(x, arr2))
    x2.sort()

    for i in x2:
        x1.append(i)

    return x1

def main():
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]

    print(relativeSortArray(arr1, arr2))

main()
    

    
    

