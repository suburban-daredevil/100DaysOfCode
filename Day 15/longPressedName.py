# https://leetcode.com/problems/long-pressed-name/

def isLongPressedName(name, typed):
    # for each ch in name, get its first index of occurence in typed
    # slice typed based upon this index and continue

    for i in range(len(name)):
        if name[i] in typed:
            index = typed.index(name[i])
            
            x = name[i]
            typed = typed[index+1:]

            if i == len(name) - 1:
                for ch in typed:
                    if ch != x:
                        return False
        else:
            return False

    return True
    

def main():
    name = "alex"
    typed = "aaleexa"
    print(isLongPressedName(name, typed))

main()