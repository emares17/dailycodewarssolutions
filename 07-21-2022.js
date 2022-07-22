// Sum of two lowest positive integers

// Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
// No floats or non-positive integers will be passed.

// For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

// [10, 343445353, 3453445, 3453545353453] should return 3453455.

// -------------------------------Solution-------------------------------
function sumTwoSmallestNumbers(numbers) {  
    let sumArray = numbers.sort((a, b) => a - b);
    
    return sumArray[0] + sumArray[1];
  }

// -----------------------------------------------------------------------------------------------------------------

// Reverse List

// Write reverseList function that simply reverses lists.

function reverseList(arr) {
  return arr.reverse();
}

// ----------------------------------------------------------------------------------------------------------------

// Detect Pangram

// A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence 
// "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

// Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

// ---------------------------------------Solution---------------------------------------

function isPangram(string){
  let pangramArr = string.toLowerCase();
  let alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
  
 for (let i = 0; i < alphabet.length; i++) {
   if (pangramArr.indexOf(alphabet[i]) < 0) {
     return false;
   }
 }
  return true;
}

// -----------------------------------------------------------------------------------------------------------

// Jenny's secret message

// Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, 
// and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

// Can you help her?

// ------------------------------Solution-----------------------------

const greet = name => name === 'Johnny' ? "Hello, my love!" : "Hello, " + name + "!";

// Regex validate PIN code

// ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

// If the function is passed a valid PIN string, return true, else return false.

// Examples (Input --> Output)
// "1234"   -->  true
// "12345"  -->  false
// "a234"   -->  false

// ------------------------------------Solution-----------------------------------

const validatePIN = pin => /^(\d{4}|\d{6})$/.test(pin) ? true : false;