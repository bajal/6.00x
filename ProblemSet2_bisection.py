#balance=320000
balance=999999
annualInterestRate=0.18
#29157.09

monthlyInterestRate=annualInterestRate/12.0

low = balance/12.0
high = (balance * (1+monthlyInterestRate)**12)/12.0 
fixPay=(low+high)/2.0

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

test = paymentTest(balance, fixPay)

numg=0


while(abs(test) > .01):
    #print "guess :"+str(numg)+" Lo "+str(low)+" Hi "+str(high) + " Test "+str(test)+" fp "+str(fixPay)    
    if(test>0):
        low=fixPay
    else:
        high=fixPay
    fixPay=(low+high)/2.0
    test = paymentTest(balance, fixPay)
    
    numg+=1

print "Lowest Payment: "+"%.2f" % fixPay
