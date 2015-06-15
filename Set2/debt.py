


balance = 3329
oBalance = balance
annualInterestRate = 0.2
payment = 0
monthlyInterestRate = annualInterestRate/12.0
while balance > 0:
  payment += 10
  balance = oBalance
  for i in range(12):
    unBalance = balance - payment
    balance = unBalance + monthlyInterestRate * unBalance
print(payment)
