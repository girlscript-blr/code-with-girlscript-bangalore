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
	$symptoms=$_POST['symptoms'];
$sql=mysqli_query($con,"INSERT INTO `patient_details`(`Full Name`, `Phone Number`, `Emergency Contact Number`, `Age`, `Gender`, `Blood Type`, `Weight`, `Height`, `Symptoms`) VALUES ('$full_name','$phone_number','$emergency_contact_number','age','$gender','$blood_type','$weight','$height','$symptoms')");
}
?>
<html>


      
<form action='patients.php'  name='form1' method='post'>
	<input name="full_name" type="text" style="width:170px" placeholder="Full Name" required="required" id="full_name" />
	<input name="phone_number" type="text" style="width:170px" placeholder="Phone Number" required="required" id="phone_number" />
	<input name="emergency_contact_number" type="text" style="width:170px" placeholder="Emergency Contact Number" required="required" id="emergency_contact_number" />
	<input name="age" type="text" style="width:170px" placeholder="Age" required="required" id="age" />
	<input name="gender" type="text" style="width:170px" placeholder="Gender" required="required" id="gender" />
	<input name="blood_type" type="text" style="width:170px" placeholder="Blood Type" required="required" id="blood_type" />
	<input name="weight" type="text" style="width:170px" placeholder="Weight" required="required" id="weight" />
	<input name="height" type="text" style="width:170px" placeholder="Height" required="required" id="height" />
	<input name="symptoms" type="text" style="width:170px" placeholder="Symptoms" required="required" id="symptoms" />
	<input name="submit" type="submit" value="Submit"/>
</form>

</html>