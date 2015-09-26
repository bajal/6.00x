balance=320000
annualInterestRate=0.2
#29157.09

monthlyInterestRate=annualInterestRate/12.0

lower = balance/12
upper = (balance * (1+monthlyInterestRate)**12)/12.0 
lowestPayment=(lower+upper)/2.0

numg=0
print "Step 1 Lower "+str(lower)+ ", Upper "+str(upper)+ ",LP "+str(lowestPayment)

def paymentTest(balance, lowestPayment):
    '''
    Returns the balance at the end of the year
    '''
    month = 0
    while month < 12:
         balance = balance - lowestPayment
         interest = balance * monthlyInterestRate
         balance = balance + interest
         month += 1
    return balance

test = paymentTest(balance, lowestPayment)

while (abs(balance - test) >= 10 and numg<10):
    print str(numg)+":"+str(abs(balance - test))
    print "test "+str(test)+", lower:"+str(lower)+", upper:"+str(upper)+",LP:"+str(lowestPayment)
   # print "lowestPayment*12 -test "+str(lowestPayment*12 -test)
   
    if (balance - test) > 0:
         lower = lowestPayment
    else:
         upper = lowestPayment

    lowestPayment = ((upper + lower)/2.0)
    test = paymentTest(balance, lowestPayment)
    
    numg+=1

print "lowestPayment "+str(lowestPayment)
