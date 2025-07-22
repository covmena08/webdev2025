// Function: a group of statements that peform specific tasks and can be kept maintained seperately from the main program.
// Syntax: functionKeyword functionName(parameter1, parameter2, ...) { 
// //function body= code to be executed goes here
//}
//Defining a function
function greetings(){
    console.log("Hello, World!");
}
// calling the function
// greetings(); //calls the greetings function, which displays "Hello, World!" in the console

//Parameters: are variables that are passed to a function when it is called. They allow us to pass values to the function so that it can use them in its code.
//Arguments: are the actual values that are passed to the function when it is called. They are the values that are passed to the parameters of the function.
//Function to add two numbers
/*function sum(num1, num2){ //num1 and num2 are parameters that are not yet given a value (arguments)
    let addition = num1 + num2;
    console.log(addition); //displays the sum of the two numbers in the console
}*/

/*sum(2,4);//arguements of parameters num1 and num2
sum(5, 7);
sum(1,9);
sum(34,68);*/

/* define a function that takes two parameters and performs either multiplication, division, or subtraction and returns the 
result. Give your function a name that relates to what it does*/

/*function multiplication(num1, num2){
    let multiplication = num1 * num2; 
    console.log(multiplication); 
}
multiplication(2, 4);
multiplication(5, 7);

function division(num1, num2){
    let division = num1 / num2; 
    console.log(division); 
}
division(2, 4);
division(21, 7);*/


//Placeholder/Default value for the undefined value of a parameter
/*function displayName(username="Guest"){
    console.log(username); //
} 
displayName(); //Since arguement of parameter 'username' is not given, it will display the default value "Guest"
displayName("Next Step"); //This will replace default value with "Next Step" in the console

//Making display more understandable to user by adding a message
let student="Damilia"; //may not make sense to user if we just display the name
let phone = 4635752864927
console.log("My name is:", student, "\n my phone number is:" phone); //This will display "My name is Damilia My phone number is 4635752864927 in the console*/


//Returning values from a function using the return statement
// Syntax: functionKeyword functionName(parameter1, parameter2, ...) {
// function body= code to be executed goes here
//ruturn value; 
//  }
//Example of a function that returns a value
//Return statement:. ..used to specify the value that a function should output/'return' to the caller of the function. The caller is the code that calls the function.
function getProduct(firstnum, secondnum){
    let product= firstnum * secondnum; //calculates the product of the two numbers
    return product; //returns the product to the caller
}
console.log("Our function has returned: ", getProduct(3, 4)); //This is the caller of the function "getProduct". It calls the getProduct function with arguments 3 and 4 in a PARANTHESIS!!!, which returns 8

//Excercise on return statement:
//create a function that returns the devision of two numbers
//create another function that takes two parameters and sums them up before returning the value. One of the parameters is the result of the function above. 
/* function divNumbers(num1, num2){
    let division=num1/num2;
    return division; //returns the division of two number (parameters that isn't yet given a value (arguments)) to the caller
}

function sumNumbers(num3, num4){
    let sum=num3+num4;
    return sum; //returns the sum of two numbers (num3 and num4) to the caller
}
let num3= divNumbers(10, 2); //  10/2=5, this is the caller of the function "divNumbers". It calls the divNumbers function with arguments 10 and 2 in a PARANTHESIS!!!, which returns 5
console.log(sumNumbers(num3, 5)) //This will display 10 in the console, since num3=5 and 5+5=10
//OR
console.log(sumNumbers(divNumbers(10, 2), 5)); //This will also display 10 in the console, since divNumbers(10, 2) returns 5 and 5+5=10*/

//Excercise on return statement:
//Create 3 functions The 1st function returns the sum of 2 numbers, the 2nd returns the difference of 2 numbers, the 3rd takes two parameters, that are the result of the firt two functions and returns the product. Product =multiplication of the two parameters.

function f1(num1, num2){
    let sum = num1 + num2;
    return sum; //returns the sum of two numbers (num1 and num2) to the caller
}
function f2(num3, num4){
    let difference = num3 - num4;
    return difference; //returns the difference of two numbers (num3 and num4) to the caller
}
function f3(num5, num6){
    let product = num5 * num6;
    return product; //returns the product of two numbers (num5 and num6) to the caller
}
let num5=f1(6, 2); // 6+2=8, this is the caller of the function "f1". It calls the f1 function with arguments 6 and 2, which returns 8, so num5=8
let num6=f2(6, 2); // 6-2=4, this is the caller of the function "f2". It calls the f2 function with arguments 6 and 2, which returns 4, so num6=4
console.log(f3(num5, num6)); //This will display 96 in the console, since num5=8 and num6=4, so 8*4=32
//OR
console.log(f3(f1(6, 2), f2(6, 2))); //This will also display 32 in the console, since f1(6, 2) returns 8 and f2(6, 2) returns 4, so 8*4=32

//Revision
/* function divideNumbers(dividend, divisor){
    let quotient = dividend / divisor; //calculates the quotient of the two numbers
    let arrayResult= [dividend, divisor, quotient]; //creates an array with the dividend, divisor, and quotient
    return arrayResult; //returns the array to the caller
}
let all = divideNumbers(10, 2); //We store our function in a variable.
console.log(all); //This will display the array [10, 2, 5] in the console, because dividend=10, divisor=2, and quotient=10/2=5
console.log(all[1]); //This will display 2 in the console, which is the divisor, the one at index 1 of the array
console.log(all[0], 'divided by', all[1], 'is', all[2]); //This will display "10 divided by 2 is 5" in the console, since dividend=10, divisor=2, and quotient=5--> user friendly*/

//Function Expression: a function that is defined and assigned to a variable. It can be anonymous or named.
//Syntax: let variableName = function(parameter1, parameter2, ...) {
// //function body= code to be executed goes here
//  }+



//Function Declaration
function getSum (a, b){
    let total= a + b; //calculates the sum of the two numbers
    return total; //returns the sum to the caller
}
//console.log(getSum(5, 3)); //This will display 8 in the console, since 5+3=8

//Function Expressions
let getDifference = function(c, d){
    let difference = c - d; //calculates the difference of the two numbers
    return difference; //returns the difference to the caller
}
//console.log(getDifference(5, 3)); //This will display 8 in the console, since 5+3=8
//OR 
let varSum=getDifference(5, 3); //A variable is like a store where you can store different datatypes.
console.log(varSum); 

//Variable Scope
// Local Variable
function salutation(){
    let greet= "How are you?"; //This is a local variable, it can only be accessed within this function
    return greet; 
}
console.log(salutation()); //This will display "How are you?" in the console, since greet is a local variable that can only be accessed within the salutation function
console.log(greet); //This will throw an error, since greet is a local variable and cannot be accessed outside the salutation function

//Example2
function animal(){
    let dog= "I am a local dog";
    return dog;
}
console.log(animal()); //To access the local variable dog we must call it through the function where it was defined (animal)
let dog="I am a global dog"; //This is a global variable, it can be accessed anywhere in the program
console.log(dog); //This will display "I am a global dog" in the console, since dog is a global variable that can be accessed anywhere in the program


// Global Variable
let greet2= "Hello, World!"; //This is a global variable, it can be accessed anywhere in the program


