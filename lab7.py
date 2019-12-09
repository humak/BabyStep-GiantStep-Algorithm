#udl computational tools for problem solving lab7
#humakal
#'19
import math

def bsgs(y, g, p):
    #  y = g^x  mod   p
    s = math.ceil( math.sqrt(p) ) 
    l1 = []
    l2 = []
    for i, j in zip(range(s+1), range(s+1)):
        l1.append([  (2 * (10**j)) % p  , j   ]  )
        l2.append([  (10**(5*i)) % p      , 5*i ]  )

    for i in range (s+1):
        for i2 in range (s+1):
            if ( l1[i][0] == l2[i2][0] ):
                return l2[i2][1] - l1[i][1]
               
def main():
    y, g, p = 2, 10, 19    #17
    #y, g, p = 3, 12, 29    #10
    #y, g, p = 13, 19, 71   #28
    x = bsgs(y, g, p)
    print(x % p-1)
    
if __name__== "__main__":
  main()