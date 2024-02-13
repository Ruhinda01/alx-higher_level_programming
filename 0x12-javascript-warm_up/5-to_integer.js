#!/usr/bin/node
const intValue = parseInt(process.argv[2]);
if (isNaN(intValue)) {
  console.log('Not a number');
} else {
  console.log('My number:', intValue);
}
