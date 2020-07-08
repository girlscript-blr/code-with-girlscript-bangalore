<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <link rel="stylesheet" href="./css/style.css">
    <title>GirlScript</title>
</head>
<body>
    <nav class="navbar navbar-dark bg-dark">
    <a class="navbar-brand">Shopping Cart</a>
    <form class="form-inline">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
    </nav>
    
    <div class="container">
      <div class="row">
      <div class="col-12 col-md-6">
        <form  action="calc.php" method="POST" id="regForm">
        <div class="form-group">
            <label for="fullname">Full Name</label>
            <input type="text" class="form-control" id="fullname" name="fullname" required >
        </div>
        <div class="form-group">
            <label for="phoneno">Contact Number</label>
            <input type="number" min="0" class="form-control" id="phoneno" name="phoneno" required>
        </div>
      </div>
      </div>
      <div class="row">
      <div class="col-12 col-md-3">
      
      <div class="card" id="card1" style="width: 18rem;">
      <img src="./images/1.jpg" class="card-img-top mt-2" alt="Oneplus 6T">
      <div class="card-body">
        <h5 class="card-title">OnePlus 6T</h5>
        <h5 class="card-title"><span>&#8377;</span>30000</h5>
        <a href="#" class="btn btn-lg btn-success" onclick="onButtonClick1()">Buy</a>
        <h5 class="hide card-title" id="qty1">Quantity</h5>
        <input class="hide" type="number" id="NumberInput1" name="qty1" min="0">
      </div>
    </div>
    </div>

    <div class="card ml-5" id="card2" style="width: 18rem;">
      <img src="./images/2.jpg" class="card-img-top" alt="Oneplus 6T">
      <div class="card-body">
        <h5 class="card-title">OnePlus earphone</h5>
        <h5 class="card-title"><span>&#8377;</span>500</h5>
        <a href="#" class="btn btn-lg btn-success" onclick="onButtonClick2()">Buy</a>
        <h5 class="hide card-title" id="qty2">Quantity</h5>
        <input class="hide" type="number" id="NumberInput2" name="qty2" min="0">
      </div>
    </div>

    <div class="card ml-4" id="card3" style="width: 18rem;">
      <img src="./images/3.png" class="card-img-top" alt="Oneplus 6T">
      <div class="card-body">
        <h5 class="card-title">OnePlus 6T Case</h5>
        <h5 class="card-title"><span>&#8377;</span>200</h5>
        <a href="#" class="btn btn-lg btn-success" onclick="onButtonClick3()">Buy</a>
        <h5 class="hide card-title" id="qty3">Quantity</h5>
        <input class="hide" type="number" id="NumberInput3" name="qty3" min="0">
      </div>
    </div>

      </div>
      </div>

      <div class="container">
      <div class="row">
      <div class="col-offset-1">
      <div class="form-group">
            <label for="payment">Payment Method</label>
            <div class="input-group">
              <div class="input-group-prepend">
                <div class="input-group-text">
                  <input type="radio" value="Cash on Devlivery" name="payment" required>
                </div>
              </div>
              <label class="form-control">Cash on Delivery</label>
            </div>
            <div class="input-group">
              <div class="input-group-prepend">
                <div class="input-group-text">
                  <input type="radio" value="BHIM/UPI" name="payment">
                </div>
              </div>
              <label class="form-control">BHIM/UPI</label>
            </div>
            <div class="input-group">
              <div class="input-group-prepend">
                <div class="input-group-text">
                  <input type="radio" value="Net Banking" name="payment">
                </div>
              </div>
              <label class="form-control">Net Banking</label>
            </div>
      </div>
      </div>
      </div>

        <button type="submit" class="btn btn-success">Submit</button>
        </form>
    </div>
    </div>

    <script src="./js/script.js"></script>
    <script src="./js/script1.js"></script>
    <!-- JS, Popper.js, and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>  
</body>
</html>