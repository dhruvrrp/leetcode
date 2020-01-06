numRows = 4
s ='PAYPALISHIRING'


result = ""

slen = max(2*(numRows-1),1)
j = 0
print(slen)
while j < len(s):
    result = result + s[j]
    j = j + slen
sslen = slen
rowN = 1
print(result)
while rowN < numRows - 1:
    curRowS = rowN
    curSpace = sslen - 2
    while curRowS < len(s):
        result = result + s[curRowS]
        curRowS = curRowS + curSpace
        curSpace = slen - curSpace
        
    print(result)
    sslen = sslen - 2
    rowN = rowN + 1
lastR = rowN
slen = 2*(numRows-1)
if lastR < numRows:
    print(result)      
    while lastR < len(s):
        if (lastR) < len(s):
            result = result + s[lastR]
            lastR = lastR + slen
print(result)