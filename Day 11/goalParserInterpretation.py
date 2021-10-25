# https://leetcode.com/problems/goal-parser-interpretation/

def interpret(str):
    i = 0

    result = ''

    while i < len(str):
        if str[i] == 'G':
            result += 'G'
        
        elif str[i] == '(':
            if str[i+1] == ')':
                result += 'o'
                i += 1
            else:
                result += 'al'
                i += 3        
        i += 1

    return result

def main():
    command = "(al)G(al)()()G"
    print(interpret(command))

main()