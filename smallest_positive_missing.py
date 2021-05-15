
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].j
def solution(A): 
    len_A = len(A)  #3
    set_A = set()
    smallest_postive = 1
    loop_break = False
    for elem in A: 
        set_A.add(elem) 
    for x in range(1,len_A+1): 
        if x  not in set_A: 
            loop_break = True 
            break 
    smallest_postive = x
    if x == len_A and loop_break == False: 
        smallest_postive = x+1

    return smallest_postive
    