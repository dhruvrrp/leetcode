x = -123
rev = 0
sign = 1
if x < 0:
    sign = -1
x = x*sign
while x != 0:
    d = abs(x%10)
    x = int(x/10)
    rev = rev* 10 + d
rev = rev * sign
if rev > (2**31 -1) or rev < -2**31:
    print(0)
print(rev)