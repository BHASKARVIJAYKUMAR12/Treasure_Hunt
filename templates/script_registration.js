const form = document.querySelector("#registration-form");

form.addEventListener("submit", function(event) {
  event.preventDefault();
  
  const name = document.querySelector("#name").value;
  const email = document.querySelector("#email").value;
  const password = document.querySelector("#password").value;
  
  // Do something with the form data, such as send it to a server
  console.log(name, email, password);
});
