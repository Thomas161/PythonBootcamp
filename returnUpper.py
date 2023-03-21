# Return indexes of upper chars in a string

def capital_indexes (n):
    indexes = []
    for i,r in enumerate(n):
        if r.isupper():
            indexes.append(i)
    return indexes
     
red = "TwISt"   
capital_indexes(red)
        
