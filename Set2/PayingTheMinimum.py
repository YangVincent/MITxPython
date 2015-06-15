



def monthlyInterestRate(annualInterestRate):
  return (annualInterestRate/12.0)
def minimumMonthlyPayment(minimumMonthlyPaymentRate, previousBalance):
  return minimumMonthlyPaymentRate * previousBalance

def monthlyUnpaidBalance(previousBalance, minimumMonthlyPayment):
  return previousBalance - minimumMonthlyPayment
def updatedBalance(monthlyUnpaidBalance, monthlyInterestRate):
  return monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance


balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
su = 0
for i in range(12):
  monthlyInterestRate = annualInterestRate/12.0

  print("Month: " + str(i+1))
  minimumMonthlyPay = minimumMonthlyPayment(monthlyPaymentRate, balance)
  minimumMonthlyPay = round(minimumMonthlyPay, 2)
  print("Minimum monthly payment: " + str(minimumMonthlyPay))
  
  monthlyUnpaidBal = monthlyUnpaidBalance(balance, minimumMonthlyPay)
  balance = monthlyUnpaidBal + monthlyInterestRate * monthlyUnpaidBal
  balance = round(balance, 2)
  print("Remaining balance: " + str(balance))
  su += minimumMonthlyPay

print("Total paid: " + str(su))
print("Remaining balance: " + str(balance))
