import java.util.*;
import java.lang.*;
import java.time.LocalDate;
import java.time.LocalDateTime; 
import java.time.format.DateTimeFormatter;
public class appEasy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc=new Scanner(System.in);
int choice,age,wt,id=1;
long phone,emgPhone,ht;
String name,gender,bloodType,otherDetails;
LocalDate date;
patientDetails pd;
boolean exit=false;
HashMap<Integer,patientDetails> hs=new HashMap<Integer,patientDetails>();
	System.out.println("**************************WELCOME TO THE APPLICATION************************\n");
	System.out.println("Press 1 to register a new patient");
	System.out.println("Press 2 to update an already existing patient");
	System.out.println("Press 3 to display all patients data");
	System.out.println("Press 4 to display current statistics");
	System.out.println("Press 5 to exit");
	do {
		System.out.println("\nEnter your choice: ");
		choice=sc.nextInt();	
		switch(choice) {
		case 1:
			System.out.println("Enter patient's name: ");
			name=sc.next();
			System.out.println("Enter patient's phone number: ");
			phone=sc.nextLong();
			System.out.println("Enter patient's emergency contact number: ");
			emgPhone=sc.nextLong();
			System.out.println("Enter patient's age : ");
			age=sc.nextInt();
			System.out.println("Enter patient's gender : ");
			gender=sc.next();
			System.out.println("Enter patient's blood type : ");
			bloodType=sc.next();
			System.out.println("Enter patient's  weight: ");
			wt=sc.nextInt();
			System.out.println("Enter patient's  height: ");
			ht=sc.nextLong();
			sc.nextLine();
			System.out.println("Enter patient's  symptoms/medical details: ");
			otherDetails=sc.nextLine();
			pd=new patientDetails(age, wt, ht,phone,emgPhone,  name,gender,bloodType,otherDetails);
			hs.put(id,pd);
			id=id+1;
			System.out.println("Patient registered !! ");
			break;
		case 2:
			System.out.println("Enter patient id you want to update: ");
			int upid=sc.nextInt();
			patientDetails pdd=hs.get(upid);
			System.out.println("What do you want to update?");
			System.out.println("press 1 for changing patient's full name\npress 2 for changing patient's phone number\npress 3 for changing patient's emergency phone number\npress 4 for changing patient's age\npress 5 for changing patient's gender\npress 6 for changing patient's blood type\npress 7 for changing patient's weight\npress 8 for changing patient's height\npress 9 for changing patient's date of admission\npress 10 for changing patient's symptoms / medical details");
			int upchoice=sc.nextInt();
			switch(upchoice) {
			case 1:
				System.out.println("Enter patient's full name:");
				String pname=sc.next();
				pdd.name=pname;
				break;
			case 2:
				System.out.println("Enter patient's phone number: ");
				long pphno=sc.nextLong();
				pdd.phone=pphno;
				break;
			case 3:
				System.out.println("Enter patient's emergency phone number: ");
				long pemgphno=sc.nextLong();
				pdd.emgPhone=pemgphno;
				break;
			case 4:
				System.out.println("Enter patient's age: ");
				int page=sc.nextInt();
				pdd.age=page;
				break;
			case 5:
				System.out.println("Enter patient's gender:");
				String pgen=sc.next();
				pdd.gender=pgen;
				break;
			case 6:
				System.out.println("Enter patient's blood type: ");
				String pbtype=sc.next();
				pdd.bloodType=pbtype;
				break;
			case 7:
				System.out.println("Enter patient's weight: ");
				int pwt=sc.nextInt();
				pdd.wt=pwt;
				break;
			case 8:
				System.out.println("Enter patient's height: ");
				int pht=sc.nextInt();
				pdd.ht=pht;
				break;
			case 9:
				System.out.println("Enter patient's date of admission: ");
				System.out.println("Enter year(in 20xx format): ");
				int y = Integer.parseInt( sc.next() );
				System.out.println("Enter month(01-12): ");
				int m = Integer.parseInt( sc.next() );
				System.out.println("Enter date: ");
				int d = Integer.parseInt( sc.next() );
				LocalDate ld = LocalDate.of( y , m , d );
				pdd.date=ld;
				break;
			case 10:
				System.out.println("Enter patient's symptoms/medical details: ");
				String pdeets=sc.nextLine();
				pdd.otherDetails=pdeets;
				break;
				default:
					System.out.println("Choose correct option!");
			}
			System.out.println("Patient details updated !! ");
			break;
		case 3:
			System.out.println("\n**************************************************PATIENTS RECORD***************************************************\n");
			for(Map.Entry<Integer, patientDetails> entry:hs.entrySet()){    
		        int key=entry.getKey();  
		        patientDetails p=entry.getValue();  
		        System.out.println("PATIENT ID: "+key);
		        System.out.println("PATIENT FULL NAME: "+p.name);
		        System.out.println("PHONE NUMBER: "+p.phone);
		        System.out.println("EMERGENCY CONTACT NUMBER: "+p.emgPhone);
		        System.out.println("AGE: "+p.age);
		        System.out.println("GENDER: "+p.gender);
		        System.out.println("BLOOD TYPE: "+p.bloodType);
		        System.out.println("WEIGHT: "+p.wt);
		        System.out.println("HEIGHT: "+p.ht);
		        System.out.println("DATE OF ADMISSION: "+p.date);
		        System.out.println("SYMPTOMS / MEDICAL DETAILS: "+p.otherDetails);
		        System.out.println("-------------------------------------------------------------------------------------------------------------------");
		    }  
			break;
		case 4:
		int ct=0;
			for(Map.Entry<Integer, patientDetails> entry:hs.entrySet()){    
		        int key=entry.getKey();  
		        patientDetails p=entry.getValue();  
		        LocalDate ld1=LocalDate.now();
		        if(p.date.equals(ld1)) {
		        ct++;
		        }
		    }  
			System.out.println("Total patients admitted today: "+ct);
			System.out.println("Total number of patients in hospital at the current time : "+hs.size());

			break;
		case 5:
			exit=true;
			break;
			default:
				System.out.println("Choose correct operation that you want to perform!!");
		}
	}
	while(exit!=true);
	System.out.println("Thank you for using our application!!");
	}

}
