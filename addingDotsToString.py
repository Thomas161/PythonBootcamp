# add and remove dots between characters

def add_dots(s):
    print(".".join(s))
return ".".join(s)
    
add_dots("Name")

def remove_dots(s):
    res = s.replace(".","")
    print(res)
    return res
    
remove_dots("m.a.m")
