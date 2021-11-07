# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

def freqAlphabets(s):
    # iterate through the string
    # at each index i, check if i is either 1 or 2, if true, check if i+2 is '#' or not
    # if s[i+2] == '#', from a substring with characters, i, i+1, i+2, and get it's represenatation from the map, append it to the resultant string, i += 3
    # else, get the represenatation of s[i] from the map and appand it to the resultant string, i += 1

    i = 0
    result = ''
    hashMap = {
        '1':'a',
        '2':'b',
        '3':'c',
        '4':'d',
        '5':'e',
        '6':'f',
        '7':'g',
        '8':'h',
        '9':'i',
        '10#':'j',
        '11#':'k',
        '12#':'l',
        '13#':'m',
        '14#':'n',
        '15#':'o',
        '16#':'p',
        '17#':'q',
        '18#':'r',
        '19#':'s',
        '20#':'t',
        '21#':'u',
        '22#':'v',
        '23#':'w',
        '24#':'x',
        '25#':'y',
        '26#':'z',
    }

    while i < len(s):
        if s[i] == '1' or s[i] == '2':
            if i+2 < len(s) and s[i+2] == '#':
                temp = s[i] + s[i+1] + s[i+2]
                result += hashMap[temp]
                i += 2
            else:
                result += hashMap[s[i]]
        else:
                result += hashMap[s[i]]

        i += 1
    
    return result

def main():
    s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    print(freqAlphabets(s))

main()