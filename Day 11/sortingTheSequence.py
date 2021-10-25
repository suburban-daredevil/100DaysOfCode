# https://leetcode.com/problems/sorting-the-sentence/

def myFun(x):
    return int(x[-1])

def sortSentence(s):

    s = list(s.split())

    s.sort(key = myFun)

    result = ''

    for i in range(len(s)):
        x = s[i]
        result += (x[:-1])
        
        if i+1 < len(s):
            result += ' '

    return result

def main():
    s = "Myself2 Me1 I4 and3"
    ans = sortSentence(s)
    print(ans)

main()