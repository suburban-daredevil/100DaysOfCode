# implement the bubble sort algorithm to sort the array
def bubbleSort(arr):

    swapped = False

    for i in range(len(arr)):
        swapped = False
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j-1]:
                swapped = True
                arr[j], arr[j-1] = arr[j-1], arr[j]
        
        if swapped is False:
            return

def main():
    arr = [5,1,4,3,2]
    bubbleSort(arr)
    print(arr)

main()


            
