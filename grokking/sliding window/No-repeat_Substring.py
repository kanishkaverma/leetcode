
def no_repeat(str): 
    start, length = 0,0
    char = { }
    for end in range(len(str)): 
        right = str[end]

        if right in char: 
            start = max(start, char[right] + 1 )
        
        char[right] = end 
        length  = max(length, end-start +1 )
    return length


def main(): 
    print(no_repeat('aabccbb'))

    print(no_repeat('abbbb  '))
main()
