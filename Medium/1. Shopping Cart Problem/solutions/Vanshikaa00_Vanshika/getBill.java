
import java.text.SimpleDateFormat;
import java.util.*;


public class getBill {

	public void calculatedBill(String name,Long phno,String paymentMethod,HashMap <Integer,Integer> map,int distance,String address,String mode) {
		int tax,q,totalAmt,itemprice,discountprice=0,wt,subtotal=0,amountSaved=0;
		String itemname="";
		itemDetails details=new itemDetails();
		int arr[]=new int[3]; 
		
		System.out.println("\n-------------------------------GENERATED INVOICE-----------------------------------------\n");
		System.out.println("Shop name: GadgetifyWithGSBlr");
		System.out.println("Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India");
		System.out.println("Shop contact no: +91 9988776655\n");
		System.out.println("Customer name: "+name);
		System.out.println("Customer phone number: "+phno);
		System.out.println("PaymentMethod Selected: "+paymentMethod+"\n");
		System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
		for (Map.Entry<Integer, Integer> e : map.entrySet()) 
		{
			int p;
			q=e.getValue();
			arr=details.getItemDetails(q,e.getKey());
			itemname=details.getItemName(e.getKey());
			itemprice=arr[0];
			discountprice=arr[1];
			wt=arr[2];
			System.out.println("  ITEM NAME- "+itemname);
			System.out.println("  QUANTITY- "+q);
			System.out.println("  ITEM PRICE- Rs "+itemprice);
			if(discountprice!=0) {
			System.out.println("  DISCOUNT PRICE- Rs "+discountprice);
			amountSaved+=((itemprice-discountprice)*q);
			}
			System.out.println("  WEIGHT- "+wt+" g");
			System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
			if(discountprice==0) {
				p=itemprice;
			}
			else {
				p=discountprice;
			}
			subtotal=subtotal+(p*q);
		}
		System.out.println("Total amount saved: Rs "+amountSaved+" !");
		tax=details.getTax(subtotal);
		System.out.println("Total tax(6%): Rs "+tax);
		totalAmt=subtotal+tax;
		System.out.println("Sum amount to be paid: Rs "+totalAmt);
		if(mode.equals("h"))
		{
			System.out.println("\nShipping Address: "+address);
			if(distance<=5) {
				System.out.println("Shipping Charges: Free!!");
			}
			else if(distance<=20) {
				System.out.println("Shipping Charges: Rs30/-");
			}
			else if(distance<=50) {
				System.out.println("Shipping Charges: Rs60/-");
			}
			else System.out.println("No delivery");
		}
		SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy  HH:mm:ss");  
		Date date = new Date();  
		System.out.println(formatter.format(date));
		System.out.println("\n---------------------------THANK YOU FOR SHOPPING WITH US! ------------------------\n");

}
}
