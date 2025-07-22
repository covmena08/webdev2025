//console.log("Hello, World!"); //de(bug)
//Variable Declaration
// Syntax: var keyword, varriable name, assignment operator, value;
// var nextstep = 10;
var nextstep = 10;//number
console.log(nextstep); //console.log(variable name);
var name = "John Doe"; //String
console.log(name); //console.log(variable name), name is crossed out because it is in library like var, or let, or const
var isGood = false; //Boolean i.e. true or false
console.log(isGood);

//Using let keyword
let nextStep = 25; //let keyword is used to declare a variable that can be changed later,   //nextStep doesnt equal nextstep above, because JavaScript is case sensitive
let next = "25";
console.log(nextStep);
console.log(next);
// Values "25" and 25 are two different data types ome is a number the other a string
/*
Display the word Easy in the console.
The console should display the word stored in a variable called trial using the let keyword
*/

let trial = "Easy";
console.log(trial);

/* const is a keyword used to declare a variable that cannot be changed later, they are constant throughout the lifetime of an app or during program execution
const syntax: const variableName=value;
*/
const pi = 3.14; //pi is a constant
console.log(pi);

/* Datatypes (primitive);
-Strings
- Numbers
- Boolean
- Undefined
- Null 
- Symbol
*/
//Numbers
let n = 18;
let s1 = "a, b,c, d"

//Boolean
let bool = true;
//Undefined
let notDefined;
// Null
let empty = null;

/*Non-Primitive Datatypes;
- Objects
- Arrays
- Functions*/
//Object
//Syntax: declaration objectName={ key:value, key:value}
let lenin={
    name:"Lenin", //String-->quotations
    phone: 3627467, //Number-->no quotations
    email: "lenin@gmail.com", //String-->quotations
};
//console.log(lenin)
//Arrays
let fruitArray=["Banana", "Mango", "Broccoli"];
console.log(fruitArray)
//Functions
//Syntax: function functionName{code}--->NO SEMI-COLUMN9

