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
	<input name="gender" type="text" placeholder="Gender" required="required" id="gender" /><br>
</div>
<div class="block">
	<label>Blood Type</label>
	<input name="blood_type" type="text" placeholder="Blood Type" required="required" id="blood_type" /><br>
</div>
<div class="block">
	<label>Weight</label>
	<input name="weight" type="text" placeholder="Weight" required="required" id="weight" /><br>
</div>
<div class="block">
	<label for="height">Height</label>
	<input name="height" type="text" placeholder="Height" required="required" id="height" /><br>
</div>
<div class="block">
	<label for="symptoms">Symptoms</label>
	<input name="symptoms" type="text" placeholder="Symptoms" required="required" id="symptoms" /><br>
</div>
	<input name="submit" style="color:white;background-color: black;height:30px;width:55px;text-align: center;transform: translate(200px, 60px);" type="submit" value="Submit"/>
</form>
</div>
</div>

</html>