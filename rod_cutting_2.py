
INF = 100000;
r = [0] + [-1*INF]*5

def max(x, y):
  if x > y:
    return x
  return y

def bottom_up_rod_cutting(c, n):
  r = [0]*(n+1)
  r[0] = 0

  for j in range(1, n+1):
    maximum_revenue = -1*INF
    for i in range(1, j+1):
      maximum_revenue = max(maximum_revenue, c[i] + r[j-i])
    r[j] = maximum_revenue
  return r[n]

if __name__ == '__main__':
  #array starting from 1, element at index 0 is fake
#   c = [0, 10, 24, 30, 40, 45]

    price = [0,1,5,8,9,10,17,17,20,24,30]
    n = 8 
    x = bottom_up_rod_cutting(price, n)
    print(x)