
# function to implement the cyclic sort algorithm
def cyclicSort(arr):
    # we try to put the elements in the correct indices
    # index = value - 1

    # if an element is at its correct index, we move forward
    # else, as long as the element is not at its correct index, we try to put it in its correct index

    i = 0

    while i < len(arr):

        correct = arr[i] - 1

        # check if the element is at its correct position
        
        if arr[i] == arr[correct]:
            i += 1
            
        else:
            arr[i], arr[correct] = arr[correct], arr[i]
        
def main():
    arr = [5,4,3,2,1]
    cyclicSort(arr)
    print(arr)

main()