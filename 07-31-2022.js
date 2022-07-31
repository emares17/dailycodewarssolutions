// Simple Pig Latin

// Move the first letter of each word to the end of it, then add "ay" 
// to the end of the word. Leave punctuation marks untouched.

// Examples
// pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
// pigIt('Hello world !');     // elloHay orldway !

// ------------------------Solution-------------------------
function pigIt(str){
    // First the string will be turned into an array.  
      
      let strArr = str.split(' ');
    // Then the array will be mapped through.  
       
        return strArr.map((element) => {
    // While mapping we will check for a word match to not contain punctuation characters using a ternary operator.
         
          return element.match(/[A-z]/i) ?
    // if the word does not contain punctuation characters, inside of template literals the first letter from every word will be removed, 
    // added to the end, and 'ay' will be added on. IF the string is a punctuation characted, it will be returned as is.
         
          `${element.substr(1)}${element.substr(0, 1)}ay` : element   
      })
    // Lastly, it will be joined together and returned.
      
        .join(' ')
};

// Or-------------------------------------------------------

const pigIt = str => str.split(' ').map((element) => element.match(/[A-z]/i) ? `${element.substr(1)}${element.substr(0, 1)}ay` : element).join(' ');

