def dp ( l1 , l2 ) : 
    print('l1: ', l1)
    print('l2: ', l2)
    
    def p ( ll1 , ll2 , n ) : 
        print('ll1: ', ll1)
        print('ll2: ', ll2)
        print('n: ', n)
        print('ll1[n]: ', ll1[n])
        print('ll2[n]: ', ll2[n])
        print('ll1[n] * ll2[n]: ', ll1[n] * ll2[n])
        
        return ll1[n] * ll2[n] 

    print(p(l1,l2,0))
    print(p(l1,l2,1))
    print(p(l1,l2,2))
    
    r = 0 
    for i in range ( len ( l1 ) ) : 
      r += p ( l1 , l2 , i ) 
    return r 


print (dp ( [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ))