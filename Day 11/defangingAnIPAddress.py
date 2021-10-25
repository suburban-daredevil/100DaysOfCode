# https://leetcode.com/problems/defanging-an-ip-address/

# traverse through the string and keep updating the result string
# if you find '.', replace it with '[.]'

def defangIPaddr(address):
    result = ''

    for ch in address:
        if ch == '.':
            result += '[.]'
        else:
            result += ch
    
    return result

def main():
    address = "255.100.50.0"
    print(defangIPaddr(address))

main()