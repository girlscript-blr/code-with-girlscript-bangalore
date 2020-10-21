<html>
<head>
	<link rel="stylesheet" href="index.css"/>
	</head>
	<body class="class1">
<a href="patients_add.php"><input class="add" type="button" name="button1" value="ADD PATIENT" /></a>
<a href="patients_view.php"><input class="view" type="button" name="button2" value="VIEW DETAILS"/></a>
<a href="patients_update.php"><input style="background-color: black;width:250px;height:70px;text-align:center;color: white;transform: translate(360px, 250px);font-size: 20px;" type="button" name="button3" value="UPDATE DETAILS"/></a>
<?php
include_once('connect.php');
echo "<div style='color:white;text-align:center;font-size:30px;font-family:Arial;'>";
echo "<br>";
$sql=mysqli_query($con,"select count('Patient ID') as count from patient_details");
while($row=mysqli_fetch_array($sql))
{
	echo "The total number of patients present now are " .$row['count']. ".";
}
echo "<br>";

$sql=mysqli_query($con,"select count(`Patient ID`) as count from `patient_details` where DATE(`Date Of Admission`)=DATE(Now())");
while($row=mysqli_fetch_array($sql)){
	echo "The total number of patients admitted today are " .$row['count']. ".";
}
echo "<br>";
$sql=mysqli_query($con,"select count(`Patient ID`) as count from `patient_details` where `Date Of Discharge`=DATE(Now())");
while($row=mysqli_fetch_array($sql)){
	echo "The total number of patients discharged today are " .$row['count']. ".";
}
echo "<br>";

echo "</div>";
?>
</body>
</html>
