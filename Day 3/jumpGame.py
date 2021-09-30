# https://leetcode.com/problems/jump-game/

# maintain a reach variable
# update reach such that, reach will be the maximum of existing reach or the maximum possible element that can be reached from that index
# maximum possible index reachable from a given index x => x + nums[x]


def canJump(nums):
    n = len(nums)
    reach = 0
    i = 0

    # maximum possbile index, reachable from i is reach
    # as long as i remains less than or equal to reach we can continue
    # if reach is exhausted and if we cannot reach the end index, loop conditon fails and return False
    while i <= reach and i < n:
        reach = max(reach, i + nums[i])
        if reach >= n-1:
            return True
        
        i += 1
    
    return False