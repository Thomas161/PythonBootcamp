# Are two identical letters next to each other by index

def double_letters (word) :
    for i in range(len(word) - 1):
        wordOne = word[i]
        wordTwo = word[i+1]
        if wordOne == wordTwo:
            return True
    return False

double_letters("kill")
