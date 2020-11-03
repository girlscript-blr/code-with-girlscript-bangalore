import java.util.*;
public class AppEasy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int n;
		String name,captain,franchise,hg;
		Map<Integer,Details> list=new LinkedHashMap<Integer,Details>();
		System.out.println("Enter the number of teams playing the tournament: ");
		try {
			n=sc.nextInt();
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
		}
		catch(Exception e) {
			System.err.println("Please provide correct value!");
			main(new String[0]);
		}

		for(Map.Entry map:list.entrySet()) {
			System.out.println(map.getKey()+" "+map.getValue());
		}

	}

}
