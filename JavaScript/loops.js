//Loops: it execute a block of code multiple times until a specified condition is met.
//Types of loops in JavaScript:
// 1. While loop=loops through a block of code as long as the specified condition is true.
//Syntax:
/*while (condition) {
    // code to be executed
}*/

// Example:
let i = 1;
while (i < 5) {
    //console.log(i);
    i++;   //post-increment operator to increase the value of i by 1 before the next iteration
}

// 2. Do...while loop= it evaluates the condition AFTER executing the block of code, ensuring that the code runs at least once. The loop continues until the condition evaluates to false.
// Syntax:
/*do {
    // code to be executed
} while (condition);*/

// Example:
let j=3;
do {
    //console.log(j);
    j++;
} while (j < 5);

//Task: write a while loop that decrements the value of variable by 1 and prints value in console. The max value of the variable should be 10.
//Task2: Repest the above using do...while loop

//Task 1:
let vari=8;
while(vari>5){
   // console.log(vari);
    vari--;
}

//Task2:
let var2=9
do{
    //console.log(var2);
    var2--;
}while(var2>5);
// 3. For loop= Repeats a block of code as long as a certain condition is met. It loops trough a block of code until the counter reaches a specified number
//Syntax:
/* for(initialization; condition; increment){       //initialization=used to initialize the counter variables and evaluated once unconditionally before the first exection of the body of the loop
code to be exercuted
}*/

//condition= evaluated at the beginning of each iteration, if T the loop statements execute if not exection of loop stops
//incremnet=updates the loop counter with a new value each time the loops runs
//Example:
for(let a=1; a<=5; a++){
    //console.log(`Count ${a}`);
}//console: 1,2,3,4,5

//Task:Write a for loop that decrements a variable and checks if the count is 0 or greater
for(let b=10; b<=6; b--){
   // console.log(`Count ${b}`);
}
//Application
let teams= ["Manchester", "Arsenal", "Liverpool", "Bayern", "Ferencvaros", "Barcelona"]
//loop through the teams array
for(let t=0; t<teams.length; t++){
    //console.log(`Team Name: ${teams[t]}`);
}


//Task: Use the for loop to display the 1st 4 items of an array with the length of 7
//use this array: [23, 92, 45, 93, 12, 37, 67]
let num=[23, 92, 45, 93, 12, 37, 67];
for(let n=0; n<4; n++){
    console.log(`Number: ${num[n]}`);
}
// 4. For...in loop=Iterates/Repeats through the properties of an object or the elements of an array. 
//Syntax:
/* for (variable in object) {
    // code to be executed
}*/
// The variable/loop counter is a STRING and not a number it contains the name of a certain property of the object or the index of an array element.
// Example:
let student = {
    name: "John",
    age: 30,
    email: "john@nextstep.org"
};
for (let varSt in student) {
    //console.log(`${varSt}: ${student[varSt]}`);  //variable=counter=name of the property in object(varSt), student[varSt]=value of the property
}

//Example 2(Array): 
let fruitArray = ["Apple", "Banana", "Cherry", "Date"];
for (let fruit  in fruitArray) {
    //console.log(`${fruit}: ${fruitArray[fruit]}`);  //counter(fruit)=index of the array(0,1,2,3,), fruitArray[fruit]=value of the element at that index
}

// 5. For...of loop= allows us to iterate over iterable objects like arrays, strings, maps, sets, etc. It iterates through the values/element of an iterable object/array.
//Syntax:
/* for (variable of object) {
    // code to be executed
}*/

//Example:
for (let varTrial of fruitArray) {
    //console.log(varTrial);  //variable(varTrial)=value of the element in the array
}
// Here the variable is not an index but the value of the element in the array or in a case of an object the value of the property, in case of a string it is the character at that index.
// Example 2:
let sentence= "The quick brown fox jumps over the lazy dog";
for (let varSentence of sentence) {
    //console.log(varSentence);  //variable(varSentence)=character at that index in the string
}

    