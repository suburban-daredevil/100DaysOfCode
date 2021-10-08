def getMaxIndex(arr, start, end):

    max = 0
    for i in range(start, end+1):
        if arr[i] > arr[max]:
            max = i
    return max

def selectionSort(arr):

    for i in range(len(arr)):
        last = len(arr) - i -1

        max = getMaxIndex(arr, 0, last)

        arr[max], arr[last] = arr[last], arr[max]

def main():
    arr = [5,4,3,2,1]
    selectionSort(arr)
    print(arr)

main()
