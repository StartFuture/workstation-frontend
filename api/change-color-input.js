var submit_button = document.getElementById("Login");

submit_button.addEventListener("click", function(e) {
  var required = document.querySelectorAll("input[required]");
  
  required.forEach(function(element) {
    if(element.value.trim() == "") {
      element.style.backgroundColor = "pink";
    } else {
      element.style.backgroundColor = "white";
    }
  });
});