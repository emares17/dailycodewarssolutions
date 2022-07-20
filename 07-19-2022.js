// Anagram Detection

// An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

// Note: anagrams are case insensitive

// Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

// Examples
// "foefet" is an anagram of "toffee"

// "Buckethead" is an anagram of "DeathCubeK"

// ------------------------------Solution-------------------------------

var isAnagram = function(test, original) {
    let testAnagram = test.toLowerCase().split('').sort().join('');
    let originalAnagram = original.toLowerCase().split('').sort().join('');
    
    if (test.length !== original.length) {
      return false;
    }
    
    if (testAnagram === originalAnagram) {
      return true;
    } else {
      return false;
    }
  };
  