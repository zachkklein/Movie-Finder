//help used for scroll visual effect: https://alvarotrigo.com/blog/css-animations-scroll/
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
  // end scroll section

  //Makes form move left when submitted
  const getRecommendationsBtn = document.getElementById('getRecommendationsBtn');
  const formSection = document.getElementById('formSection');
  const recommendationsSection = document.getElementById('recommendations');

  getRecommendationsBtn.addEventListener('click', function(event) {
      // event.preventDefault();  // Prevent form submission POSSIBLE ISSUE NEED TO FIX!!!

      // Move the form section to the left
      formSection.style.transform = 'translateX(-55%)';

      

      // Display the recommendations section
      recommendationsSection.style.display = 'block';
      form.submit();
      
  });

$(document).ready(function() {
        $('#recommendation-form').submit(function(event) {
            // Prevent the default form submission
            event.preventDefault();

            // Get the form data
            var formData = $(this).serialize();

            // Send the AJAX request to the server
            $.ajax({
                type: 'POST',
                url: '/recommendations',
                data: formData,
                success: function(response) {
                    // Update the recommendation-results div with the response
                    $('#recommendation-results').html(response);
                },
                error: function(error) {
                    // Handle any errors here
                    console.log('Error:', error);
                }
            });
        });
    });