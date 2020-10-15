import java.util.*;
import java.lang.*;
import java.time.LocalDate; 
import java.time.format.DateTimeFormatter;

public class patientDetails {
	int age,wt;
	long phone,ht,emgPhone;
	String name,gender,bloodType,otherDetails;
	LocalDate date;
	public patientDetails() {}
	public patientDetails(int age, int wt, long ht, long phone, long emgPhone, String name, String gender,
			String bloodType, String otherDetails) {
	
		this.age = age;
		this.wt = wt;
		this.ht = ht;
		this.phone = phone;
		this.emgPhone = emgPhone;
		this.name = name;
		this.gender = gender;
		this.bloodType = bloodType;
		this.otherDetails = otherDetails;
		this.date = LocalDate.now();
	}
	
}
