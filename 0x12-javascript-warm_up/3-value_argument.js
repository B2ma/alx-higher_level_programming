#!/usr/bin/node
let index = 2;
let argCount = 0;
while (process.argv[index] !== undefined) {
  argCount++;
  console.log(process.argv[index]);
  index++;
}
if (argCount === 0) {
  console.log('No argument');
}
