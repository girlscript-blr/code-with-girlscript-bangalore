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
      <div class="col-12">
        <table class="table table-striped table-dark">
            <thead>
              <tr class="bg-success">
                <th scope="col">Serial Number</th>
                <th scope="col">Product</th>
                <th scope="col">Price</th>
                <th scope="col">Quantity</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>OnePlus 6T</td>
                <td><span>&#8377;</span>30000</td>
                <td><input type="number" min="0" name="qty1" id="qty1" placeholder="0"></td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>OnePlus earphone</td>
                <td><span>&#8377;</span>500</td>
                <td><input type="number" min="0" name="qty2" id="qty2" placeholder="0"></td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td>OnePlus 6T Case</td>
                <td><span>&#8377;</span>200</td>
                <td><input type="number" min="0" name="qty3" id="qty3" placeholder="0"></td>
              </tr>
            </tbody>
          </table>
      </div>
      </div>
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

    <script src="./js/script.js"></script>
    <!-- JS, Popper.js, and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>  
</body>
</html>