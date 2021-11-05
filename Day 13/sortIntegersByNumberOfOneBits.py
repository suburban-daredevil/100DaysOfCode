# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

# function to get the number of one's in the binary representation of x
def myFunc(x):
    bin_x = bin(x)[2:]
    count = 0
    for i in range(len(bin_x)):
        if bin_x[i] == '1':
            count += 1
    return count

def sortByBits(arr):
    arr.sort(key = lambda x : (myFunc(x),x))
    return arr

def main():
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    print(sortByBits(arr))

main()