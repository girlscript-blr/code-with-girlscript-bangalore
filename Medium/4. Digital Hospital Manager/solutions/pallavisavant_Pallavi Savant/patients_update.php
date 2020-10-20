
<?php
include_once('connect.php');
if(isset($_POST['submit'])){
	$id=$_POST['id'];
	$comments=$_POST['comments'];
	$date=$_POST['date'];
	$discharge=$_POST['comments1'];
	$sql=mysqli_query($con,"update `patient_details` set `Date Of Discharge`='$date',`Medical Details/Comments`='$comments',`Discharge Comments`='$discharge' where `Patient ID`='$id'");
	if($_POST['date1']){
		$date1=$_POST['date1'];
		$sql=mysqli_query($con,"update `patient_details` set `Date And Time Of Death`='$date1' where `Patient ID`='$id'");
	}

	
	
}

?>
<!DOCTYPE html>
<html>
</html>
<head>
	<link rel="stylesheet" href="index.css"/>
	<script type="text/javascript">
		function executeonsubmit(){
		alert("Data updated successfully!!!");
	}
	</script>
	</head>
<body>
	<div class="content2">
		<div class="content1">
	<form action="patients_update.php" onsubmit="return executeonsubmit();" method="post">
		<div class="block">
		<label>Patient ID: </label>
		<input type="number" name="id" placeholder="Patient ID" required="required">
	</div>
		<div class="block">
		<label>Medical Details/Comments: </label>
		<input type="text" name="comments" placeholder="Medical Comments" required="required">
	</div>
		<div class="block">
		<label>Discharge Date: </label>
		<input type="date" name="date" placeholder="Discharge Date" required="required">
	</div>
	<div class="block">
		<label>Discharge Comments: </label>
		<select name="comments1" required="required">
		<option value="Decreased">Decreased</option>
		<option value="cured">Cured</option>
			</select>
	</div>
	<div class="block">
		<label>Date And Time Of Death</label>
		<input type="datetime-local" name="date1" placeholder="Date">(If Decreased then enter the date of death)</input>
	</div>
	<input name="submit" style="color:white;background-color: black;height:30px;width:55px;text-align: center;transform: translate(200px, 20px);" type="submit" value="Submit"/>
</form>
</form>
</div>
</div>
</form>
<a href="index.php"><input style="background-color: black;width:80px;height:30px;text-align: center;color: white;transform: translate(700px, 150px);" type="button" name="button2" value="HOME"/></a>
	</body>
	</html>