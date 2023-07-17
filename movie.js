//help used for scroll: https://alvarotrigo.com/blog/css-animations-scroll/
function reveal() {
    var reveals = document.querySelectorAll(".reveal");
    for (var i = 0; i < reveals.length; i++) {
      var areaHeight = window.innerHeight;
      var areaTop = reveals[i].getBoundingClientRect().top;
      var areaVisible = 150;
      if (areaTop < areaHeight - areaVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }
  
  window.addEventListener("scroll", reveal);