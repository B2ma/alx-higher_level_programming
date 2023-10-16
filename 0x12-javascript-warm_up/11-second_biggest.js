#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg));
const largest = Math.max(...args);
args.splice(args.indexOf(largest), 1);
let secondLargest = Math.max(...args);
if (args.length <= 1 || isNaN(secondLargest)) {
  secondLargest = 0;
}
console.log(secondLargest);
