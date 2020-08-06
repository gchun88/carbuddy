
var slideIndex1 = 1;
var slideIndex2 = 1;
var slidetest = false;


console.log(1);

slideArrow_1(slideIndex1);
slidePosition_1(slideIndex1);
// slidePosition_2(slideIndex2);
autoslides_2();
matilda();

// if(!slidetest){
//   autoslides_2();
// }


function slide_arrow_1(n) {
  slideArrow_1(slideIndex1 += n);
}

function position_Button_1(j) {
  slidePosition_1(slideIndex1 = j);
}


function slideAutomation_2(j) {
  slidePosition_2(slideIndex2 = j);
}

function slideArrow_1(n) {
  var i;
  var x = document.getElementsByClassName("main-slide-1");
  if (n > x.length) {slideIndex1 = 1}
  if (n < 1) {slideIndex1 = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex1-1].style.display = "block";
}


function slidePosition_1(j) {
  var x = document.getElementsByClassName("main-slide-1");
  var i;
  for (i = 0; i < x.length; i++){
      x[i].style.display ="none";
  }
  x[slideIndex1-1].style.display = "block";
}

function slidePosition_2(j) {
  var x = document.getElementsByClassName("main-slide-2");
  var dots = document.getElementsByClassName("position-button-2");
  var i;
  for (i = 0; i < x.length; i++){
      x[i].style.display ="none";
  }
  if (slideIndex2 >x.length){slideIndex2 = 1}
  x[slideIndex2-1].style.display = "block";

  console.log("before if : "+slidetest)
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  dots[slideIndex2-1].className += " active";
  // if (slidetest == true){
  //   slidetest = false;
  // }
  // else {slidetest = true}
  //  slidetest = true;
  slidetest = true;
  autoslides_2()
}


function autoslides_2() {
  var i;
  var slides = document.getElementsByClassName("main-slide-2");
  var dots = document.getElementsByClassName("position-button-2");
  if (slidetest == true){
    slidetest = false;
    return false
  }
  for(i = 0; i < slides.length; i++){
    slides[i].style.display = "none";
  }
  slideIndex2++;
  if (slideIndex2 > slides.length) {slideIndex2 = 1}
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex2-1].style.display = "block";
  dots[slideIndex2-1].className += " active";
  setTimeout(autoslides_2, 2000); // Change image every 2 seconds
}
// === absolute equal == when memory path is different == still shows true



function matilda(){
  var i;
  var mtd = document.getElementsByClassName("main-slide-3");
  for(i = 0; i < mtd.length; i++){
  mtd[i].style.display = "none";
  }
  mtd[0].style.display = "block";
  console.log(mtd[2])
}





