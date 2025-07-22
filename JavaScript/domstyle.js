
//Selecting an element
let elementSelection = document.getElementById("firstPara");

//Applying styles to the above selected element
elementSelection.style.color="red";
elementSelection.style.fontSize="20px";
elementSelection.style.fontWeight="bold";

//Selecting the element
let elementTwo = document.getElementById("secondPara");

/*Getting the styling information from the element
document.write(elementTwo.style.color,"<br>");
document.write(elementTwo.style.fontSize,"<br>");
document.write(elementTwo.style.fontFamily,"<br>");*/

//Using the className Property to Replace or Add CSS classes
//Selecting the element
let elementThree = document.getElementById("firstDiv");
//Replacing the  "disabled" class
//elementThree.className= "enabled"; //Replacces all classes of firstDiv with "enabled"
//Adding a new class to new class "enabled"
//elementThree.className += " highlight"; //Adds the class "highlight" to the existing classes. Withot space after first double quotes it would merge 'enabled class with new one: "highlight"= "enabledhighlight"

//Using the Classlist Property to Add or remove CSS classes
// Selecting the element
let elementFour = document.getElementById("secondDiv");
//Adding a new class
elementFour.classList.add("warning"); //Adds new class ( no space needed)
elementFour.classList.add("two", "three", "four"); //Adding multiple new classes
//Removing a class
//elementFour.classList.remove("three"); //Remove one class
//elementFour.classList.remove("four", "warning"); //Removes multiple classes

//Task: Add 3 classes to the firstDiv using classList property, then style the classes as below: 
// First color: green
// Second border: 10px solid color
// Third font-size: 40px
// Lastly, using the classList method remove the third class

elementThree.classList.add("green", "border", "largeFont");
elementThree.classList.remove("largeFont");



