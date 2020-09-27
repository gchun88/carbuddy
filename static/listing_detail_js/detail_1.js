var slideIndex2 = 1;
button_black_gray()
function button_handler(j) {
  button_black_gray(slideIndex2 = j);
}


function button_black_gray(j) {
  var x = document.getElementsByClassName("btn-light");
  var i;
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active-black", " inactive-gray");
  }
  x[slideIndex2-1].className = x[slideIndex2-1].className.replace(" inactive-gray", " active-black");
}