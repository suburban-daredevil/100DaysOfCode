# https://leetcode.com/problems/count-items-matching-a-rule/

def countMatches(items, ruleKey: str, ruleValue: str) -> int:
    c = 0

    j = -1
    if(ruleKey == 'type'):
        j = 0
    elif(ruleKey == 'color'):
        j = 1
    elif(ruleKey == 'name'):
        j = 2
    
    for i in range(len(items)):
        if(items[i][j] == ruleValue):
            c += 1
    
    return c