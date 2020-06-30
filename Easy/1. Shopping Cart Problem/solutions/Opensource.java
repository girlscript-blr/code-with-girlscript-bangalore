
package opensource;

import java.util.HashMap;
import java.util.Scanner;

/**
 *
 * @author nblar
 */
public class Opensource {

   static double sum=0; static String name,phoneNo,payment;
   static HashMap<Integer,Integer> menu=new HashMap<Integer,Integer>();
   
    public static void main(String[] args) {
         
        System.out.println("Welcome to GadgetifyWithGSBlr\nElectronics at your footseps! "+"\nPress 1 to see menu");
        
        Scanner sc=new Scanner(System.in);
        int ch=sc.nextInt();
        if(ch==1) shopping_list();
        System.out.println("Press 7 to enter things you want to want to purchase\nPress 8 to see the purchase list\nPress 9 for the bill");

        ch=sc.nextInt();
        
       if(ch==7) choice();
       else if(ch==8) shopping_list();
       else if(ch==9) System.out.println("Sorry! You need to buy something first, to get the bill. Try Again!");
       else System.out.println("Wrong Choice. Come Again!");
       
    }

    private static void shopping_list() {
        System.out.println("The Items Avavlible in the store are");
        System.out.println("-------------------------------------");
        System.out.println("1.Basshead earphones: Rs. 1200\n" +
        "2.Bluetooth computer mouse: Rs. 600\n"+"3.Mobile Charger: Rs.500\n"+"4.Wireless Keyboard: Rs 1500\n"+"5.Wireless Earphones: Rs.1200\n");
        menu.put(1,1200);
        menu.put(2,600);
        menu.put(3,500);
        menu.put(4,1500);
        menu.put(5,1200);
    }

    private static void choice() { 
        // System.out.println("Press 7 to enter things you want to want to purchase\nPress 8 to see the purchase list\nPress 9 for the bill");
         Scanner sc=new Scanner(System.in);
            
            
        while(true){
            
            System.out.println("State the index of your Purchase");
            int index=sc.nextInt();
            System.out.println("State the quantity");
            int quant=sc.nextInt();
             bill(index,quant);
            System.out.println("Press 9 get the bill\nPress 8 to see the shopping list again\nPress 0 to continue");
            int ch=sc.nextInt();
            switch(ch){
                case 9: display_bill(); break;
                case 8: shopping_list();break;
                case 0: 
            }
            
        }
        
        //System.out.println("Use the format:- (index of your product),quantity");
    }

    private static void bill(int index, int quant) {
        sum+=(menu.get(index)*quant);
    }

    private static void display_bill() {
             System.out.println("Enter Your Name");
              Scanner sc=new Scanner(System.in);
              name=sc.next();
              System.out.println("Enter Your Phone Number");
              phoneNo=sc.next();
              System.out.println("Enter the payment mode (Cash/Card/Online)");
              payment=sc.next();
              
              System.out.println("Thanks you For Shopping at GadgetifyWithGSBlr\n Your bill for the shopping is as follows");
              for (int i = 0; i < 10000; i++);
              
              System.out.println("-------------- BILL -------------------");
              System.out.println("Shop name:- GadgetifyWithGSBlr");
              System.out.println("Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India");
              System.out.println("Shop contact no: +91 9988776655");
              System.out.println("Customer Details are --------------");
              System.out.println("Name:- "+name+"\nPhone Number:- "+phoneNo);
              sum=sum+(0.06*sum);
              System.out.println("Total Amount of purchase is:- "+sum);
              System.out.println("Payemnt Mode:- "+payment);
              System.out.println("Thanks For Your Visit. See You soon \n---------------------------");
              System.exit(0);
            
        
    }
    
}
