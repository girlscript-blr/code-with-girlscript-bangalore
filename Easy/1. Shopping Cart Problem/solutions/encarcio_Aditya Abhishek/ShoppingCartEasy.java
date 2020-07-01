import java.util.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ShoppingCartEasy {
    private String shopName;
    private String address;
    private String contactNo;
    private Customer customer;
    private String choosenItem;
    private int quantity;
    private double totalAmount;
    private double tax;
    private static Scanner scanner = new Scanner(System.in);

    private static Map<String, Integer> shopItems = new HashMap<String, Integer>();

    public ShoppingCartEasy() {
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
        shopItems.put("basshead earphones", 1200);
        shopItems.put("bluetooth computer mouse", 600);
        shopItems.put("computer monitor", 500);
        shopItems.put("smart watch", 1600);
        shopItems.put("bluetooth speakers", 1800);
    }

    public void getItemMenu() // method to get Item menu
    {
        System.out.println("List of Items and their prices");
        for (String item : shopItems.keySet()) {
            System.out.println(item.toUpperCase() + " : Rs." + shopItems.get(item));
        }
    }

    public void fillCustomerDetails() // method to enter customer details
    {
        System.out.println("Enter Your Name:");
        String name = scanner.next();
        System.out.print("Enter Your Phone Number:");
        String number = scanner.next();
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

    }

    public void chooseItem() // Choosen Item and its quantity;
    {
        System.out.print("\n");
        System.out.println("Please enter the name of any one item among the list of items from menu");
        this.choosenItem = scanner.nextLine();
        this.choosenItem = this.choosenItem.toLowerCase();
        System.out.println("Enter quantity of choosen item");
        this.quantity = scanner.nextInt();
    }

    public void calculatePayment() { // calcuating payment
        this.totalAmount = shopItems.get(this.choosenItem) * this.quantity;
        this.tax = 0.06 * totalAmount;
    }

    public void generateBill() { // generating bill
        this.fillCustomerDetails();
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
        System.out.println(this.customer.toString());
        System.out.println("Item Bought: " + this.choosenItem);
        System.out.println("Item Quantity: " + this.quantity);
        System.out.println("Total Tax: Rs." + this.tax);
        System.out.println("Sum amount to be paid: Rs." + (this.totalAmount + this.tax));
        System.out.println("Billing Date:" + this.billTime().split(" ")[0]);
        System.out.println("Billing Date:" + this.billTime().split(" ")[1]);
    }

    public static void main(String[] args) {
        System.out.println("-----Welcome to GadgetifyWithGSBlr---");
        System.out.print("\n");
        ShoppingCartEasy cart = new ShoppingCartEasy();
        cart.getItemMenu();
        cart.chooseItem();
        cart.generateBill();
        cart.printBill();
    }
}