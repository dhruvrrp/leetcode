class Solution:
    def myAtoi(self, str: str) -> int:
        curNum = 0
        firstNum = False
        count = 0
        sign = 1
        for i in str:
            if i == ' ' and firstNum is False:
                sign = 1
                if count == 1:
                    return 0
            elif i == '-' and firstNum is False and count == 0:
                sign = -1
                count = 1
            elif i == '+' and firstNum is False and count == 0:
                sign = 1
                count = 1
            elif i.isdigit():
                firstNum = True
                curNum = curNum*10 + int(i)
            else:
                if firstNum:
                    curNum = curNum*sign
                    if curNum < -2**31:
                        return -2**31
                    elif curNum > 2**31 -1:
                        return 2**31 - 1
                    else:
                        return curNum
                else:
                    return 0
        if firstNum:
            curNum = curNum*sign
            if curNum < -2**31:
                return -2**31
            elif curNum > 2**31 -1:
                return 2**31 - 1
            else:
                return curNum
        else:
            return 0