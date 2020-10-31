<?php

$con=mysqli_connect("localhost","root","","my_db");
if(mysqli_connect_errno()){
	echo "failed".mysqli_connect_error();
}
?>