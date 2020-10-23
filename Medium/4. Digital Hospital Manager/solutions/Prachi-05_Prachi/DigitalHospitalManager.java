/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package digitalhospitalmanager;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.*;
import java.util.Scanner;

/**
 *
 * @author Prachi
 */
public class DigitalHospitalManager {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);        
        System.out.println("DIGITAL HOSPITAL MANAGEMENT");
        char ch = '1';
        while(ch=='1' || ch=='2' || ch=='3' || ch=='4'){
            System.out.println("1. Add Patient\n2. Update Patient Data\n3. Fetch All Patient Records\n4.Fetch Patient Data\n Press any key to exit\nEnter choice:");
            ch=in.next().charAt(0);
            try{
                switch(ch){
                    case '1': readPatientData(); break;
                    case '2': 
                        System.out.print("\nEnter Patient ID: ");
                        updateData(in.nextInt());break;
                    case '3': fetchPatients();break; 
                    case '4': 
                        System.out.print("\nEnter Patient ID: ");
                        fetchPatient(in.nextInt());break;
                }
            }
            catch(IOException e){
                e.printStackTrace();
            }
            
        }
        
    }
    static void updateData(int id) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Connection con;
        Statement stmt;
        ResultSet rs;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/digitalhospitalmanager", "root", "alohomora");
            stmt = con.createStatement();
            int ch=1;
            while(ch!=0){
                System.out.println("\nUpdate:\n1.Medical details/comments\n2.Discharge Date\n3.Discharge comment\n4.Death date\n0.Done ");
                ch = Integer.parseInt(in.readLine());
                switch(ch){
                    case 1: System.out.println("Medical details/comments: "); 
                            String medicaldetails = in.readLine();
                            stmt.execute("Update PatientRecord set medicaldetails='"+medicaldetails+"' where PatientID="+id);
                            System.out.println("Update successful");
                    break;
                    case 2: System.out.println("Discharge Date: "); 
                            String dischargedate = in.readLine();
                            stmt.execute("Update PatientRecord set dischargedate="+dischargedate+" where PatientID="+id);
                            System.out.println("Update successful");
                    break;
                    case 3: System.out.println("Discharge comment: "); 
                            String dischargecomments = in.readLine();
                            stmt.execute("Update PatientRecord set dischargecomments='"+dischargecomments+"' where PatientID="+id);
                            System.out.println("Update successful");
                    break;
                    case 4: System.out.println("Death date: "); 
                            String deathdate = in.readLine();
                            stmt.execute("Update table PatientRecord set deathdate="+deathdate+" where PatientID="+id);
                            System.out.println("Update successful");
                    break;
                }
            }
            
            con.close();
        } catch (ClassNotFoundException | SQLException ex) {
            ex.printStackTrace();
        }
        
    }
    static void fetchPatient(int id){
        Connection con;
        Statement stmt;
        ResultSet rs;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/digitalhospitalmanager", "root", "alohomora");
            stmt = con.createStatement(
                ResultSet.TYPE_SCROLL_INSENSITIVE, 
                ResultSet.CONCUR_READ_ONLY
            );
            rs = stmt.executeQuery("SELECT * FROM PatientRecord where PatientID = "+id);
            if(rs.next()){
                System.out.println("Patient Name: "+rs.getString(2)+"\nPhone Number: "+rs.getString(3)+
                        "\nEmergency Contact Number: "+rs.getString(4)+"\nAge: "+rs.getInt(5)+"\nGender: "+rs.getString(6)+
                        "\nBlood Type: "+rs.getString(7)+"\nWeight: "+rs.getFloat(8)+"\nHeight: "+rs.getFloat(9)+
                        "\nSymptoms: "+rs.getString(10)+"\nSeverity: "+rs.getString(12)+"\nMedical Details: "+rs.getString(13)+
                        "nDate of Admission: "+rs.getTimestamp(11)+"\nDate of Discharge: "+rs.getDate(14)+
                        "\nDischarge comments: "+rs.getString(16)+"\nDate and Time of Death(If Deceased): "+rs.getTimestamp(15));
            }
            else{
                System.out.println("\nInvalid Patient ID");
            }
            rs.close();
            con.close();
            
        } catch (ClassNotFoundException | SQLException ex) {
            ex.printStackTrace();
        }
    }
    static void fetchPatients(){
        Connection con;
        Statement stmt;
        ResultSet rs;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/digitalhospitalmanager", "root", "alohomora");
            stmt = con.createStatement(
                ResultSet.TYPE_SCROLL_INSENSITIVE, 
                ResultSet.CONCUR_READ_ONLY
            );
            rs = stmt.executeQuery("SELECT count(*) as count from PatientRecord");
            rs.next();
            System.out.println("Total number of patients: "+ rs.getInt("count"));
            rs = stmt.executeQuery("SELECT count(*) as count from PatientRecord where admissiondate = curDate() ");
            rs.next();
            System.out.println("Total number of patients currently admitted: "+ rs.getInt("count"));
            rs = stmt.executeQuery("SELECT count(*) as count from PatientRecord where dischargedate = curDate() ");
            rs.next();
            System.out.println("Total number of patients currently admitted: "+ rs.getInt("count"));
            rs = stmt.executeQuery("SELECT * FROM PatientRecord");
            if(rs.next()){
                rs.previous();
                System.out.println("Patient ID\tPatient Name\tPhone Number\tEmergency Contact Number\t"
                        + "Age\tGender\tBlood Type\tWeight\tHeight\tSymptoms\t\t\t\tSeverity\t\tMedical Details\t\tDate of Admission\t\tDate of Discharge\t\tDischarge comments\t\tDate and Time of Death(If Deceased)");
                while(rs.next()){
                    System.out.println(rs.getInt(1)+"\t\t"+rs.getString(2)+"\t\t"+rs.getString(3)+"\t\t"+rs.getString(4)
                    +"\t\t"+rs.getInt(5)+"\t"+rs.getString(6)+"\t"+rs.getString(7)+"\t\t"+rs.getFloat(8)+"\t"+rs.getFloat(9)
                    +"\t"+rs.getString(10)+"\t\t"+rs.getString(12)+"\t\t"+rs.getString(13)+"\t\t"+rs.getTimestamp(11)+"\t\t"+rs.getDate(14)+"\t\t"+rs.getString(16)+"\t\t"+rs.getTimestamp(15)+"\t\t");                  

                }
            }
            else{
                System.out.println("No patient records found.");
            }
            rs.close();
            con.close();
            
        } catch (ClassNotFoundException | SQLException ex) {
            ex.printStackTrace();
        }
    }
    static void readPatientData() throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("\nPatient Name: ");
        String name = in.readLine();
        System.out.print("\nPhone number: ");
        String phone = in.readLine();
        System.out.print("\nEmergency Contact: ");
        String emergency = in.readLine();
        System.out.print("\nAge: ");
        int age = Integer.parseInt(in.readLine());
        int ageCategory=0;
        if(age > 0 && age<16) ageCategory = 1;
        else if(age >= 16 && age<=45) ageCategory = 2;
        else ageCategory = 3;
        System.out.print("\nGender: ");
        String gender = in.readLine();
        System.out.print("\nBlood type: ");
        String blood = in.readLine();
        System.out.print("\nWeight: ");
        float weight = Float.parseFloat(in.readLine());
        System.out.print("\nHeight: ");
        float height = Float.parseFloat(in.readLine());
        int ch=1; String symptoms="";
        while(ch!=0){
            System.out.println("\nSymptoms:\n1.Fever\t2.Headache\t3.Fatigue and weakness\n4.Stuffy/runny nose\t5.Sneezing\t6.Sore Throat\n7.Cough\t8.Shortness of breath\t9. Bluish lips of face\n10.Constant pain or pressure in your chest\t0.Done ");
            ch = Integer.parseInt(in.readLine());
            switch(ch){
                case 1: symptoms+="Fever, "; break;
                case 2: symptoms+="Headache, "; break;
                case 3: symptoms+="Fatigue and weekness, "; break;
                case 4: symptoms+="Stuffy/runny nose, "; break;
                case 5: symptoms+="Sneezing , "; break;
                case 6: symptoms+="Sore Throat, "; break;
                case 7: symptoms+="Cough, "; break;
                case 8: symptoms+="Shortness of breath, "; break;
                case 9: symptoms+="Bluish lips or face, "; break;
                case 10: symptoms+="Constant pain or pressure in your chest, "; break;
            }
        }
        String[] sym = symptoms.split(",");
        symptoms= symptoms.substring(0, symptoms.length()-2);
        System.out.print("\nMedical Details/comments: ");
        String comments = in.readLine();
        addPatientDB(name,phone,emergency,age,ageCategory,gender,blood,weight,height,symptoms,sym,comments);
    }
    static void addPatientDB(String name, String phone, String emergency,
            int age,int ageCat, String gender,String blood, float weight, float height, String symptoms, String sym[],String comments){
        Connection con;
        Statement stmt;
        ResultSet rs;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/digitalhospitalmanager", "root", "alohomora");
            stmt = con.createStatement();
            String severity="";
            for(String i:sym){
                rs = stmt.executeQuery("SELECT severity FROM symptomsdetails where ageCategory = "+ageCat+" and symptom='"+i.trim()+"'");
                if(rs.next())
                    severity += rs.getString("severity")+", ";
            }
            severity= severity.substring(0,severity.length()-2);
            stmt.execute("INSERT INTO PatientRecord VALUES(0,'"+name+"','"+phone+"','"+emergency+"',"+age+",'"+gender+"','"+blood+"',"+
                    weight+","+height+",'"+symptoms+"',CURRENT_TIMESTAMP,'"+severity+"','"+comments+"',null,null,null);");
            con.close();
        } catch (ClassNotFoundException | SQLException ex) {
            ex.printStackTrace();
        }
        
    }
    
}
