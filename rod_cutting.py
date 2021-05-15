import math

def bottom_up_cut_rod(p, n): 
    r = [0]*(n+1) 
    r[0] = 0

    for j in range(1, n+1 ): 
        q = -math.inf

        for i in range(1,j+1): 
            q= max(q,p[i] + r[j-i])
        
        r[j] = q
    return r[n]

def main(): 
    price = [0,1,5,8,9,10,17,17,20,24,30]
    n = [5,8,9] 

    for num in n: 
        print(bottom_up_cut_rod(price, num))




if __name__ ==  "__main__": 
    main()