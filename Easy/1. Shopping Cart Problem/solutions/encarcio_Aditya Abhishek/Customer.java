//Class to contain customer details during purchase

public class Customer {
    private String name;
    private String phoneNo;
    private String paymentMethod;

    public Customer(String name, String phoneNo) { // setting customer name and phone number
        this.name = name;
        this.phoneNo = phoneNo;
    }

    public void setPaymentMethod(String paymentMethod) { // setting payment method
        this.paymentMethod = paymentMethod;
    }

    @Override
    public String toString() {
        return "Customer Name: " + this.name + "\n" + "Phone No: " + this.phoneNo + "\n" + "Payment Method: "
                + this.paymentMethod;
    }
}