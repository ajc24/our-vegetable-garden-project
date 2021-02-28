/* Form JSON data */
var formJson = {
  autofocus: 'name',
  fileInput: [
    'photo'
  ],
  textInput: [
    'name',
    'variety'
  ],
};

/**
 * Onload event to ensure all form fields are cleared each time
 * the page is refreshed / reloaded
 */
window.onload = function() {
  clearFormData(formJson);
}

/**
 * Submits the form and POSTs the data to the server side
 */
function submitForm() {
  var formData = new FormData();
  formData.append('name', getCleanInputValue(formJson.textInput[0]));
  formData.append('variety', getCleanInputValue(formJson.textInput[1]));
  formData.append('photo', getFileUpload(formJson.fileInput[0]));
  postRequest('/submitaddaplant', formData, true, function(response) {
    alert(response);
    clearFormData(formJson);
  });
}
