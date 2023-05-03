def get_first_idx(s):
    idx = len(s) - 1

    while s[idx] == " ":
        idx -= 1

    return idx 



def lengthOfLastWord(s: str) -> int:
        
    idx = get_first_idx(s)
    count = 0

    for i in range(idx, -1, -1):
        
        if s[i] == " ":
            break
        count += 1
        

    return count



w = "Hello World"

a = lengthOfLastWord(w)

print(a)