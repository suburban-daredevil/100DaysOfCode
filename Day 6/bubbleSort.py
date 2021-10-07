
# implementation of the bubble sort algorithm

def bubbleSort(arr):
    # run the steps n-1 times

    # when the input is a sorted array, the loops still checks the entire array and does not swap at all
    # so at any pass, is we do not perform swap implies that array is sorted

    swapped = False
    for i in range(len(arr)):
        # at each pass, the max element in the remaining part of the array will come to the correct position
        # The is it will be pushed to the last
        swapped = False
        for j in range(1, len(arr)-i):
            # swap if the element is smaller than the previous element
            if arr[j] < arr[j-1]:
                # swap
                swapped = True
                arr[j], arr[j-1] = arr[j-1], arr[j]

        # if we do not swap for a particular value of i, it means that the array is sorted, we can return the array
        if swapped is False:
            return

def main():
    arr = [1,2,3,4,5]
    bubbleSort(arr)
    print(arr)

main()

        