
var slideIndex = 1;
slideArrow_1(slideIndex);
slidePosition_1(slideIndex);
slideAutomation_2(slideIndex);


function slide_arrow_1(n) {
  slideArrow_1(slideIndex += n);
}

function position_Button_1(j) {
  slidePosition_1(slideIndex = j);
}

function position_Button_2(j) {
  slidePosition_3(slideIndex = j);
}
function slideAutomation_2(j) {
  var a;
  slidePosition_2(slideIndex= j);
  a+=slideIndex;
  setTimeout(slidePosition_2(a),1000)
}
function slideArrow_1(n) {
  var i;
  var x = document.getElementsByClassName("main-slide-1");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
}


function slidePosition_1(j) {
  var x = document.getElementsByClassName("main-slide-1");
  var i;
  for (i = 0; i < x.length; i++){
      x[i].style.display ="none";
  }
  x[slideIndex-1].style.display = "block";
}


function slidePosition_3(j) {
  var x = document.getElementsByClassName("main-slide-2");
  var i;
  for (i = 0; i < x.length; i++){
      x[i].style.display ="none";
  }
  if (slideIndex >x.length){slideIndex = 1}
  x[slideIndex-1].style.display = "block";
}
function slidePosition_2(j) {
  var x = document.getElementsByClassName("main-slide-2");
  var i;
  var a;
  for (i = 0; i < x.length; i++){
      x[i].style.display ="none";
  }
  if (slideIndex >x.length){slideIndex = 1}
  x[slideIndex-1].style.display = "block";

}

