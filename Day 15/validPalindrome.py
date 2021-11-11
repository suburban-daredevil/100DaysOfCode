# https://leetcode.com/problems/valid-palindrome/

# convert s to a string of lowercase non-alphanumeric string
# check if s is a palindrome or not

def isPalindrome(s):

    s = s.lower()
    my_string = ''

    for ch in s:
        if ch.isalnum():
            my_string += ch
    
    start = 0
    end = len(my_string) - 1

    while start <= end:
        if my_string[start] == my_string[end]:
            start += 1
            end -= 1
        else:
            return False
    
    return True    

def main():
    s = ""
    print(isPalindrome(s))

main()