# https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverseWords(s):
    # convert the string s, into a list of words
    # reverse each word of the list
    # conver the list to string and return

    myList = s.split()

    for i in range(len(myList)):
        myList[i] = myList[i][::-1]
    
    result = ''
    for newWord in myList:
        result += newWord
        result += ' '
    
    result = result.strip()

    return result

def main():
    s = "Let's take LeetCode contest"
    print(reverseWords(s))

main()
