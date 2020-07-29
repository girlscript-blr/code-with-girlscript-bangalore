function deliveryCheck() {
  if (document.getElementById("homedel").checked) {
    document.getElementById("if-homedel").style.display = "block";
    document.getElementById("shippingAddress").required = true;
    document.getElementById("distKMs").required = true;
  } else {
    document.getElementById("if-homedel").style.display = "none";
    document.getElementById("shippingAddress").required = false;
    document.getElementById("distKMs").required = false;
  }
}

$(function () {
  $("[id^=quantity_]").on("submit", function (event) {
    var that = this;
    var formId = this.id;
    var quantity = this.elements.item(0).value;
    $.ajax({
      data: {
        id: formId,
        quantity: quantity,
      },
      type: "POST",
      url: "/add_to_cart",
      success: function (data) {
        alert(`Item added: ${data["item"]}`);
      },
    });
    event.preventDefault();
  });
});
