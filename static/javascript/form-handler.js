/**
 * Clears all of the form data from any screen
 * @param {{ autofocus: string, fileInput: Array.<string>, textInput: Array.<string> }} formJson
 */
function clearFormData(formJson) {
  /* Clear all of the file inputs in the form */
  for (var index = 0; index < formJson.fileInput.length; index += 1) {
    document.getElementById(formJson.fileInput[index]).value = '';
  }
  /* Clear all of the text inputs in the form */
  for (var index = 0; index < formJson.textInput.length; index += 1) {
    document.getElementById(formJson.textInput[index]).value = '';
  }
  /* Set the autofocus to the desired element */
  document.getElementById(formJson.autofocus).focus();
}

/**
 * Retrieves the cleaned up input value from the specified input field
 * The input field is identified by ID
 * @param {string} inputId
 * @returns {string} 
 */
function getCleanInputValue(inputId) {
  var rawValue = document.getElementById(inputId).value.trim();
  while (rawValue.indexOf('  ') > -1) {
    rawValue = rawValue.replace('  ', ' ').trim();
  }
  return rawValue;
}

/**
 * Retrieves the file uploaded by the user
 * @param {string} inputId
 * @returns {File}
 */
function getFileUpload(inputId) {
  return document.getElementById(inputId).files[0];
}

/**
 * Handles user input into the relevant form fields
 * @param {string} inputId 
 * @param {string} newInputValue 
 */
function handleUserFormInput(inputId, newInputValue) {
  document.getElementById(inputId).value = newInputValue;
}
