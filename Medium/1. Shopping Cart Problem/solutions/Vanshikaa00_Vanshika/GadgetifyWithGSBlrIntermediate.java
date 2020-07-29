import java.util.*;
import java.io.*;
public class GadgetifyWithGSBlrIntermediate {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		getBill g = new getBill();
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		System.out.println(
				"\n---------------------------------------------------WELCOME TO GadgetifyWithGSBlr-----------------------------------------------	");
		System.out.println("\n"
				+ "1. Name: Basshead earphones, Original Price: Rs. 1200, Weight: 150g  ----  Get discount price of Rs. 899 on buying 4 or more!\n"
				+ "2. Name: Bluetooth computer mouse, Original Price: Rs. 600, Weight: 120g  ----  Get discount price of Rs. 499 on buying 3 or more!\n"
				+ "3. Name: HP keyboard, Original Price: Rs. 1800, Weight: 850g  ----  Get discount price of Rs. 1650 on buying 5 or more!\n"
				+ "4. Name: Gadget Organiser, Original Price: Rs. 1000, Weight: 350g  ----  Get discount price of Rs. 800 on buying 3 or more!\n"
				+ "5. Name: Sony Playstation 2, Original Price: Rs. 5990, Weight: 900g  ----  Get discount price of Rs. 4500 on buying 2 or more!");
		System.out.println(
				"----------------------------------------------------------------------------------------------------------------------------------------	");
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
