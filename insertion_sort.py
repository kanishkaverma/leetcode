def insertion_sort(num): 
    for i in range(1, len(num)): 
        key = num[i]
        j = 1-1 

        while j>=0 and num[j]>key: 
            num[j+1] = num[j]
            j -=1 
            num[j+1]=key 

