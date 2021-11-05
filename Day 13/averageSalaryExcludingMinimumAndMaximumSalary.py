# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

def average(salary):
    # find min, and max and pop them
    mini = min(salary)
    mini_index = salary.index(mini)
    salary.pop(mini_index)

    maxi = max(salary)
    maxi_index = salary.index(maxi)
    salary.pop(maxi_index)

    # find the average of the remaining elements of the array

    avg = sum(salary)/len(salary)
    return avg

def average1(salary):

    # sort the array
    salary.sort()
    
    # pop the first and last element of the array, which will be the minimum and maximum resp
    salary.pop(0)
    salary.pop(len(salary) - 1)

    # find the average of the remaining elements
    avg = sum(salary)/len(salary)
    return avg

def main():
    salary = [8000,9000,2000,3000,6000,1000]
    print(average1(salary))

main()