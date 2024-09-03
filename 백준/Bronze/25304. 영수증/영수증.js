const fs = require("fs");
const path = require("path");
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const X = parseInt(input[0]);
const N = parseInt(input[1]);
let sum = 0;

for(i = 2; i <= N + 1; i++) {
    const a = input[i].split(" ");
    sum += a[0]*a[1];
}

console.log(sum===X ? 'Yes' : 'No');