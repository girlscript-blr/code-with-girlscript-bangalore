import java.util.*;
public class FoodSupplyEasy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.println("*********************WELCOME TO FOOD APP************************");
		String aadhar,name,gender;
		int age,eatricequan,eatdalquan,a1,a2,a3,a4,a5,a6,inp1,inp2,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11;
		q1=q2=q3=q4=q5=q6=q7=q8=q9=q10=q11=0;
		a1=a2=a3=a4=a5=a6=0;
boolean exit=false;
do {
	System.out.println("\nWould you like to fill the survey? Enter Yes/No");
	String choice=sc.next();
	if(choice.equalsIgnoreCase("yes")) {
		System.out.println("Please fill in your details:");
		System.out.println("Enter Aadhar Card Number:");
		aadhar=sc.next();
		System.out.println("Enter name:");
		name=sc.next();
		System.out.println("Enter gender(choose from male,female,others):");
		gender=sc.next();
		System.out.println("Enter age:");
		age=sc.nextInt();
		System.out.println("How much rice in grams you eat per day?:");
		eatricequan=sc.nextInt();
		q1+=eatricequan;
		System.out.println("How much dal in grams you eat per day?:");
		eatdalquan=sc.nextInt();
		q2+=eatdalquan;
		System.out.println("Choose any 2 special food items from the list below: ");
		if(age<=2) {
			a1+=1;
			System.out.println("1. Cerelac \n2. Amul powder\n3. Nandini milk tetra packs\n(Choose their number)");
			System.out.println("Enter choice1: ");
			inp1=sc.nextInt();
			System.out.println("Enter choice2: ");
			inp2=sc.nextInt();
			if(inp1==1) {
				q3+=1;
			}
			else if(inp1==2) {
				q4+=1;
			}
			else if(inp1==3) {
				q5+=1;
			}
			if(inp2==1) {
				q3+=1;
			}
			else if(inp2==2) {
				q4+=1;
			}
			else if(inp2==3) {
				q5+=1;
			}

		}
		else if(age>=3 && age<18) {
			a2+=1;
			System.out.println("1. Bread \n2. Tiger/Parle G\n3. Nandini milk tetra packs\n4. Canned Fruits\n5. Canned Veggies\n(Choose their number)");
			System.out.println("Enter choice1: ");
			inp1=sc.nextInt();
			System.out.println("Enter choice2: ");
			inp2=sc.nextInt();
			if(inp1==1) {
				q6+=1;
			}
			else if(inp1==2) {
				q7+=1;
			}
			else if(inp1==3) {
				q5+=1;
			}
			else if(inp1==4) {
				q9+=1;
			}
			else if(inp1==5) {
				q8+=1;
			}

			if(inp2==1) {
				q6+=1;
			}
			else if(inp2==2) {
				q7+=1;
			}
			else if(inp2==3) {
				q5+=1;
			}
			else if(inp2==4) {
				q9+=1;
			}
			else if(inp2==5) {
				q8+=1;
			}
		}
		else if(age>70) {
			a3+=1;
			System.out.println("1. Canned Fruits\n2. Canned Veggies\n3. Nandini Milk TetraPacks\n4. Medicine Packs\n(Choose their number)");
			System.out.println("Enter choice1: ");
			inp1=sc.nextInt();
			System.out.println("Enter choice2: ");
			inp2=sc.nextInt();
			if(inp1==1) {
				q9+=1;
			}
			else if(inp1==2) {
				q8+=1;
			}
			else if(inp1==3) {
				q5+=1;
			}
			else if(inp1==4) {
				q10+=1;
			}
			if(inp2==1) {
				q9+=1;
			}
			else if(inp2==2) {
				q8+=1;
			}
			else if(inp2==3) {
				q5+=1;
			}
			else if(inp2==4) {
				q10+=1;
			}
		}
		else {
			if(gender.equalsIgnoreCase("female")) {
				a4+=1;
				System.out.println("1. Canned Fruits\n2. Canned Veggies\n3. Nandini Milk TetraPacks\n4. Calcium Sandoz Tablets\n(Choose their number)");
				System.out.println("Enter choice1: ");
				inp1=sc.nextInt();
				System.out.println("Enter choice2: ");
				inp2=sc.nextInt();
				if(inp1==1) {
					q9+=1;
				}
				else if(inp1==2)
				{
					q8+=1;
				}
				else if(inp1==3) {
					q5+=1;
				}
				else if(inp1==4) {
					q11+=1;
				}
				if(inp2==1) {
					q9+=1;
				}
				else if(inp2==2)
				{
					q8+=1;
				}
				else if(inp2==3) {
					q5+=1;
				}
				else if(inp2==4) {
					q11+=1;
				}
			}
			else if(gender.equalsIgnoreCase("male")) {
				a5+=1;
				System.out.println("1. Canned Fruits\n2. Canned Veggies\n3. Nandini Milk TetraPacks\n(Choose their number)");
				System.out.println("Enter choice1: ");
				inp1=sc.nextInt();
				System.out.println("Enter choice2: ");
				inp2=sc.nextInt();
				if(inp1==1) {
					q9+=1;
				}
				else if(inp1==2)
				{
					q8+=1;
				}
				else if(inp1==3) {
					q5+=1;
				}

				if(inp2==1) {
					q9+=1;
				}
				else if(inp2==2)
				{
					q8+=1;
				}
				else if(inp2==3) {
					q5+=1;
				}

			}
			else if(gender.equalsIgnoreCase("others")) {
				a6+=1;
				System.out.println("1. Canned Fruits\n2. Canned Veggies\n3. Nandini Milk TetraPacks\n4. Calcium Sandoz Tablets\n(Choose their number)");
				System.out.println("Enter choice1: ");
				inp1=sc.nextInt();
				System.out.println("Enter choice2: ");
				inp2=sc.nextInt();
				if(inp1==1) {
					q9+=1;
				}
				else if(inp1==2)
				{
					q8+=1;
				}
				else if(inp1==3) {
					q5+=1;
				}
				else if(inp1==4) {
					q11+=1;
				}
				if(inp2==1) {
					q9+=1;
				}
				else if(inp2==2)
				{
					q8+=1;
				}
				else if(inp2==3) {
					q5+=1;
				}
				else if(inp2==4) {
					q11+=1;
				}
			}
		}	
		System.out.println("-------------------------------THANK YOU FOR FILLING SURVEY !------------------------------");
	}
	else {
		exit=true;
	}
}
while(exit==false);
float kq1=(float)q1/1000;
float kq2=(float)q2/1000;
System.out.println("PERSON INFO: ");
System.out.println("-------------------------------------------------------------------------");

