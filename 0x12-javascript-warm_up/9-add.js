#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const integerOne = parseInt(process.argv[2]);
const integerTwo = parseInt(process.argv[3]);
if (isNaN(integerOne) || isNaN(integerTwo)) {
  console.log('NaN');
} else {
  const result = add(integerOne, integerTwo);
  console.log(result);
}
