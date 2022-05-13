// Given an array of integers, return a new array with each value doubled.

// For example:

// [1, 2, 3] --> [2, 4, 6]
// ---------------------Solution------------------------
function maps(x){
    return x.map(multiply => multiply * 2)
  }
// Or---------------------------------------------------
const maps = x => x.map(multiply => multiply * 2);