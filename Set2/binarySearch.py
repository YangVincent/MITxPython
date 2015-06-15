


balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
lower = balance/12
upper = balance * pow(1 + monthlyInterestRate, 12)/12.0;
payment = (lower + upper)/2
oBalance = balance

while abs(lower-upper) >= .2:
  payment = (lower + upper)/2
  balance = oBalance
  for i in range(12):
    unBalance = balance - payment
    balance = unBalance + monthlyInterestRate * unBalance
  if balance > 0:
    lower = payment
  elif balance < 0:
    upper = payment
  else:
    break
payment = (lower+upper)/2
payment = round(payment, 2)
print(payment)



