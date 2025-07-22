const prompt = require('prompt-sync')(); // Importing the prompt-sync module to use prompt in Node.js
//Conditional Statements in JavaScript
//Types of conditional statements: if statement, if...else statement, if...else if...else statement, switch....case statement
//If Statement
//Syntax: if(condition) {
// // code to be executed if condition is true
// }
//Example of if statement
let num = 10;
//Condition1: if number is greater than 0 it is positive
if(num > 0) {
    console.log("The number is positive");
}
//Condition2: if the modulus of the number is 0 then its even
if(num % 2 == 0) {  // The identical operator means that the value and datatype of the left operand is equal to the value and datatype of the right operand/ This a modulus operator, it returns the remainder of the division of num by 2.
    console.log("The number is even");
}
if(num % 2 !== 0) {  // The not identical operator 
    console.log("This number is even" ); // This will not be executed in the console because the number is even, so the condition is false
} 

//If...else statement
//Syntax: if(condition) {
// // code to be executed if condition is true
// } else {
// // code to be executed if condition is false
// }
//Example of if...else statement
//Conditiion: if age is greater than or equal to 18 then display "Adult" else display "Minor"
let age=20;
if(age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}

//Task: write an if...else statement to fufill the following conditions: 
//If a student scores 80 or higher theen display "Pass" else display "Fail"
/*let score = 85;
if(score>=80){
    console.log("Pass");
} else{
    console.log("Fail");
}*/
//If...else if...else statement 
//Syntax: if(condition1) {
// // code to be executed if condition1 is true
// } else if(condition2) {
// // code to be executed if condition2 is true
// } else if(condition3) {
// // code to be executed if condition3 is true
// } else {
// // code to be executed if all conditions are false
// }

//Task for if...else if...else statement;
//Create a simple grading system that assigns the following grades:
//Grade A: 80 and above
//Grade B: 60 to 79
//Grade C: 40 to 59
//Below 40: Fail

let point=65;
if(point >= 80 && point <= 100){ //&& is the logical AND operator, it checks if both conditions are true
    console.log(point, ": Grade A!!!");
}else if (point >= 60 && point <= 79){
    console.log(point,": Grade B!!!");
}else if (point >= 40 && point <= 59){
    console.log(point,": Grade C!!!");
}else if (point < 40 && point >= 0){ //&& is the logical AND operator, it checks if both conditions are true
    console.log(point,": Fail!!! :(");
}else{
    console.log(point,": Invalid score!!!"); // This will be executed if the score is not a number or is negative
}

/*let displayAge = 23;
console.log("Your age is: " + displayAge); //This will display "Age is: 23" in the console
//Or
console.log(`Your age is: ${displayAge}`); //This will also display "Age is: 23" in the console*/

//Task: write an if...else if...else statement write a program the checks the following conditions:
// If x > 0 then display "Positive", if x < 0 then display "Negative", else display "Zero"
/* let x=-8;
if (x>0){
    console.log(x, "is Positive");
} else if (x<0){
    console.log(x, "is Negative");
}else{
    console.log(x, "is Zero");
}*/

/*const userName = prompt('Enter your name: '); //This will prompt the user to enter their name
console.log(`Welcome ${userName}! This is the Web Development class!`); */


//Nested if...else statement

/*
let weather = prompt('Enter the weather (sunny or rainy): '); 
//Prompting user to enter the weather and converting it to lowercase
let temperature= prompt('Enter the temprature outside: ');

if (weather==="sunny"){
    if (temperature > 30) {  //Nested if...else statement to check the temperature
        console.log("It's a very hot and sunny day, consider carrying a water bottle!");
    } else if (temperature > 20) {
        console.log("It's a warm and sunny day, dress accordingly!");
    } else {
        console.log("It's a bit cool outside, consider warmer clothing!");
    }
} else if (weather==="rainy"){
    console.log("It's a rainy day, don't forget your umbrella!");
} else {
    console.log("Kindly check the weather forecast!");
}
*/
//Switch...case statement
//Switch...case statement is used to execute one block of code among many options based on the value of a variable or expression.
//Syntax: switch(variable/expression) {
// case value1:
// // code to be executed if variable/expression is equal to value1
// break; // breaks out of the switch statement
// case value2:
// // code to be executed if variable/expression is equal to value1
// break; // breaks out of the switch statement
// case value3:
// // code to be executed if variable/expression is equal to value1
// break; // breaks out of the switch statement
// default:
// // code to be executed if variable/expression does not match any case
// break; // breaks out of the switch statement
// }

//Example of switch...case statement
let mark= parseInt(prompt('Enter student"s mark: ')); //
console.log(typeof( mark)); //Displaying the datatype of the variable mark in the console


let grade;
switch(true){ // Using true as the expression to allow for range checking
    case mark >= 80 && mark <= 100:
        grade = "A";
        break;
    case mark >= 60 && mark <= 79:
        grade = "B";
        break;
    case mark >= 40 && mark <= 59:
        grade = "C";
        break;
    case mark >= 20 && mark <= 39:
        grade = "D";
        break;
    case mark >= 0 && mark <= 19:
        grade = "Fail";
        break;
    default:
        grade = "Undefined"; // This will be executed if the mark is not a number or is negative
        break;
}
console.log(`The grade for ${mark} is ${grade}`); //This will display the grade in the console based on the mark entered by the user

let fruit = prompt('Enter a fruit (apple, banana, orange): '); //Prompting user to enter a fruit and converting it to lowercase
switch(fruit.toLowerCase()){ // Using fruit variable to check the value of the variable fruit
    case "apple":
        console.log("An apple costs 200ft/piece!"); // This will be executed if the fruit is apple
        break;
    case "banana":
        console.log("A banana costs 200ft/piece!");
        break;
    case "orange":
        console.log("An orange costs 200ft/piece!");
        break;
    
    default:
        console.log(`We do not have ${fruit} in stock!`); // This will be executed if the fruit is not apple, banana, or orange
        break;
}
