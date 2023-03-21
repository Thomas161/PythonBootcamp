# Return empty string if even length, return middle characters if odd length

import math

def mid (str) :
    # for s in range(len(str)):
    if len(str) % 2 == 0:
        return ""
    elif len(str) % 2 == 1:
        ret = len(str) / 2
        result = math.ceil(ret)
        return   str[result-1]
        
mid("Pools")
