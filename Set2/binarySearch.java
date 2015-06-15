



public class binarySearch
{
  public static void main(String[] args)
  {
    double balance = 320000;
    double annualInterestRate = 0.2;
    double monthlyInterestRate = annualInterestRate/12;
    double lower = balance/12; 
    double upper = balance * Math.pow(1+monthlyInterestRate, 12)/12.0;
    double payment = (lower+upper)/2;
    double oBalance = balance;

    int counter = 0;
    while(Math.abs(lower-upper) >= .2)
    {
      //round balance
//      balance = (int) (balance * 100);
//      balance /= 100;
      System.out.println("lower is " + lower + " upper is " + upper + "\n");
      //round nums
      lower = (int) (lower * 100);
      lower /= 100;
      upper = (int) (upper * 100);
      upper /= 100;
      payment = (lower+upper)/2;
      balance = oBalance;
      for (int i = 0; i < 12; i++)
      {
        double unBalance = balance - payment;
        balance = unBalance + monthlyInterestRate * unBalance;
      }
      if (balance > 0)
        lower = payment;
      else if (balance < 0)
        upper = payment;
      else
        break;
    }
  payment = (lower+upper)/2;
  payment = (int)((payment+0.5)*100);
  payment /= 100;
  System.out.println("Result is " + payment);



  }
}
