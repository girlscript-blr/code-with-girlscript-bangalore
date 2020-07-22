<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <link rel="stylesheet" href="./css/style.css">
    <title>Calculation</title>
</head>
<body>
    <?php
    if(isset($_POST['fullname'])){
        $FULLNAME = $_POST['fullname'];
        $CONTACTNO = $_POST['phoneno'];
        $PAYMENT = $_POST['payment'];
        if(isset($_POST['qty1'])){
            $PROD1="OnePlus 6T";
            $PRICE1=30000;
            $QTY1=$_POST['qty1'];
            $AMT1=$PRICE1*(int)$QTY1;
        }
        if(isset($_POST['qty2'])){
            $PROD2="OnePlus earphone";
            $PRICE2=500;
            $QTY2=$_POST['qty2'];
            $AMT2=$PRICE2*(int)$QTY2;
        }
        if(isset($_POST['qty3'])){
            $PROD3="OnePlus 6T Case";
            $PRICE3=200;
            $QTY3=$_POST['qty3'];
            $AMT3=$PRICE3*(int)$QTY3;
        }
        $TOTAL=$AMT1+$AMT2+$AMT3;
        $TAX=0.06*$TOTAL;
        $FINALTOTAL=$TOTAL+$TAX;
        date_default_timezone_set('Asia/Kolkata');
        $date = date('d-m-y h:i:s');
    }
    ?>

    <nav class="navbar navbar-dark bg-dark">
    <a class="navbar-brand">Shopping Cart</a>
    <form class="form-inline">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
    </nav>

    <div class="container">
    <div class="row">
    <div class="col-6">
    <div class="card" style="width: 30rem;">
    <div class="card-body">
        <h3 class="card-title">Bill</h3>
        <h6 class="card-subtitle mb-2 text-muted">
            GadgetifyWithGSBlr<br>
            address: 311/5 Akshay nagar, Bangalore, Karnataka, India<br>
            contact no: +91 9988776655<br><br><br>
        </h6>
        <h6 class="card-subtitle mb-2 text-muted">Customer: <?php echo $FULLNAME ?></h6>
        <h6 class="card-subtitle mb-2 text-muted">Phone Number: <?php echo $CONTACTNO ?></h6>
        <table class="table table-striped table-dark">
        <tr>
            <th>PRODUCT</th>
            <th>PRICE</th>
            <th>QUANTITY</th>
            <th>AMOUNT</th>
        </tr>
        <tr>
            <?php if(($_POST['qty1']) != 0) { ?>
            <td><?php echo $PROD1 ?></td>
            <td><span>&#8377;</span><?php echo $PRICE1 ?></td>
            <td><?php echo $QTY1 ?></td>
            <td><?php echo $AMT1 ?></td>
            <?php } ?>
        </tr>
        <tr>
            <?php if(($_POST['qty2']) != 0) { ?>
            <td><?php echo $PROD2 ?></td>
            <td><span>&#8377;</span><?php echo $PRICE2 ?></td>
            <td><?php echo $QTY2 ?></td>
            <td><?php echo $AMT2 ?></td>
            <?php } ?>
        </tr>
        <tr>
            <?php if(($_POST['qty3']) != 0) { ?>
            <td><?php echo $PROD3 ?></td>
            <td><span>&#8377;</span><?php echo $PRICE3 ?></td>
            <td><?php echo $QTY3 ?></td>
            <td><?php echo $AMT3 ?></td>
            <?php } ?>
        </tr>
        </table>
        <hr>
        <table class="table table-striped table-dark">
            <tr>
                <td>Total:</td>
                <td></td>
                <td></td>
                <td><span>&#8377;</span><?php echo $TOTAL ?></td>
            </tr>
            <tr>
                <td>Tax:</td>
                <td></td>
                <td></td>
                <td><span>&#8377;</span><?php echo $TAX ?></td>
            </tr>
            <tr>
                <td colspan="2">Amount to be paid:</td>
                <td></td>
                <td><span>&#8377;</span><?php echo $FINALTOTAL ?></td>
            </tr>
        </table>
        <h6 class="card-subtitle mb-2 text-muted">PAYMENT METHOD: <?php echo $PAYMENT ?></h6>
        <h6 class="card-subtitle mb-2 text-muted"><?php echo $date ?></h6>
    </div>
    </div>
    </div>
    </div>
    </div>
</body>
</html>