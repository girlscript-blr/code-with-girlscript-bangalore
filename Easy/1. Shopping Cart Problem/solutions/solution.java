import java.util.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class solution
{
    public static void main(String args[])
      throws InterruptedException {
        try{
          Scanner input = new Scanner(System.in);
          String[] products={"JBL Headphones","Bose Speakers","Oneplus Monitor","Sony Home Theatre"};
          int[] price={5000,9900,25000,35000,85000};
          String[] payment={"cash","card","online"};
          LocalDateTime now = LocalDateTime.now();
          DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");

          String shopName = "GadgetifyWithGSBlr";
          String address = "311/5 Akshay nagar, Bangalore, Karnataka, India";
          String contact = "+91 9988776655";

          System.out.println("\tWelcome to Gadgetify With GirlScript Bangalore!\t\n");
          System.out.println("\t\tShop name: GadgetifyWithGSBlr\n\t\tShop address: 311/5 Akshay nagar,\n\t\t\t Bangalore, Karnataka,\n\t\t\t India\n\t\tShop contact no: +91 9988776655\n");

          System.out.println("\nPlease tell us your name: ");
          String name = input.nextLine() ;
          System.out.println("\nHey there "+ name+" Welcome to the shop.");
          System.out.println("\nPlease feed in your phone number: ");
          long number = input.nextLong();
          System.out.println("\nPick your payment method:\n\t\tHit 0 for Cash\t\tHit 1 for Card\t\tHit 2 for Online payment");
          int pay = input.nextInt();
          System.out.println("\nPlease pick an item: ");
          for(int i = 0; i < products.length; i++){
            System.out.println("\tHit "+i+" for " + products[i] + " Rs. " + price[i]);
          }
          int prod = input.nextInt();
          System.out.println("\nQuantity of "+ products[prod]+": ");
          int quantity = input.nextInt();
          System.out.println("\n\t\t\t\t\t\t x----- Billing-----X\n");
          //Thread.sleep(2000);

          System.out.println("Date Time:"+ dtf.format(now));
          System.out.print("\n\tCustomer Name : "+ name);
          System.out.println("\tContact Number : "+ number);
          System.out.print("\n\tProduct\t\t\t\tQuantity\t\tPrice\t\t\tTotal Price");
          System.out.println("\n\t"+ products[prod] + "\t\t\t" + quantity+ "\t\t\t" + price[prod] + "\t\t\t" + price[prod]*quantity);
          System.out.println("\n\t\t\t total payable amount after tax :" + 1.06*price[prod]*quantity);
          System.out.println("\tPayment Method: " + payment[pay]);
          System.out.println("\n\n\t\t\t\tThank you for shopping with us <3\n\t\t\t\t\t" + shopName +"\n\t\t\t" + address +"\n\t\t\t\t\t" + contact);
        }
        catch (Exception e) {
          System.out.println("Something went wrong. Byee");
        }

    }
}
