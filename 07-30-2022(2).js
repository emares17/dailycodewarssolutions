// Square Every Digit

// Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

// For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

// Note: The function accepts an integer and returns an integer

// ---------------------------Solution----------------------------

function squareDigits(num){
    //   First the num was turned into a string to be able to split 
    //   and turn into an array, it was then mapped over, squared and turned
    //   back into a Number.
      let numArray = num.toString().split('').map(str => {
        return Math.pow(Number(str), 2)
      })
    //   Lastly it was joined back together, and used Number to turn the string back into a Number.
      return Number(numArray.join(''))
    }
