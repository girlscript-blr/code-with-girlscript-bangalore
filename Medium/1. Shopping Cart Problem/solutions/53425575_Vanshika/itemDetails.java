import java.util.*;
public class itemDetails {
	
	public int getTax(int amt) {
		return (int)(0.06*amt);
	}
public int[] getItemDetails(int q,int itemno) {
	int arr[]=new int[3];
	switch(itemno) {
	case 1:
		arr[0]=1200;
		if(q>=4) {
		arr[1]=899;
		}
		else {
			arr[1]=0;
		}
		arr[2]=150;
		break;
	case 2:
		arr[0]=600;
		if(q>=3) {
			arr[1]=499;
			}
			else {
				arr[1]=0;
			}
		arr[2]=120;
		break;
	case 3:
		arr[0]=1800;
		if(q>=5) {
			arr[1]=1650;
			}
			else {
				arr[1]=0;
			}
		arr[2]=850;
		break;
	case 4:
		arr[0]=1000;
		if(q>=3) {
			arr[1]=800;
			}
			else {
				arr[1]=0;
			}
		arr[2]=350;
		break;
	case 5:
		arr[0]=5990;
		if(q>=2) {
			arr[1]=4500;
			}
			else {
				arr[1]=0;
			}
		arr[2]=900;
		break;
		
	}
	return arr;
}
public String getItemName(int itemno) {
	String name="";
	switch(itemno) {
	case 1:
		name="Basshead earphones";
		break;
	case 2:
		name="Bluetooth computer mouse";
		break;
	case 3:
		name="HP keyboard ";
		break;
	case 4:
		name="Gadget Organiser ";
		break;
	case 5:
		name="Sony Playstation 2 ";
		break;
	}
	return name;
}

}
