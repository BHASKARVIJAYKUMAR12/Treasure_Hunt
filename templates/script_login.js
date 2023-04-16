const form = document.querySelector("#login-form");

form.addEventListener("submit", function(event) {
  event.preventDefault();
  
  const email = document.querySelector("#email").value;
  const password = document.querySelector("#password").value;
  
  // Do something with the form data, such as send it to a server
  console.log(email, password);
});
