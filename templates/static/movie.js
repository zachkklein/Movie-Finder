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

  //Makes form move left when submitted
  const getRecommendationsBtn = document.getElementById('getRecommendationsBtn');
  const formSection = document.getElementById('formSection');
  const recommendationsSection = document.getElementById('recommendations');

  getRecommendationsBtn.addEventListener('click', function(event) {
      event.preventDefault(); // Prevent form submission POSSIBLE ISSUE!!!

      // Move the form section to the left
      formSection.style.transform = 'translateX(-55%)';

      // Display the recommendations section
      recommendationsSection.style.display = 'block';
      
  });