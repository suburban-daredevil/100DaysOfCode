# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

def numOfStrings(patterns, word):
    # iterate through the patterns array
    # check if each element of the array is a substring of the word or not
    # update count correspondingly

    count = 0

    for i in patterns:
        if i in word:
            count += 1
    
    return count

def main():
    patterns = ["a","a","a"]
    word = "ab"
    print(numOfStrings(patterns, word))

main()