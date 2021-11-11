# https://leetcode.com/problems/implement-strstr/submissions/

# return the index of first occurence of needly in haystack
# return -1, if needle is not present in the haystack

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1

def main():
    haystack = ""
    needle = ""
    print(strStr(haystack, needle))

main()
