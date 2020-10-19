Instructions to run the application:

```
*Import the .sql file into XAMPP software which has database.
*Run index.php by typing loaclhost/index.php on your browser.
*To add the new patient details click on ADD button and click submit after entering all the details.
*To view the patient details click on VIEW button.
```
Instruction to import .sql file:

```
1) Go to localhost/phpmyadmin/
2) Create a new database of name my_db
3)Click on import and import .sql file
4) Then you will get the table in your database.
```
Application also outputs:

```
*The  total number of patients admitted on current date.

*Total number of patients present at current time.
```
The index.php looks like this:
![image](Dashboard.png)

Clicking ADD button will take you to Patients_add.php
![image](Adding_Details.png)

Clicking VIEW button will take you to patients_view.php
![image](View_Details.png)