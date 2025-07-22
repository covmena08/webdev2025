//Operators
//Types of operators: Arthmetic, Assignment, String, Logical, Comperison, Increment&Decrement operators
//Arithmetic Operators (5--> + addition, - subtraction, * multiplication, / division, % modulus)
let num1 = 10;
let num2 = 5;
//console.log(num1+num2); //addition
//console.log(num1-num2); //subtraction
//console.log(num1*num2); // multiplication
//console.log(num1/num2); // division
//console.log(num1%num2); // modulus

/* Declare two variables of your choice and assign 12 to the first variable and 4 to the second
 Use the above arithmetic operators to perform calculations as per the example above*/ 
 let Num1 = 12;
let Num2 = 4;
/*console.log(Num1+Num2); //addition
console.log(Num1-Num2); //subtraction
console.log(Num1*Num2); // multiplication
console.log(Num1/Num2); // division
console.log(Num1%Num2); // modulus*/

// Assigment Operators: = assign, += add&assign, -= subtract&assign, *= multiply&assign, /= divide&assign quotient, %= divide&assign modulus

let assignment; //Variable declaration
//Assign
assignment=10;
//console.log(assignment);//10
//add%assign
assignment+=5;
//console.log(assignment); //15
//subtract&assign
assignment-=2;
//console.log(assignment);//13
//multiply&assign
assignment*=2;
//console.log(assignment);//26
//divide&assign
assignment/=2;
//console.log(assignment); //13
//divide&assign modulus
assignment%=2;
//console.log(assignment); //1


// String Operators: + concatination, += concatination assignment
//Concatination
let string1="Hello"
let string2=" World!"
//console.log(string1+string2);
//Concatination Assignment
string1+=string2;
//console.log(string1);

let firstNum="10";
let secondNum="2";
//console.log(firstNum+secondNum);
//Task: concatinate and assign the above variables, firstNum and secondNum. firstNum should display the concatinated value. Hint firstNum will display 102
firstNum+=secondNum;
//console.log(firstNum);
/* Incrementing & Decrementing operators
- Pre-increment: ++x (first increments x by 1 and then returns new value of x) or post-increment:x++ (first returns value of x then increments x by 1)
(x=variable, ++=incrementing)
- Pre-decrement: --x (first decrements x by 1 and then returns new value of x) or post-decrement:x-- (first returns value of x then decrements x by 1) 
(x=variable, --=decrementing)
*/
let add; //variable declaration
add=10 // value assignment
/*console.log(add); //add=10
console.log(++add); //add=11
console.log(add++); //output: 11
console.log(add); //add=12*/

/* Declare a variable m and assign it a value of 2. Use the pre-incrementing and post-incrementing operators to perform calculations as per the example above*/
let m=2;
/*console.log(m); //output: m=2
console.log(++m); //output: m=3
console.log(m++); //output: 3
console.log(m); //output: m=4*/

let sub =20; //variable declaration
/*console.log(sub); //sub=20
console.log(--sub); //sub=19
console.log(sub--); //output: 19
console.log(sub); //sub=18*/

/*Comparison operators: ==, ===, !=, !==, >, <, >=, <= (used to compare 2 values in boolean expression; returns true or false)
- ==: equal to (compares only value)
- ===: indentical to (compares value and data type)
- !=: not equal to (compares only value)
- !==: not identical to (compares value and data type)
- >: greater than
- <: less than
- >=: greater than or equal to
- <=: less than or equal to
*/

let x=10, y=20, z="10"; //shorthand for declaring multiple variables
//Equal and Identical operators
//console.log(x==y); //output:false
//console.log(x==z); //output:true--> because it compares only value
//console.log(x===z); //output:false--> because it compares value and data type


//Not equal and Not identical operators
//console.log(x!=y); //output:true
//console.log(x!=z); //output:false-->compares only value
//console.log(x!==z); //output:true-->compares value and data type

//Less than and Greater than operators
//console.log(x < y); //output:true
//console.log(x < z); //output:false-->because their values are equal

//console.log(x > y); //output:false
//console.log(x > z); //output:false-->because their values are equal


//Less than or equal to and Greater than or equal to operators
//console.log(x <= y); //output:true
//console.log(x <= z); //output:true-->because their values are equal

//console.log(x >= y); //output:false
//console.log(x >= z); //output:true-->because their values are equal

/*Logical operators: &&, ||, ! (used to combine boolean expressions)
- &&: logical AND (returns true if BOTH operands are true)
- ||: logical OR (returns true if AT LEAST ONE operand is true)
- !: logical NOT (returns true if operand is false and vice versa)
*/
let A=10, B=20, C=30; //shorthand for declaring multiple variables


//AND operator
 if ((A<B) && (A<C)){
    //console.log("True"); //output:true
 } //--> meaning: if BOTH A is less than B AND A is less than C is true, then display true
 if ((A<B) && (C<A)){
    //console.log("True"); //output:no output--> because C<A is false
 } //--> meaning: since BOTH, A is less than B AND A is less than C are not true, interpreter will not display anything


 //OR operator
 if ((A<B) || (C<A)){
    //console.log("True"); //output:true--> because A<B is true, even though C<A is false
 } //--> meaning: if EITHER A is less than B OR C is less than A is true, then display true
 if ((C<B) || (C<A)){
    //console.log("True"); //output:no output--> because both C<B and C<A is false
 } //--> meaning: since NEITHER, C is less than B NOR C is less than A is true, interpreter will not display anything


 //NOT operator
    if (!(A<B)){
        //console.log("True"); //output:no output--> because A<B is true, but with NOT operator it will return false
    } //--> meaning: if A is NOT less than B is true, then display true
    if (!(C<A)){
        //console.log("True"); //output:true--> because C<A is false, so with NOT operator it will return true
    } //--> meaning: if C is NOT less than A is true, then display true
    