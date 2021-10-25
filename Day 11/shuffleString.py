# https://leetcode.com/problems/shuffle-string/

def restoreString(s,indices):
    # build the result array
    # take the elements of the result array and convert it into a string and return

    result = [None for i in range(len(s))]

    for i in range(len(s)):
        result[indices[i]] = s[i]
    

    answer = ''
    for ch in result:
        answer += ch

    return answer

def main():
    s = "aiohn"
    indices = [3,1,4,2,0]

    print(restoreString(s, indices))

main()