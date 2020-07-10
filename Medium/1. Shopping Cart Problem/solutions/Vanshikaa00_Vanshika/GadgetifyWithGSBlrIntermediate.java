import java.util.*;
import java.io.*;

public class GadgetifyWithGSBlrIntermediate {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		getBill g = new getBill();
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		System.out.println(
				"\n------------------------------WELCOME TO GadgetifyWithGSBlr---------------------------------	");
		System.out.println("\n"
				+ "1. Name: Basshead earphones, Original Price: Rs. 1200, Discount price: Rs. 899, Weight: 150g\n"
				+ "2. Name: Bluetooth computer mouse, Original Price: Rs. 600, Discount price: Rs. 499, Weight: 120g\n"
				+ "3. Name: HP keyboard, Original Price: Rs. 1800, Discount price: Rs. 1650, Weight: 850g\n"
				+ "4. Name: Gadget Organiser, Original Price: Rs. 1000, Discount price: Rs. 800, Weight: 350g\n"
				+ "5. Name: Sony Playstation 2, Original Price: Rs. 5990, Discount price: Rs. 4500, Weight: 900g");
		System.out.println(
				"---------------------------------------------------------------------------------------------	");
		System.out.println("*Enter your name: ");
		String name = sc.next();
		System.out.println("*Enter your phone number: ");
		Long phno = sc.nextLong();
		System.out.println("*Enter your payment method (cash/card/online): ");
		String paymentMethod = sc.next();
		System.out.println("*Enter number of items you want to buy: ");
		int i, n = sc.nextInt();
		int itemno, quantity, distance;
		String address = "";
		for (i = 0; i < n; i++) {
			System.out.println("*Enter number of item " + (i + 1) + " you want to buy: ");
			itemno = sc.nextInt();
			System.out.println("*Enter quantity of item " + (i + 1) + " you want to buy: ");
			quantity = sc.nextInt();
			map.put(itemno, quantity);
		}
		System.out.println("*Do you want to takeaway or do home delivery?(Choose t/h)");
		String mode = sc.next();
		// Distance from shop to the delivery address in KM. (if Home delivery is
		// selected)
		if (mode.equals("h")) {
			System.out.println("*Enter Distance from shop to the delivery address in KM: ");
			distance = sc.nextInt();
			System.out.println("*Enter shipping address: ");
			address = sc.next();
		} else {
			distance = 0;
			address = null;
		}
		System.out.println("\nGenerating your Bill, please wait.....\n");
		g.calculatedBill(name, phno, paymentMethod, map, distance, address,mode);
	}

}
