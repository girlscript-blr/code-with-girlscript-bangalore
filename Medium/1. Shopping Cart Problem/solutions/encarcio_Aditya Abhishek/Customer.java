import java.util.Scanner;

//Class to contain customer details during purchase

public class Customer {
    private String name;
    private long phoneNo;
    private String paymentMethod;
    private String deliveryMode;
    private int homeDistance;
    private String shippingAddress;
    private static Scanner scanner = new Scanner(System.in);

    public Customer(String name, long phoneNo) { // setting customer name and phone number
        this.name = name;
        this.phoneNo = phoneNo;
    }

    public void setPaymentMethod(String paymentMethod) { // setting payment method
        this.paymentMethod = paymentMethod;
    }

    public void setDeliveryMode(boolean deliveryMode) {
        if (deliveryMode) {
            this.deliveryMode = "Home Delivery";
            System.out.println("Please enter the distance of your home (in KMS)");
            this.homeDistance = scanner.nextInt();
            scanner.nextLine();
            System.out.println("Please enter your shipping address");
            this.shippingAddress = scanner.nextLine();
        } else {
            this.deliveryMode = "Takeaway";
        }
    }
    
    public String getDeliveryMode() {
        if(this.deliveryMode.equals("Home Delivery"))
        {
            return this.deliveryMode+"\n"+"Shipping Address: "+this.shippingAddress;
        }
        return this.deliveryMode;
    }
    public int getHomeDistance() {
        return homeDistance;
    }
    @Override
    public String toString() {
        return "Customer Name: " + this.name + "\n" + "Phone No: " + this.phoneNo + "\n" + "Payment Method: "
                + this.paymentMethod + "\n" + "Delivery Mode: " + this.getDeliveryMode();
    }
}