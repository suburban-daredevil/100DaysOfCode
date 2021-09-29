# https://leetcode.com/problems/reach-a-number/

# approach
# if I add i to curent value of start, there are 3 cases
# start + i == target => return ans + 1
# start + i < target => increment start with i
# start + i  > target => decremet start with i

def reachNumber(target: int):
    
    # i value startes from 1, so min number of steps required to reach the target = 0 is 1
    if target == 0:
        return 1

    if target < 0:
        target = target*-1

    start = 0
    i = 1

    while start < target:
        start += i
        i += 1
    
    while (start - target)%2:
        start += i
        i += 1
    
    return i - 1

def main():
    target = 100
    print(reachNumber(target))

main()