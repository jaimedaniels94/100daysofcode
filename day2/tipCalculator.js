const input = require("readline-sync");

console.log("Hello and welcome to the handy tip calculator");
const bill = parseInt(input.question("How much is the bill? $"));
const tip = parseInt(
  input.question("What percentage would you like to tip? 15, 20, or 25?")
);
const split = parseInt(input.question("How many people are splitting?"));

const billWithTip = (tip / 100) * bill + bill;
let billPerPerson = billWithTip / split;

billPerPerson = billPerPerson.toFixed(2);

console.log(billPerPerson);
