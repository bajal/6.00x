def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    lo=0
    hi=len(aStr)
    mi=len(aStr)/2
        
    if aStr=='':
         return False
    elif char == aStr[mi]:         
         return True        
    elif char > aStr[mi]:
         #print "greater "+str(mi)+ " " +aStr[mi+1:hi]
         return isIn(char,aStr[mi+1:hi]) 
    elif char < aStr[mi]:
         #print "lower "+str(mi)  +" "+aStr[lo:mi]
         return isIn(char,aStr[lo:mi])    
    else:
         return False
            

