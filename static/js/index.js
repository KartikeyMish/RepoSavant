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