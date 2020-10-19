<?php
include_once('connect.php');
if (isset($_POST['submit'])){
	$full_name=$_POST['full_name'];
	$phone_number=$_POST['phone_number'];
	$emergency_contact_number=$_POST['emergency_contact_number'];
	$age=$_POST['age'];
	$gender=$_POST['gender'];
	$blood_type=$_POST['blood_type'];
	$weight=$_POST['weight'];
	$height=$_POST['height'];
	if(isset($_POST['fever'])){
	$symptom1=$_POST['fever'];}
	else{
		$symptom1=NULL;
	}
	if(isset($_POST['headache'])){
		$symptom2=$_POST['headache'];
	}
	else{
		$symptom2=NULL;
	}
if(isset($_POST['Fatigue,weakness'])){
	$symptom3=$_POST['Fatigue,weakness'];
}
else{
	$symptom3=NULL;
}
if(isset($_POST['Stuffy/runny nose'])){
	 $symptom4=$_POST['Stuffy/runny nose'];
	}
	else{
		$symptom4=NULL;
	}
	if(isset($_POST['Sneezing'])){
	$symptom5=$_POST['Sneezing'];}
	else{
		$symptom5=NULL;
	}
	if(isset($_POST['Sore Throat'])){
	$symptom6=$_POST['Sore Throat'];}
	else{
		$symptom6=NULL;
	}
	if(isset($_POST['Cough'])){
	$symptom7=$_POST['Cough'];}
	else{
		$symptom7=NULL;
	}
	if(isset($_POST['Shortness of breath'])){
	$symptom8=$_POST['Shortness of breath'];}
	else{
		$symptom8=NULL;
	}
	if(isset($_POST['Bluish lips or face'])){
	$symptom9=$_POST['Bluish lips or face'];}
	else{
		$symptom9=NULL;
	}
	if(isset($_POST['Constant pain or pressure in your chest'])){
	 $symptom10=$_POST['Constant pain or pressure in your chest'];
	}
	else{
		$symptom10=NULL;
	}
	$comments=$_POST['comments'];

$sql=mysqli_query($con,"INSERT INTO `patient_details`(`Full Name`, `Phone Number`, `Emergency Contact Number`, `Age`, `Gender`, `Blood Type`, `Weight`, `Height`, `Symptoms`,`Medical Details/Comments`) VALUES ('$full_name','$phone_number','$emergency_contact_number','age','$gender','$blood_type','$weight','$height','$symptom1 $symptom2','$comments')");
if(($symptom1 and $age>=0 and $age<=16) or ($symptom1 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"update `patient_details` set `Severity`=CONCAT(`Severity`,'Mild ') where `Full Name`='$full_name'");
}
if($symptom1 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom2 and $age>=0 and $age<=16) or ($symptom2 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom2 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom3 and $age>=0 and $age<=16) or ($symptom3 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom3 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom4 and $age>=0 and $age<=16) or ($symptom4 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom4 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom5 and $age>=0 and $age<=16) or ($symptom5 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom5 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom6 and $age>=0 and $age<=16) or ($symptom6 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom6 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom7 and $age>=0 and $age<=16) or ($symptom7 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom7 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom8 and $age>=0 and $age<=16) or ($symptom8 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom8 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom9 and $age>=0 and $age<=16) or ($symptom9 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom9 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}
if(($symptom10 and $age>=0 and $age<=16) or ($symptom10 and $age>=17 and $age<=45)){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Mild ')");
}
if($symptom10 and $age>=46){
	$sql=mysqli_query($con,"UPDATE `patient_details` SET `Severity`=CONCAT(`Severity`,'Emergency ')");
}

}
?>
<html>
<head>
	<link rel="stylesheet" href="index.css">
</head>
<div class="content2">
   <div class="content1">   
<form action='patients_add.php'  name='form1' method='post'>
	<div class="block">
	<label>Full Name</label>
	<input name="full_name" type="text"  placeholder="Full Name" required="required" id="full_name"/><br>
</div>
<div class="block">
	<label>Phone Number</label>
	<input name="phone_number" type="text" placeholder="Phone Number" required="required" id="phone_number" /><br>
</div>
<div class="block">
	<label>Emergency Contact Number</label>
	<input name="emergency_contact_number" type="text" placeholder="Emergency Contact Number" required="required" id="emergency_contact_number" /><br>
</div>
<div class="block">
	<label>Age</label>
	<input name="age" type="text"  placeholder="Age" required="required" id="age" /><br>
</div>
<div class="block">
	<label>Gender</label>
	<select name="gender">
	<option value="Male">Male</option>
	<option value="Female">Female</option>
	<option value="Others">Others</option>
</select>
</div>
<div class="block">
	<label>Blood Type</label>
	<select name="blood_type">
		<option value="A+">A+</option>
		<option value="B+">B+</option>
		<option value="AB+">AB+</option>
		<option value="A-">A-</option>
		<option value="B-">B-</option>
		<option value="AB-">AB-</option>
		<option value="O+">O+</option>
		<option value="O-">O-</option>
	</select>
</div>
<div class="block">
	<label>Weight</label>
	<input name="weight" type="text" placeholder="Weight" required="required" id="weight" /><br>
</div>
<div class="block">
	<label for="height">Height</label>
	<input name="height" type="text" placeholder="Height" required="required" id="height" /><br>
</div>
<div>
	<label>Symptoms:</label>
	<input type="checkbox" name="fever" value="fever">Fever</input>
	<input type="checkbox" name="headache" value="headache">Headache</input>
	<input type="checkbox" name="Fatigue,weakness" value="Fatigue,weakness">Fatigue,weakness</input>
	<input type="checkbox" name="Stuffy/runny nose" value="Stuffy/runny nose">Stuffy/runny nose</input>
	<input type="checkbox" name="Sneezing" value="Sneezing">Sneezing</input>
	<input type="checkbox" name="Sore Throat" value="Sore Throat">Sore Throat</input>
	<input type="checkbox" name="Cough" value="Cough">Cough</input>
	<br>
	<label></label>
	<input type="checkbox" name="Shortness of breath" value="Shortness of breath">Shortness of breath</input>
	<input type="checkbox" name="Bluish lips or face" value="Bluish lips or face">Bluish lips or face</input>
	<input type="checkbox" name="Constant pain or pressure in your chest" value="Constant pain or pressure in your chest">Constant pain or pressure in your chest </input>
	</div>
	<br>
	<div class="block">
		<label>Medical Details/Comments</label>
		<textarea rows="4" cols="50" name="comments">Enter Comments Here.....</textarea>
	</div>
	<input name="submit" style="color:white;background-color: black;height:30px;width:55px;text-align: center;transform: translate(200px, 20px);" type="submit" value="Submit"/>
</form>
</div>
</div>

</html>