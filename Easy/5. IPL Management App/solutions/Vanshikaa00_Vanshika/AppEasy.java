import java.util.*;
public class AppEasy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner sc=new Scanner(System.in);
System.out.println("Enter the number of teams playing the tournament: ");
int n=sc.nextInt();
String name,captain,franchise,hg;
Map<Integer,Details> list=new LinkedHashMap<Integer,Details>();
for(int i=0;i<n;i++) {
	System.out.println("Fill team "+(i+1)+" details: ");
	System.out.println("Enter team name: ");
	name=sc.next();
	System.out.println("Enter captain name: ");
	captain=sc.next();
	System.out.println("Enter franchise: ");
	franchise=sc.next();
	System.out.println("Enter home ground: ");
	hg=sc.next();
	list.put(i+1,new Details(name,captain,franchise,hg));
}

for(Map.Entry map:list.entrySet()) {
	System.out.println(map.getKey()+" "+map.getValue());
}

	}

}
