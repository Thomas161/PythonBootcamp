# Count syllables

def count(s):
    hy = "-"
    x = s.count(hy)
    print(x)
    if x == 0:
        return 1
    if x > 0:
        return x += 1
    return x
    
count("Star")
