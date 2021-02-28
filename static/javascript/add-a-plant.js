/**
 * Onload event to ensure all form fields are cleared each time
 * the page is refreshed / reloaded
 */
window.onload = function() {
  document.getElementById('name').value = '';
  document.getElementById('variety').value = '';
}

/**
 * Handles user input into the relevant form fields
 * @param {string} inputFieldId 
 * @param {string} newInputValue 
 */
function handleUserFormInput(inputFieldId, newInputValue) {
  document.getElementById(inputFieldId).value = newInputValue;
}

/**
 * Submits the form and POSTs the data to the server side
 */
function submitForm() {
  var formData = new FormData();
  formData.append('name', document.getElementById('name').value.trim());
  formData.append('variety', document.getElementById('variety').value.trim());
  postRequest('/submitaddaplant', formData, true, function(response) {
    alert(response);
  });
}
