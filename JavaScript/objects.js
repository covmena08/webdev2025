// Objects= a collection of named values, called properties
// Objects are complex variables that allow us to store more than 1 value or a group of values under a single variable name but the difference between objects and arrays is that objects are unordered collections of key-value pairs, while arrays are ordered collections of values.
// Objects are created using curly braces {} with optional properties (key-value pairs) listed inside.
// The key is ALWAYS a string and the value can be any datatype (string, number, boolean, array, object, function, etc.) even a method (function inside an object).
/* Syntax: let objectName = {
key: value,
key: value,
key: value
}; */
//objectName is the name of the object, property1, property2, ... are the properties of the object, value1, value2, ... are the values of the properties

let person = {
name: "John Doe",
age: 25,
gender: "Male",
phone: 8012345678,
//Calling a method of an object
display: function() {
    console.log(this.name);} //this function is used to display the name property of the person object
};
//console.log(person); //displays the properties of person object in the console

//Displaying a specific property of the object;
//With dot notation
//console.log(person.name); //displays the name property of the person object
//With square brackets notation
//console.log(person["age"]); //displays the age property of the person object

//Setting object properties
//Syntax: objectName.propertyName = value;
person.country = "China"; //adds a new property to the person object
//console.log(person.country); //displays the country property of the person object

//Updating an existing property of an object
person.age = 30; //updates the age property of the person object
//console.log(person.age); //displays the updated age property of the person object

//Deleting a property from an object
delete person.gender; //deletes gender property from the person object
//console.log(person); //displays the person object without the gender property
//Calling a method of the object
person.display(); //calls the display method of the person object with dot notation
person["display"](); //calls the display method of the person object with square brackets notation



/*//display: function(){
//console.log(this.name);   //this keyword is used to refer to the current object
//console.log(person);
//console.log(person.name); //displays the name property of the person object
// console.log(person["name"]); //square brackets notation to access the name property of the person object
// Setting object properties
person.country = "China"; //adds a new property to the person object
//console.log(person.country);

//Updating an existing property of the object
person.age = 30; //updates the age property of the person object
//console.log(person.age); //displays the updated age property of the person object
delete person.gender;
// console.log(person);
// person.display(); //calls the display method of the person object //dot notation
person["display"](); //square brackets notation*/

