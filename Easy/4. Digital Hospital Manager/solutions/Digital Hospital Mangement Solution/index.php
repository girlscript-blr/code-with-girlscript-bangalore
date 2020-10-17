<html>
<head>
	<link rel="stylesheet" href="index.css"/>
	</head>
	<body class="class1">
<a href="patients_add.php"><input class="add" type="button" name="button1" value="ADD" /></a>
<a href="patients_view.php"><input class="view" type="button" name="button2" value="VIEW"/></a>


<?php
include_once('connect.php');
echo "<div style='color:white;text-align:center;font-size:30px;font-family:Arial;'>";
echo "<br>";
$sql=mysqli_query($con,"select count('Patient ID') as count from patient_details");
while($row=mysqli_fetch_array($sql))
{
	echo "The total number of patients admitted are " .$row['count']. ".";
}
echo "<br>";
$sql=mysqli_query($con,"select count('Patient ID') as count from patient_details");
while($row=mysqli_fetch_array($sql))
{
	echo "The total number of patients present now are " .$row['count']. ".";
}
echo "<br>";

$sql=mysqli_query($con,"select count('Patient ID') as count from patient_details where DATE(date)=DATE(Now())");
while($row=mysqli_fetch_array($sql)){
	echo "The total number of patients admitted today are " .$row['count']. ".";
}
echo "</div>";
?>
</body>
</html>
