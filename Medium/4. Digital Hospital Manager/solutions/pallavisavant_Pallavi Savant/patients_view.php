<html>
 <body>
 	<div class="content2">
 		<div class="content1">
 	<form action="patients_view.php" method="post">
 		<input type="text" name="search" placeholder="Enter Patient Name OR ID">
 		<input type="submit" name="submit" value="SUBMIT">
 	</form>
 </div>
</div>
 </body>


<?php
include_once("connect.php");
if(isset($_POST['submit'])){
	$name=$_POST['search'];
$result = mysqli_query($con,"SELECT * FROM patient_details where `Full Name`='$name' or `Patient ID`='$name'");
echo "<table border='1' align='center'>";
echo "<tr><th>INPUTS</th><th>VALUES</th></tr>";
 while($row = mysqli_fetch_array( $result )) {
 	echo "<tr>";
 	echo "<td>Patient ID</td>";
 	echo "<td>" .$row['Patient ID']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Full Name</td>";
 	echo "<td>" .$row['Full Name']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Phone Number</td>";
 	echo "<td>" .$row['Phone Number']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Emergency Contact Number</td>";
 	echo "<td>" .$row['Emergency Contact Number']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Age</td>";
 	echo "<td>" .$row['Age']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Gender</td>";
 	echo "<td>" .$row['Gender']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Blood Type</td>";
 	echo "<td>" .$row['Blood Type']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Weight</td>";
 	echo "<td>" .$row['Weight']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Height</td>";
 	echo "<td>" .$row['Height']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Symptoms</td>";
 	echo "<td>" .$row['Symptoms']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Severity</td>";
 	echo "<td>" .$row['Severity']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Medical Details/Comments</td>";
    echo "<td>" .$row['Medical Details/Comments']. "</td>";
    echo "</tr>";
    echo "<tr>";
    echo "<td>Date Of Admission</td>";
 	echo "<td>" .$row['Date Of Admission']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Date Of Discharge</td>";
 	echo "<td>" .$row['Date Of Discharge']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Discharge Comments</td>";
 	echo "<td>" .$row['Discharge Comments']. "</td>";
 	echo "</tr>";
 	echo "<tr>";
 	echo "<td>Date and time of death</td>";
 	echo "<td>" .$row['Date And Time Of Death']. "</td>";
 	echo "</tr>";


 }}
 echo "</table>";
 ?>

 </html>