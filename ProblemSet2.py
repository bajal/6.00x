#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal

balance=4842
annualInterestRate=0.2
monthlyPaymentRate=0.04

unPaidBalance=5000
totalAmountPaid=0

for month in range(1,13):
    print "Month: "+str(month)
    minMonthlyPayment=balance*monthlyPaymentRate
    print "Minimum monthly payment: " + "%.2f" % minMonthlyPayment

    totalAmountPaid+=minMonthlyPayment

    unPaidBalance=balance-minMonthlyPayment
    monthlyInterest=unPaidBalance*annualInterestRate/12
    
    balance=unPaidBalance+monthlyInterest

    print "Remaining balance:" + "%.2f" % balance
    
print "Total Paid : " + "%.2f" % totalAmountPaid
print "Remaining Balance: "+ "%.2f" % balance
