/**
 * Handles a document click - this will hide any previously visible dropdown menu item containers
 * @param {Event} event 
 */
function handleDocumentClick(event) {
  var prevExpandedDropdownMenuItem;
  if (event.target.classList.contains('menu-bar-item-content') === false) {
    /* Clicked on the document - ensure any previously opened menu items are found and marked as hidden */
    var dropdownMenuItems = document.querySelectorAll('div[class="menu-bar-item-content"][data-expanded]');
    var index = 0;
    var foundExpandedMenuItem = false;
    while (index < dropdownMenuItems.length && foundExpandedMenuItem === false) {
      if (dropdownMenuItems[index].getAttribute('data-expanded') === 'true') {
        prevExpandedDropdownMenuItem = dropdownMenuItems[index];
        foundExpandedMenuItem = true;
      }
      index += 1;
    }
  }
  if (event.target.classList.contains('menu-bar-item-content') === true && event.target.getAttribute('data-expanded') === 'false') {
    /* Another dropdown menu item has been clicked - ensure any previously opened menu items are found and marked as hidden */
    prevExpandedDropdownMenuItem = document.querySelector('div[class="menu-bar-item-content"][data-expanded="true"]');
  }
  if (prevExpandedDropdownMenuItem !== undefined) {
    /* A previously opened menu item has been found - trigger a click event on it to hide it */
    prevExpandedDropdownMenuItem.dispatchEvent(new Event('click'));
  }
}

/**
 * Handles clicking on a dropdown menu item which marks the relevant dropdown menu container as visible / hidden
 * @param {Event} event 
 */
function handleDropdownMenuItemClick(event) {
  event.preventDefault();
  var menuItem = event.target;
  var menuItemExpanded = menuItem.getAttribute('data-expanded');
  var dropdownMenuContainerId = '' + menuItem.parentNode.getAttribute('id') + '-content-parent';
  var dropdownMenuContainer = document.querySelector('div[id="' + dropdownMenuContainerId + '"]');
  if (menuItemExpanded === 'true') {
    /* Hide the dropdown menu container */
    event.stopPropagation();
    dropdownMenuContainer.style.transition = 'none';
    dropdownMenuContainer.style.opacity = 0;
    menuItem.setAttribute('data-expanded', 'false');
    document.removeEventListener('click', handleDocumentClick, { capture: true });
  } else {
    /* Show the dropdown menu container */
    dropdownMenuContainer.style.transition = 'opacity 0.3s ease-in-out';
    dropdownMenuContainer.style.opacity = 1;
    event.target.setAttribute('data-expanded', 'true');
    document.addEventListener('click', handleDocumentClick, { capture: true });
  }
}

/**
 * Sets the dropdown menu container position for each of the dropdown menus
 * identified by the menu item id and the dropdown container id
 * @param {string} menuItemId 
 * @param {string} dropdownContainerId 
 */
function setDropdownMenuContainerPosition(menuItemId, dropdownContainerId) {
  /* Find the boundaries of the parent menu item for this component */
  const parentMenuItemElement = document.querySelector('div[id="' + menuItemId + '"]');
  const parentMenuItemElementBoundary = parentMenuItemElement.getBoundingClientRect();
  /* Find the boundaries for the container element itself */
  const containerElement = document.querySelector('div[id="' + dropdownContainerId + '"]');
  const containerElementBoundary = containerElement.getBoundingClientRect();
  /* Ensure all children menu items are at least as wide as their parent menu item */
  if (containerElementBoundary.width < parentMenuItemElementBoundary.width) {
    containerElement.style.width = '' + parentMenuItemElementBoundary.width + 'px';
  } else {
    containerElement.style.width = '' + containerElementBoundary.width + 'px';
  }
  containerElement.style.minWidth = containerElement.style.width;
  /* Determine if the leftmost position of the children menu items needs to be adjusted to fit the screen size */
  let leftmostPosition = parentMenuItemElementBoundary.left;
  if (parentMenuItemElementBoundary.left + containerElementBoundary.width > window.innerWidth) {
    leftmostPosition = window.innerWidth - containerElementBoundary.width;
  }
  /* Set the top and left positions for this element */
  containerElement.style.top = '' + parentMenuItemElementBoundary.bottom + 'px';
  containerElement.style.left = '' + leftmostPosition + 'px';
}

/**
 * Sets all of the dropdown menu container positions
 */
function setAllDropdownMenuContainerPositions() {
  setDropdownMenuContainerPosition('menu-item-plants', 'menu-item-plants-content-parent');
}

/* Ensure the dropdown menu containers are always adjusted on screen resize event */
window.addEventListener('resize', setAllDropdownMenuContainerPositions, { capture: true });
