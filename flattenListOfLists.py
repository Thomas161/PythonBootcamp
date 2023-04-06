#Flatten list of lists

def flatten(l):
    res = []
    for i in l:
        for x in i:
            res.append(x)
    return res
flatten([[12,3], [9,76]])
