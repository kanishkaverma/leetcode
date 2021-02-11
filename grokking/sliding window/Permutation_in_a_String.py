def permutation(arr, s): 
    k = len(s)
    char_set = set()
    tar_set = set(s)
    for end in range(len(arr)): 
        right = arr[end]
        
        char_set.add(right)
        if end >= k -1 and right not in char_set: 
            char_set.pop()
        if char_set == tar_set: 
            return True
    return False

def permutation_hashmap(arr,s ): 
    pass

def main(): 
    print(permutation('oidbcaf', 'abc'))
    print(permutation('bcdxabcdy', 'bcdyabcdx'))
    print(permutation('aaacb', 'abc') )
    print(permutation('odicf', 'dc'))
    print()


main()
        