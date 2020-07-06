
import java.util.*;
import java.text.SimpleDateFormat;  
import java.util.Date; 
public class GadgetifyWithGSBlr {
	public static double getTaxAmt(int price) {
		return (0.06)*price;
	
	}
	public static int getTotal(int price,int q) {
		return price*q;
	}
public static void calculatedBill(String name,Long phno,String paymentMethod,int itemno,int quantity) {
	int amt=0,price=Integer.MIN_VALUE;
	double taxamt,total;
	String itemname="";
	switch(itemno) {
	case 1:
		price=1200;
		itemname=" Earphones";
		break;
	case 2:
		price=50;
		itemname= "Bread";
		break;
	case 3:
		price=800;
		itemname= "Pizza";
		break;
	case 4:
		price=250;
		itemname= "Chocolate";
		break;
	case 5:
		price=350;
		itemname= "Roohafza";
		break;
	}
	amt=getTotal(price,quantity);
	taxamt=getTaxAmt(amt);
	total=amt+taxamt;
	System.out.println("*****************************************GENERATED BILL*******************************************");
	System.out.println();
	System.out.println("Shop name: GadgetifyWithGSBlr\nShop address: 311/5 Akshay nagar, Bangalore, Karnataka, India\nShop contact no: +91 9988776655\n"
			+ "Customer name: "+name+"\nCustomer phone no: "+phno+"\nYou've bought " +quantity+" "+itemname+" costing Rs "+price+" each\n"
					+ "Total tax amount(6 %): Rs"+taxamt+"\nTotal Amount: Rs"+total+"\nPayment Method used: "+paymentMethod);
	  SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");  
	    Date date = new Date();  
	    System.out.println(formatter.format(date));
	    System.out.println("\n********************************THANK YOU FOR SHOPPING WITH US!!********************");
}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc=new Scanner(System.in);
System.out.println("*******************WELCOME TO GadgetifyWithGSBlr*********************");
System.out.println("\n1. Earphones:Rs 1200\n2. Bread:Rs 50\n3. Pizza:Rs 800\n4. Chocolate:Rs 250\n"
		+ "5. Roohafza:Rs 350\n");
System.out.println("*********************************************************************");
System.out.println("Please enter your name");
String name=sc.next();
System.out.println("Please enter your phone number");
Long phno=sc.nextLong();
System.out.println("Please enter your payment method (cash/card/online)");
String paymentMethod=sc.next();
System.out.println("Select a single shopping item number and it’s quantity");
int itemno=sc.nextInt();
int quantity=sc.nextInt();
System.out.println("Calculating your bill...");
calculatedBill(name,phno,paymentMethod,itemno,quantity);

	}

}
