def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    ans=min(a,b)
    while(True):
        if(a % ans == 0 and b % ans==0):
            break
        else:        
            ans-=1
    return ans
