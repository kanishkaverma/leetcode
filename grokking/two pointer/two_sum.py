def two_sum(arr, target): 
    # res = []
    start = 0 
    end = len(arr)-1
    sum = arr[start]+arr[end]

    while sum != target: 
        sum = arr[start] + arr[end] 
        if sum>target: 
            end -= 1 
        if sum<target: 
            start += 1 
    
    return [start,end]

def main(): 
    print(two_sum([1,2,3,4,6],6))
    print(two_sum([2,5,9,11],11 ))
main()