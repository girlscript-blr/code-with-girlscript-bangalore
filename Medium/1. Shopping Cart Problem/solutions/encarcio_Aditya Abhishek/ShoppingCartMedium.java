import java.util.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ShoppingCartMedium {
    private String shopName;
    private String address;
    private String contactNo;
    private Customer customer;
    private String choosenItem;
    private int choosenItemIndex;
    private int quantity;
    private double totalAmount;
    private double shippingCharge = 0;
    private double amountSaved = 0;
    private double tax;
    private int deliveryChoice = 0;
    private static Scanner scanner = new Scanner(System.in);

    private Map<Integer, Integer> choosenItems = new HashMap<Integer, Integer>();
    private Map<Integer, ShopItem> shoppingItems = new HashMap<Integer, ShopItem>();

    public ShoppingCartMedium() {
        this.shopName = "GadgetifyWithGSBlr";
        this.address = "311/5 Akshay nagar, Bangalore, Karnataka, India";
        this.contactNo = "+91 9988776655";
        this.fillItemPrices();
    }

    public void shopInfo() { // Shop Information
        System.out.println("Shop Name: " + this.shopName);
        System.out.println("Shop Address: " + this.address);
        System.out.println("Shop Contact No: " + this.contactNo);
    }

    public void fillItemPrices() // method to make a menu of shopping items with their prices
    {
        shoppingItems.put(1, new ShopItem("Basshead Earphones", 1200, 1000, 100));
        shoppingItems.put(2, new ShopItem("Bluetooth Computer mouse", 600, 400, 150));
        shoppingItems.put(3, new ShopItem("Computer Monitor", 500, 500));
        shoppingItems.put(4, new ShopItem("Smart Watch", 1600, 50));
        shoppingItems.put(5, new ShopItem("Bluetooth Speakers", 1800, 700));
    }

    public void getItemMenu() // method to get Item menu
    {
        System.out.println("List of Items and their prices");
        int index = 1;
        for (ShopItem item : shoppingItems.values()) {
            System.out.println(index + "." + item.toString());
            index += 1;
        }
    }

    public void fillCustomerDetails() // method to enter customer details
    {
        String name = "";
        long number = 0;
        System.out.println("Enter Your Name:");
        name += scanner.nextLine();
        System.out.print("Enter Your Phone Number:");
        boolean flag=false;
        while (!flag) {
            try {
                number = scanner.nextLong();
                scanner.nextLine();
                flag=true;
            } catch (Exception e) {
                System.out.println("Please enter a valid number");
                scanner.next();
            } 
        }

        this.customer = new Customer(name, number);
        System.out.print("\n");
        System.out.println(
                "Choose payment method\n1.cash\n2.card\n3.online\nPlease enter the number assigned to the method above to choose it");
        int choice = scanner.nextInt();

        while (!(choice == 1 || choice == 2 || choice == 3)) {
            System.out.println("Please choose again");
            choice = scanner.nextInt();
        }

        switch (choice) { // choosing payment method
            case 1:
                this.customer.setPaymentMethod("cash");
                break;
            case 2:
                this.customer.setPaymentMethod("card");
                break;
            case 3:
                this.customer.setPaymentMethod("online");
                break;
            default:
                break;
        }
        System.out.println("Choose your delivery method\n1.Home Delivery\n2.Takeway");
        this.deliveryChoice = scanner.nextInt();

        while (!(this.deliveryChoice == 1 || this.deliveryChoice == 2)) {
            System.out.println("Please choose again");
            this.deliveryChoice = scanner.nextInt();
        }
        if (this.deliveryChoice == 1) {
            this.customer.setDeliveryMode(true);
        } else {
            this.customer.setDeliveryMode(false);
        }

    }

    public void chooseItem() // Choosen Item and its quantity;
    {
        System.out.print("\n");
        boolean stillChoosing = true;
        String answer = "";
        while (stillChoosing) {
            System.out.println("Please enter the item number of items among the list of items from menu");
            this.choosenItemIndex = scanner.nextInt();
            while (!(this.choosenItemIndex >= 1 && this.choosenItemIndex <= 5)) {
                System.out.println("Invalid Item Number\nPlease enter again");
                this.choosenItemIndex = scanner.nextInt();
            }
            System.out.println("Enter quantity of choosen item");
            this.quantity = scanner.nextInt();
            scanner.nextLine();
            if (this.choosenItems.containsKey(this.choosenItemIndex)) {
                this.choosenItems.put(this.choosenItemIndex,
                        this.choosenItems.get(this.choosenItemIndex) + this.quantity);
            } else {
                this.choosenItems.put(this.choosenItemIndex, this.quantity);
            }
            System.out.println("Do you want to choose more? (Y/N)");
            answer = scanner.nextLine();
            if (answer.equals("n") || answer.equals("N") || answer.equals("no") || answer.equals("NO")
                    || answer.equals("No"))
                stillChoosing = false;
        }
    }

    public String shippingCharge() {
        String charge = "";
        if (this.customer.getHomeDistance() <= 5) {
            charge += "Free";
            this.shippingCharge = 0;
        } else if (this.customer.getHomeDistance() > 5 && this.customer.getHomeDistance() <= 20) {
            charge += 30;
            this.shippingCharge = 30;
        } else if (this.customer.getHomeDistance() > 20 && this.customer.getHomeDistance() <= 50) {
            charge += 60;
            this.shippingCharge = 60;
        } else {
            System.out.println("No delivery is possible");
            System.exit(0);
        }
        return charge;
    }

    public void calculatePayment() { // calcuating payment
        double originalAmount = 0;
        for (int index : choosenItems.keySet()) {
            if (shoppingItems.get(index).getDiscountPrice() != 0) {
                this.totalAmount += (shoppingItems.get(index).getDiscountPrice()) * this.choosenItems.get(index);
            } else {
                this.totalAmount += (shoppingItems.get(index).getOriginalPrice()) * this.choosenItems.get(index);
            }
            originalAmount += (shoppingItems.get(index).getOriginalPrice()) * this.choosenItems.get(index);
        }
        this.amountSaved = originalAmount - this.totalAmount;
        this.totalAmount += this.shippingCharge;
        this.tax = 0.06 * totalAmount;
    }

    public void generateBill() { // generating bill
        this.fillCustomerDetails();
        if (this.deliveryChoice == 1) {
            this.shippingCharge();
        }
        this.calculatePayment();
    }

    public String billTime() { // generating bill date and time
        LocalDateTime dateObj = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        String formattedDate = dateObj.format(formatter);
        return formattedDate;
    }

    public void printBill() // printling bill
    {
        System.out.println("-----Shopping Bill-------");
        this.shopInfo();
        int quantity = 0;
        System.out.println(this.customer.toString());
        System.out.println("Items Bought");
        for (int index : choosenItems.keySet()) {
            ShopItem item = this.shoppingItems.get(index);
            this.choosenItem = item.getName();
            quantity = this.choosenItems.get(index);
            System.out.println("Item Bought: " + this.choosenItem + ", Item Quantity: " + quantity
                    + ", Original Price: " + item.getOriginalPrice() + ", Discount Price: " + item.getDiscountPrice());
        }
        if (this.deliveryChoice == 1) {
            System.out.println("Shipping Charge: Rs." + this.shippingCharge());
        }
        System.out.println("Total Tax: Rs." + this.tax);
        System.out.printf("Amount Saved: Rs. %.2f\n", this.amountSaved);
        System.out.println("Sum amount to be paid: Rs." + (this.totalAmount + this.tax));
        System.out.println(
                "Billing Date:" + this.billTime().split(" ")[0] + ", Billing Time:" + this.billTime().split(" ")[1]);
    }

    public static void main(String[] args) {
        System.out.println("-----Welcome to GadgetifyWithGSBlr---");
        System.out.print("\n");
        ShoppingCartMedium cart = new ShoppingCartMedium();
        cart.getItemMenu();
        cart.chooseItem();
        cart.generateBill();
        cart.printBill();
    }
}