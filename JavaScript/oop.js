// oop (Object Oriented Programming) in JavaScript
//Objects, classes, inheritance, encapsulation, abstraction and polymorphism are key concepts in OOP.
// OOP is a programming paradigm that uses objects and classes to structure code.
// It allows for encapsulation, inheritance, and polymorphism, making code more modular and reusable
//Object: An instance of a class that contains properties and methods. For example, a car object might have properties like color and model, and methods like start and stop. These are arrays, strings, functions in js,
// Two ways to create an object in JavaScript:
// 1. Object Literal Notation
//Example
let person = {   //the object is "person"
    //Properties: key-value pairs that define the object's attributes
    name: "John",
    age: 30,
    //Methods: functions within an object that define the object's behavior
    get_function: function() {       //get_function is a key, and the function is the value
        return(`The name of person is: ${person.name}`);
    },
    //Object within an object
    phone_number: {
        home: 123-456-7890,
        work: 198-765-4321,
    }
};
console.log(person.get_function()); // Accessing the method of the object
console.log("The home number is:" + person.phone_number.home); // Accessing the nested object property
// 2. Object Constructor Function
