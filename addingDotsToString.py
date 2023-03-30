# In progress

def add_dots(s):
    res = ""
    for r in range(len(s)):
        res += s[r]+"."
        if res[len(res)-1] == ".":
            print(res[len(res)-1])
            res[len(res)-1].replace(".","")
            # # res[:-1]
            # print(res)
            # res += s[r]+""
            # print(len(res[:-1]))
    return res
    
add_dots("Name")
