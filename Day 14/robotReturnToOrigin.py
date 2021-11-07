# https://leetcode.com/problems/robot-return-to-origin/

def judgeCircle(moves):
    # from the moves string, count the number of left, right, up and down movement by the robot
    # if the count of up == down and right == left, return True
    # else return False

    hashMap = {
        'R':0,
        'L':0,
        'U':0,
        'D':0,
    }

    for ch in moves:
        hashMap[ch] += 1
    
    if hashMap['R'] == hashMap['L']:
        if hashMap['U'] == hashMap['D']:
            return True

    return False

def main():
    moves = "LDRRLRUULR"
    print(judgeCircle(moves))

main()