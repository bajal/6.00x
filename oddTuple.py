def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    count=0
    oddTups=()
    for i in aTup:
        if(count %2 ==0):
           oddTups= oddTups+ (i,)
        count+=1
    print oddTups
