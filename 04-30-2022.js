// Write a function that checks if a given string (case insensitive) is a palindrome.
// ---------------Solution-----------------

function isPalindrome(x) {
    return x.split('').reverse().join('').toLowerCase() === x.toLowerCase();
  }
//  In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

//   Example
//   filter_list([1,2,'a','b']) == [1,2]
//   filter_list([1,'a','b',0,15]) == [1,0,15]
//   filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
// -------------Solution-------------------
function filter_list(l) {
    const onlyNums = l.filter(nums => typeof nums === 'number')
    return onlyNums;
  }

// JavaScript Arrays support a filter function (starting in JavaScript 1.6). Use the filter functionality to complete the function given.

// The solution would work like the following:
  
// getEvenNumbers([2,4,5,6]) // should == [2,4,6]
// ----------------Solution-----------------
function getEvenNumbers(numbersArray){
    return numbersArray.filter(evens => evens % 2 === 0)
  }

// In this kata your task is to remove all the duplicates from the array using a standart build-in method - Array.prototype.filter(); return the array containing unique values only.

// Tip: use the index of value(s) to solve this kata

// If you are not familiar with filter() - info is here:

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

// For example:

// var arr = [4];

// unique(arr); // should return [4]

// var arr = [1,1,1,2,2,3];

// unique(arr); // should return [1,2,3]
// ------------------------Solution-----------------------
function unique(arr) {
    return arr.filter((c, index) => arr.indexOf(c) === index)
  }
// ----Or----------------
const unique =  arr => arr.filter((c, index) => arr.indexOf(c) === index)
