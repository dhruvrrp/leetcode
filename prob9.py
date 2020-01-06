class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        start = str(x)
        l = 0
        r = len(start) -1
        while l < r:
            if start[l] == start[r]:
                l+=1
                r-=1
            elif l == r:
                return True
            else:
                return False
        return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        start = x
        rev = 0
        while start != 0:
            d = start%10
            start = int(start/10)
            rev = rev*10 + d
        if rev == x:
            return True
        else:
            return False