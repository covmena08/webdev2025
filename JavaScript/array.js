// Arrays are complex variables that allow us to store more than 1 value or a group of values under a single variable name
// Syntax: let arrayName = [value1, value2, value3, ...];  // indexing //dot notation

let cities = ["Lagos", "Abuja", "Port Harcourt", "Ibadan", "Enugu"]; //Array of strings
let fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple"]; 
let students = ["John", "Jane", "Mary", "Peter", "Paul"]; 
let items = ["Henry", "henry@gmail.com", 1234567890, 30, 1995]; //Array of mixed data types (String, Number)
let numbers = [10, 23, 45, 67, 89, 97, 58, 45, 21, 129]; // Array of numbers

//console.log(cities); //console.log(arrayName); //displays array in the console
//console.log(cities[0]); //display the first element in the array; //indexing starts from 0, so cities[0] is Lagos
// console.log(cities.lenghth); //displays the length of the array; //length is a property of the array that returns the number of elements in the array
// console.log(cities[cities.length - 2]); //display the second to last element in the array;
//console.log(fruits);
fruits.push("strawberry");
//console.log(fruits);  //push() method is used to add a new element to the end of the array
//Removing elements from an array using the pop() method : let students = ["John", "Jane", "Mary", "Peter", "Paul"]; 
/* console.log(students); //Original array
console.log(students.length); //Displays the original length of the array //output: 5
students.pop(); //Removes the LAST element from the array
console.log(students); // array after removing the last element
console.log(students.length); //Displays the length of the array after removing the last element //output: 4*/ 


//Add or remove elements at any position in the array using the splice() method
//Syntax: arrayName.splice(startIndex, deleteCount, item1, item2, ...);// startIndex is the index at which to start adding/removing elements, deleteCount is the number of elements to be removed, item1, item2, ... are the elements to be added
//let numbers = [10, 23, 45, 67, 89, 97, 58, 45, 21, 129]; //Array of numbers above 
numbers.splice(0,  1); //removes one element (10) from the beginning of the array (index 0)
// console.log(numbers);

//Adding elements to (numbers) array using splice() method
numbers.splice(3, 0, "Jane", "Peter"); //adds "Jane" and "Peter" at index 3 without removing any element+
//console.log(numbers); //adds Jane and Peter to the 3rd index of the array;;


//MERGING 2 or more arrays using concat() method
//Syntax: arrayName1.concat(arrayName2, arrayName3, ...); //arrayName1 is the 1st array, arrayName2 is the 2. array, ... being merged as on array
// Example: joining fruits and studentss arrays
fruits.concat(students); //merges fruits and students arrays
console.log(fruits.concat(students)); //displays the merged array in the console, can also be used to display the merged array in the console directly without above line of code
//Or you can store the merged array in a new variable and display it
let concatenated = fruits.concat(students); //variable's value is the merged array of fruits and students 
console.log(concatenated); //concatenated=joined, displays the merged array in the console

// let concatenated = fruits.concat(cities); //merges fruits and cities arrays
// console.log(concatenated); //displays the merged array in the console