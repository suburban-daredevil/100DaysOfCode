
# function to implement the insertion sort
# i runs from [0, n-2]
# j runs from [i+1,0] (j decreases)
# when we are at a particular j, it means that the elements upto index j-1 are already sorted
def insertionSort(arr):
    for i in range(len(arr)-1):
        j = i+1
        while j > 0:
            # when element at a particular index is less than its previous element, we swap
            # if not, we have placed the element in its required position => break the loop
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
            else:
                break

def main():
    arr = [5,8,0,3,1,-7,4,-5]
    insertionSort(arr)
    print(arr)

main()
