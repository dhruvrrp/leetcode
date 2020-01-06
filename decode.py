def decodeVariations(S):
    """
    @param S: str
    @return: int
    """
    decode = [0] * (len(S) + 1)
    decode[0] = 1
    decode[1] = 1
    for i in range(2, len(S)+1):
        curr = int(S[i-1])
        prev = int(S[i-2])
        prev_num = prev*10 + curr
        if curr == 0 and prev == 0:
            return 0
        if curr != 0:
            decode[i] = decode[i] + decode[i-1]
        if 10 <= prev_num <= 26:
            decode[i] = decode[i] + decode[i-2]

    return decode[len(S)]


def decodeVariations2(S):
    """
    @param S: str
    @return: int
    """
    pre, cur = 27, 0
    first, second = 1, 1
    for i in range(len(S)-1, -1, -1):
        d = int(S[i])
        print(d)
        if d == 0:
          cur = 0
        else:
          cur = first
          if d * 10 + pre < 27:
            cur += second
        pre = d
        first, second = cur, first
    return cur
print(decodeVariations2('1262'))

