document.addEventListener('DOMContentLoaded', function () {
    // JavaScript code to change the button text to "Analyzing" when clicked
    document.getElementById('submitButton').addEventListener('click', function (event) {
        // Prevent the default form submission behavior
        event.preventDefault();
  
        // Get the input value
        const input = document.querySelector('input[name="username"]').value;
  
        // Check if the input is not empty and valid (you can add your validation logic here)
        if (input.trim() !== '') {
            // Change the button text to "Analyzing"
            document.getElementById('submitButton').textContent = 'Analyzing';
  
            // Submit the form (you can remove this line if you don't want to submit the form)
            document.querySelector('form').submit();
        } else {
            // Handle invalid input (e.g., show an error message)
            alert('Please provide a valid input.');
        }
    });
  });

//   document.addEventListener("DOMContentLoaded", function () {
//     const loadingOverlay = document.getElementById("loading-overlay");
//     const form = document.querySelector("form");
//     const submitButton = document.getElementById('submitButton');

//     form.addEventListener("submit", function (event) {
//         // Prevent the default form submission behavior
//         event.preventDefault();

//         // Get the input value
//         const input = document.querySelector('input[name="username"]').value;

//         // Check if the input is not empty and valid (you can add your validation logic here)
//         if (input.trim() !== '') {
//             // Disable the submit button to prevent multiple submissions
//             submitButton.disabled = true;

//             // Change the button text to "Analyzing"
//             submitButton.textContent = 'Analyzing';

//             // Show the loading animation
//             loadingOverlay.style.display = "flex";

//             // Submit the form (you can remove this line if you don't want to submit the form)
//             document.querySelector('form').submit();
//         } else {
//             // Handle invalid input (e.g., show an error message)
//             alert('Please provide a valid input.');
//         }
//     });

//     // You can also hide the loading animation when you receive the result, for example:
//     // Replace this with your actual logic to check for the result
//     const resultElement = document.querySelector(".result");
//     if (resultElement) {
//         // Hide the loading animation when the result is displayed
//         loadingOverlay.style.display = "none";
//     }
// });
