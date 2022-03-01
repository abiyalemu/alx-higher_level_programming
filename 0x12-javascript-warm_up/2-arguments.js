#!/usr/bin/node
// this script prints a massage depending of the number of arguments passed
const myVar = process.argv.length;
if (myVar === 2) {
    console.log('No argument');
} else if (myVar === 3) {
    console.log('Argument found')
} else {
    console.log('Arguments found')
}