System.out.println("|                AGE GROUP              | 	NO.OF PEOPLE		|");
System.out.println("-------------------------------------------------------------------------");
System.out.println("| Infants: Below 2years	                |		"+a1+"		|");
System.out.println("| Children: Between 3 to 18 years       |		"+a2+"		|");
System.out.println("| Old Age: Above 70 years               |		"+a3+"		|");
System.out.println("| Adult Female: Between 18 to 69 years  |		"+a4+"		|");
System.out.println("| Adult Male: Between 18 to 69 years    |		"+a5+"		|");
System.out.println("| Adult Other: Between 18 to 69 years   |		"+a6+"		|");
System.out.println("-------------------------------------------------------------------------");


System.out.println("\nFOOD INFO: ");
System.out.println("-----------------------------------------------------------------");
System.out.println("|	FOOD ITEM            	| 	   REQUIRED QUANTITY    |");
System.out.println("-----------------------------------------------------------------");
System.out.println("| Rice in Kg per day            |		"+kq1+"		|");
System.out.println("| Dal in Kg per day	        |		"+kq2+"		|");
System.out.println("| Cerelac                       |		"+q3+"		|");
System.out.println("| Amul powder                   |		"+q4+"		|");
System.out.println("| Nandini Milk TetraPacks	|		"+q5+"		|");
System.out.println("| Bread                         |		"+q6+"		|");
System.out.println("| Tiger/Parle G Biscuits	|		"+q7+"		|");
System.out.println("| Canned Veggies                |		"+q8+"		|");
System.out.println("| Canned Fruits                 |		"+q9+"		|");
System.out.println("| Medicine Packs                |		"+q10+"		|");
System.out.println("| Calcium Sandoz Tablets	|		"+q11+"		|");
System.out.println("-----------------------------------------------------------------");
	}

}
