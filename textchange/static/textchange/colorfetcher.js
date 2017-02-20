
var globalCount = 0;

function getColor() {
  var oldcolor = localStorage.getItem("funColor");
  var oldcolor2 = localStorage.getItem("funColor2");

  if(oldcolor) {
    document.getElementById("landing_page").style.animation
    document.getElementById("landing_page").style.background = 'linear-gradient(180deg,' + oldcolor + ', ' +  oldcolor2 + ')';
  } else {
    document.getElementById("landing_page").style.background = 'linear-gradient(180deg, rgb(255, 162, 102), rgb(234, 107, 107))';
  }
}

function changeColor() {
  var colors = [['rgb(255, 96, 115)', 'rgb(234, 56, 77)'],
  ['rgb(139, 223, 181)', 'rgb(145, 222, 145)'],
  ['rgb(127, 139, 144)', 'rgb(78, 83, 96)'],
  ['#4EA9F6' , '#3583D0'],
  ['rgb(255, 162, 102)', 'rgb(234, 107, 107)']];

  if(globalCount === 4) {
    globalCount = 0;
  } else {
    globalCount += 1;
  }
  document.getElementById("landing_page").style.background = 'linear-gradient(180deg,' + colors[globalCount][0] + ', ' +  colors[globalCount][1] + ')';

  localStorage.setItem("funColor", colors[globalCount][0]);
  localStorage.setItem("funColor2",  colors[globalCount][1])
}
