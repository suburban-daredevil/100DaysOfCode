# returns the index of the maximum element in the given range
def getMax(arr, start, end):
    max = 0

    for i in range(start, end+1):
        if arr[i] > arr[max]:
            max = i
    return max

# implement the selection sort algorithm
def selectionSort(arr):

    for i in range(len(arr)):
        # find the max element in the remaining array and swap it with the correct index

        # last index with which I need to swap
        last = len(arr) - i - 1

        # get the maximum element from the array
        maxIndex = getMax(arr, 0, last)

        arr[maxIndex], arr[last] = arr[last], arr[maxIndex]

def main():
    arr = [5,4,-3,2,-1]
    selectionSort(arr)
    print(arr)

main()


