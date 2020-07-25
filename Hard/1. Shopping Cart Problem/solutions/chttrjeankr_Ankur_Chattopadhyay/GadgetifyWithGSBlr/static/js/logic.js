// Delivery Type Handler
//
function deliveryCheck() {
  if (document.getElementById("homedel").checked) {
    document.getElementById("if-homedel").style.display = "block";
    document.getElementById("shipping_address").required = true;
    document.getElementById("distance_from_shop").required = true;
  } else {
    document.getElementById("if-homedel").style.display = "none";
    document.getElementById("shipping_address").required = false;
    document.getElementById("distance_from_shop").required = false;
  }
}
// END //

// CSRF TOKEN FOR AJAX
//
// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }
// const csrftoken = getCookie("csrftoken");
//
// function csrfSafeMethod(method) {
//   // these HTTP methods do not require CSRF protection
//   return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
// }
// $.ajaxSetup({
//   beforeSend: function (xhr, settings) {
//     if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//       xhr.setRequestHeader("X-CSRFToken", csrftoken);
//     }
//   },
// });
// END //

// Add to Cart Button
//
// $(function () {
//   $("[id^=quantity_]").on("submit", function (event) {
//     var that = this;
//     var formId = this.id;
//     var quantity = this.elements.item(0).value;
//     $.ajax({
//       data: {
//         id: formId,
//         quantity: quantity,
//       },
//       type: "POST",
//       url: "/add_to_cart/",
//       success: function (data) {
//         alert(`Item modified: ${data["item"]}`);
//       },
//     });
//     event.preventDefault();
//   });
// });
// END //
