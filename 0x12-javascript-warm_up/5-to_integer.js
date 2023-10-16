#!/usr/bin/node
const firstArg = process.argv[2];
const convertedArg = parseInt(firstArg);
if (!isNaN(convertedArg)) {
  console.log(`My number: ${convertedArg}`);
} else {
  console.log('Not a number');
}
