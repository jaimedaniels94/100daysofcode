const input = require("readline-sync");

console.log("Hello and welcome to the band name generator!");
const city = input.question("What is the name of the city you grew up in?");
const pet = input.question("What is the name of your pet?");
console.log(`The name of your band could be ${city} ${pet}`);
