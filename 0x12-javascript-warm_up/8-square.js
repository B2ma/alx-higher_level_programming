#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < size) {
    let j = 0;
    let sqLine = '';
    while (j < size) {
      sqLine += 'X';
      j++;
    }
    console.log(sqLine);
    i++;
  }
}
