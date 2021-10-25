# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

def arrayStringsAreEqual(word1, word2) -> bool:

    result1 = ''
    result2 = ''

    for x in word1:
        result1 += x

    for x in word2:
        result2 += x

    return result1 == result2

def main():
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]

    print(arrayStringsAreEqual(word1, word2))

main()