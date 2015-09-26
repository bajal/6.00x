balance=1000
annualInterestRate=0.2

monthlyInterestRate=annualInterestRate/12.0

fixPay=10
tempBalance=balance
unPaidBalance=balance

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

while(True):
    test = paymentTest(balance, fixPay)
    
    if(test<0.1):
        break
    else:
        fixPay+=10

    print "Remaining balance:" +str(fixPay)+":"+ "%.2f" % test
    
        

print "Lowest Payment:" +str(fixPay)
