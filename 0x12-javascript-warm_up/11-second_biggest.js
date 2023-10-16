#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg));
const largest = Math.max(...args);
const filteredArgs = args.filter(num => num !== largest);
let secondLargest = Math.max(...filteredArgs);
if (args.length <= 1 || isNaN(secondLargest)) {
  secondLargest = 0;
}
console.log(secondLargest);
