document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const loader = document.getElementById("loader");

    form.addEventListener("submit", function () {
      // Show the loader when the form is submitted
      loader.style.display = "inline-block";
    });
  });