# return count for number of online statuses in dict

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count (stats) :
    val = 0
    for num in stats:
        if stats[num] == "online":
            val += 1
    return val
        
online_count(statuses)
