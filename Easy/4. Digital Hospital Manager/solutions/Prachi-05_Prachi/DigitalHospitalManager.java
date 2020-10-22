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
        while(ch=='1' || ch=='2'){
            System.out.println("1. Add Patient\n2. Fetch Patient Records\n Press any key to exit\nEnter choice:");
            ch=in.next().charAt(0);
            try{
                switch(ch){
                    case '1': readPatientData(); break;
                    case '2': fetchPatient();break;                    
                }
            }
            catch(IOException e){
                e.printStackTrace();
            }
            
        }
        
    }
    static void fetchPatient(){
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
            rs = stmt.executeQuery("SELECT count(*) as count from PatientRecord where admissiondate = CURRENT_TIMESTAMP ");
            rs.next();
            System.out.println("Total number of patients currently admitted: "+ rs.getInt("count"));
            rs = stmt.executeQuery("SELECT * FROM PatientRecord");
            if(rs.next()){
                rs.previous();
                System.out.println("Patient ID\tPatient Name\tPhone Number\tEmergency Contact Number\t"
                        + "Age\tGender\tBlood Type\tWeight\tHeight\tSymptoms/Medical Details\tDate of Admission");
                while(rs.next()){
                    System.out.println(rs.getInt(1)+"\t\t"+rs.getString(2)+"\t\t"+rs.getString(3)+"\t\t"+rs.getString(4)
                    +"\t\t"+rs.getInt(5)+"\t"+rs.getString(6)+"\t"+rs.getString(7)+"\t\t"+rs.getFloat(8)+"\t"+rs.getFloat(9)
                    +"\t"+rs.getString(10)+"\t\t"+rs.getTimestamp(11));                  

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
        System.out.print("\nGender: ");
        String gender = in.readLine();
        System.out.print("\nBlood type: ");
        String blood = in.readLine();
        System.out.print("\nWeight: ");
        float weight = Float.parseFloat(in.readLine());
        System.out.print("\nHeight: ");
        float height = Float.parseFloat(in.readLine());
        System.out.print("\nSymptoms/Medical Details: ");
        String symptoms = in.readLine();
        addPatientDB(name,phone,emergency,age,gender,blood,weight,height,symptoms);
    }
    static void addPatientDB(String name, String phone, String emergency,
            int age, String gender,String blood, float weight, float height, String symptoms){
        Connection con = null;
        Statement stmt;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/digitalhospitalmanager", "root", "alohomora");
            stmt = con.createStatement();
            stmt.execute("INSERT INTO PatientRecord VALUES(0,'"+name+"','"+phone+"','"+emergency+"',"+age+",'"+gender+"','"+blood+"',"+
                    weight+","+height+",'"+symptoms+"',CURRENT_TIMESTAMP);");
            con.close();
        } catch (ClassNotFoundException | SQLException ex) {
            ex.printStackTrace();
        }
        
    }
    
}
