def longest_substring_map(str, k):
    length = 0
    char = {}
    start = 0
    for end in range(len(str)):
        right = str[end]
        if right not in char:
            char[right] = 0
        char[right] += 1
        while len(char) > k:
            left = str[start]
            char[left] -= 1 
            if char[left] ==0:
                del char[left]
            start += 1
        length = max(length, end-start + 1)
    return length

def longest_substring_set(str, k): 
    length = 0 
    start = 0
    char = set()
    for end in range(len(str)): 
        right = str[end]
        char.add(right)
        while len(char) > k: 
            left = str[start]
            char.pop()
            start += 1 
        length = max(length, end-start+1)
    return length

        

def main(): 
    print( longest_substring_set('araaci',2 ))

    print( longest_substring_set('araaci',1  ))

    print( longest_substring_set('cbbebi',3 ))
main()