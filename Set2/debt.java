


public class debt
{

  public static void main(String[] args)
  {

    double balance = 3329;
    double oBalance = balance;
    double annualInterestRate = 0.2;
    int payment = 0;
    double monthlyInterestRate = annualInterestRate/12.0;
    while (balance > 0)
    {
      payment+=10;
      balance = oBalance;
      for (int i = 0; i < 12; i++)
      {
        double unBalance = balance - payment;
        balance = unBalance + monthlyInterestRate*unBalance; 
      }

    }
    System.out.println("The final thing is " + payment);
  }
}
