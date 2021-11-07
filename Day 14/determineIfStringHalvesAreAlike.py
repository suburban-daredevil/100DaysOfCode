# https://leetcode.com/problems/determine-if-string-halves-are-alike/

def checkIfThereAreEvenNumberOfVowels(s):
    
    # convert the string entirely to lower/upper case
    # count the number of vowels in the string
    # if the number of vowels is even, count the number of vowels in the first and second half of the string
    # if they are same, return True
    # else return False

    s = s.lower()

    count = 0

    for i in s:
        if i in ['a','e','i','o','u']:
            count += 1

    if count % 2 == 0:
        return True
    else:
        return False

def halvesAreAlike(s):
    if not(checkIfThereAreEvenNumberOfVowels(s)):
        return False
    
    s = s.lower()
    count1 = 0
    count2 = 0

    for i in range(len(s)//2):
        if s[i] in ['a','e','i','o','u']:
            count1 += 1
    
    for i in range(len(s)//2,len(s)):
        if s[i] in ['a','e','i','o','u']:
            count2 += 1
    
    if count1 == count2:
        return True
    
    return False

def main():
    s = "tkPAdxpMfJiltOerItiv"
    print(halvesAreAlike(s))

main()