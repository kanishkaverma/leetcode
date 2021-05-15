
def maxSubArray( arr): 
    maxsum, currentSum = arr[0], 0 

    for end in range(len(arr)): 
        currentSum += arr[end]

        if currentSum < 0: 
            currentSum= 0 
        if currentSum > maxsum: 
            maxsum = currentSum; 

    return maxsum
        


def main(): 
    print(maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])) 

main()
