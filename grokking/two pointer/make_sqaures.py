def make_squares(arr):
    n = len(arr)
    max_index = n-1 
    squares = [0 for x in range(n)]
    left, right = 0, n-1 
    while left <= right:
        left_square = arr[left]*arr[left]
        right_square = arr[right]*arr[right]
        if left_square>right_square:
            squares[max_index] = left_square
            left +=1 
        else: 
            squares[max_index] = right_square
            right -=1 
        max_index -=1 
    return squares

def main(): 
    print(make_squares([-2,-1,0,2,3]))

main()
