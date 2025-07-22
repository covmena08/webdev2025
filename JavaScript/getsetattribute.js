//methods to get and set attributes in JavaScript
//getAttribute("attributeName") and setAttribute("attributeName", "value")
let firstAttribute = document.getElementById("first");

//Getting the value of the "class" attribute
let idValue = firstAttribute.getAttribute("id");
document.writeln(idValue);

//Example 2: where there are multiple 
let secondAttribute = document.getElementById("html");
//Getting the value of the "lang" attribute
let secondValue = secondAttribute.getAttribute("lang");
document.writeln("<br><hr>", secondValue);

//Setting attributes on elements
let para= document.getElementById("para");
//Setting new attributes
para.setAttribute("class", "style"); // Sets the "class" attribute to "style"
para.setAttribute("name"); 


//Task 1: Read on how to remove attributes: https://www.w3schools.com/jsref/met_element_removeattribute.asp
//Removing attributes: removeAttribute("attributeName")
para.removeAttribute("name"); //Removes the "name" attribute from the element

//Task 2: Read on adding new elements to the DOM: https://www.w3schools.com/jsref/met_document_createelement.asp
//Adding a new element to the DOM
let newElement = document.createElement("div"); // Creates a new div element
newElement.setAttribute("id", "newDiv"); // Sets an id attribute for the new element
newElement.textContent = "This is a new div element"; // Adds text content to the new element
document.body.appendChild(newElement); // Appends the new element to the body of the document

//Task 3: Read on navigating between the DOM nodes i.e accessing the child nodes: https://www.w3schools.com/jsref/dom_nodes.asp
//Navigating between DOM nodes
let parentElement = document.getElementById("parentDiv"); // Selecting a parent element
let childNodes = parentElement.childNodes; // Getting all child nodes of the parent element
document.writeln("<br><hr>Child Nodes: ", childNodes.length); // Displaying the number of child nodes