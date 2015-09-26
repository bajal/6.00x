#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month =
#  (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

balance=1000
annualInterestRate=0.2

monthlyInterestRate=annualInterestRate/12.0

fixPay=10
tempBalance=balance
unPaidBalance=balance

while(True):
    for month in range(1,13):        
        unPaidBalance=tempBalance-fixPay
        tempBalance = unPaidBalance+unPaidBalance*monthlyInterestRate
        #print "Monthly Balance :"+str(month)+":"+str(unPaidBalance)

    print "Remaining balance:" +str(fixPay)+":"+ "%.2f" % tempBalance
    if(tempBalance < 0.1):
        break
    else:
        tempBalance=balance #reset the tempBalance
        fixPay+=10        
        

print "Lowest Payment:" +str(fixPay)


