#!/usr/bin/node
const size = math.floor(number(process.argv[2]));
if (isNaN(size)) {
	console.log('Missing size');
} else {
  for (j = 0; j < size; j++) {
	  let row = '';
	  for (let c = 0; c < size; c++) row += 'X';
	  console.log(row);
  }
}
