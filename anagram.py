#One string anagram of another

def is_anagram(first,second):
    one = first.lower()
    two = second.lower()
    
    if(len(one) == len(two)):
        sortOne = sorted(one)
        sortTwo = sorted(two)
        
        if(sortOne == sortTwo):
            return True
        else:
            return False
is_anagram("sunny","uNsny")
