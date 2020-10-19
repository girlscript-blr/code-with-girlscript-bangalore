<?php
include_once("connect.php");
$result = mysqli_query($con,"SELECT * FROM patient_details")or die(mysql_error());
echo "<table border='1' align='center'>";
echo "<tr></tr><th>Patient ID</th><th>Full Name</th><th>Phone Number</th><th>Emergency Number</th><th>AGE</th><th>Gender</th><th>Blood Type</th><th>Weight</th><th>Height</th><th>Symptoms</th><th>Date</th></tr>";
 while($row = mysqli_fetch_array( $result )) {
 	echo "<tr>";
 	echo "<td>" .$row['Patient ID']. "</td>";
 	echo "<td>" .$row['Full Name']. "</td>";
 	echo "<td>" .$row['Phone Number']. "</td>";
 	echo "<td>" .$row['Emergency Contact Number']. "</td>";
 	echo "<td>" .$row['Age']. "</td>";
 	echo "<td>" .$row['Gender']. "</td>";
 	echo "<td>" .$row['Blood Type']. "</td>";
 	echo "<td>" .$row['Weight']. "</td>";
 	echo "<td>" .$row['Height']. "</td>";
 	echo "<td>" .$row['Symptoms']. "</td>";
 	echo "<td>" .$row['Date Of Admission']. "</td>";
 	echo "</tr>";
 }
 echo "</table>";
 ?>
 <html>
 <head>
 	<link rel="stylesheet" href="index.css">
 </head>
 <a href="index.php"><input type="button" class="back1" value="HOME"></a>
 </html>