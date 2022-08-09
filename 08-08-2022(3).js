// Valid Parentheses

// Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
// The function should return true if the string is valid, and false if it's invalid.

// Examples
// "()"              =>  true
// ")(()))"          =>  false
// "("               =>  false
// "(())((()())())"  =>  true

// -------------------------Solution--------------------------

function validParentheses(parens) {
    // Set a counter to keep track of open and closing parentheses
      let count = 0;
    // Begin a loop 
      for (let i = 0; i < parens.length; i++) {
    // Check for closing and opening parentheses
        if (parens.charAt(i) == '(') {
    //    If an opening parentheses if found, add +1 to the counter, else subtract 1
          count += 1;
        } else {
          count -= 1
        }
    // After the loop and counter is completed, if the count is less than 0, we know to return false
        if (count < 0) {
          return false
        }
      }
    // Outside the for loop, we will check the counter again, if the counter is equal to 0, we know we have a valid parentheses set.
    // Therefore, we would return true, else we would not have valid parentheses, and return false.
      if (count === 0) {
          return true
        } else {
          return false;
        }
}