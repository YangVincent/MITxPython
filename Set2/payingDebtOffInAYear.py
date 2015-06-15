

def calcMonthInterest(annualInterestRate):
  return annualInterestRate/12.0
def calcUnpaidBalance(a, b):
  return a-b
def updatedBalance(a, b, c):
  return a+(b*c)
monthlyPayment = 10
balance = 3329
oBalance = balance
annualInterestRate = 0.2
monthlyInterestRate = calcMonthInterest(annualInterestRate)
    
print("Monthly interest rate is " + str(calcMonthInterest(annualInterestRate)))
while balance > 0 and monthlyPayment < 320:
  monthlyPayment += 10
  balance = oBalance
  for i in range(12):
    print("i is " + str(i))
    monthlyUnpaidBalance = calcUnpaidBalance(balance, monthlyPayment)
    balance = updatedBalance(balance, monthlyInterestRate, monthlyUnpaidBalance)
    print("Balance is " + str(balance))
  print("new loop" + str(monthlyPayment))
print(monthlyPayment)








