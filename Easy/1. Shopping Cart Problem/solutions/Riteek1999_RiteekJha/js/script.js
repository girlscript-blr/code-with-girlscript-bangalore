(function () {
    var form1 = document.getElementById("regForm");
    form1.addEventListener('submit', checkForm);
    function checkForm(event) {
      event.preventDefault();
      console.log(event);
      myform = event.target.value;
  

      var mno = document.getElementById("phoneno").value;
      var qty1 = document.getElementById("qty1").value;
      var qty2 = document.getElementById("qty2").value;
      var qty3 = document.getElementById("qty3").value;
      if(qty1==0 && qty2==0 && qty3==0){
        alert("You to buy atleast one product");
        return false;
      }
      if (mno.toString().length != 10) {
        alert("Invalid contact number");
        return false;
      } else {
       event.target.submit();
      }
    }
  })();