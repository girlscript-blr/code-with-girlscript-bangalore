import java.util.*;
public class Details {
	String teamname,captain,franchise,homeground;

	public Details(String teamname, String captain, String franchise, String homeground) {
		super();
		this.teamname = teamname;
		this.captain = captain;
		this.franchise = franchise;
		this.homeground = homeground;
	}

	@Override
	public String toString() {
		return "Teamname=" + teamname + ", captain=" + captain + ", franchise=" + franchise + ", homeground="+ homeground ;
	}


	

}
