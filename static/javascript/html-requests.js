/**
 * Determines if the current request is an asynchronous request or not
 * Defaults to an asynchronous request
 * @param {boolean} isAsync
 * @returns {boolean}
 */
function isAsyncRequest(isAsync) {
  if (isAsync === undefined || typeof isAsync !== 'boolean') {
    return true;
  }
  return isAsync;
}

/**
 * Executes a HTML POST request using XMLHttpRequest
 * Returns the string value of the response from the server
 * @param {string} serverUrl
 * @param {FormData} formData
 * @param {boolean} asyncRequest
 * @param {function} callback
 * @returns {string}
 */
function postRequest(serverUrl, formData, asyncRequest, callback) {
  /* By default use an async request unless otherwise stated */
  var isAsync = isAsyncRequest(asyncRequest);
  var xhttp = new XMLHttpRequest();
  /* Send the POST request */
  xhttp.open('POST', serverUrl, isAsync);
  xhttp.send(formData);
  /* Set the response from the server */
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200 && callback) {
      return callback(xhttp.responseText);
    }
  };
}
