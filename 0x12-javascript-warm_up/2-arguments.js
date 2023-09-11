#!/usr/bin/node

// import { argv } from 'node:process';

const args = process.argv;
const argLen = args.length;

if (argLen <= 2) {
  console.log('No argument');
} else if (argLen === 3) {
  console.log('Argument found');
} else if (argLen >= 4) {
  console.log('Arguments found');
}
