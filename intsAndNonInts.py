# return true if both params are ints, return false if either param not an int

def only_ints (a,b) :
    if (type(a) is int) and (type(b) is int):
        return True
    else:
        return False
        
only_ints(4,2)
