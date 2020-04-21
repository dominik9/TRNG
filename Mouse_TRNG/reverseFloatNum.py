from struct import pack, unpack

def reverseBits(n):
    rev = 0
    for counter in range(8):
        rev <<= 1
        if n & 1 == 1:
            rev ^= 1
        n >>= 1
    return rev

def reverseFloat(s):
    fs = pack('d', s)
    bval = list( unpack('BBBBBBBB', fs))
    for b in range(len(bval)):
        bval[b] = reverseBits(bval[b])
    bval.reverse()
    fs = pack('BBBBBBBB', *bval)
    fnew = unpack('d',fs)
    return fnew[0]



