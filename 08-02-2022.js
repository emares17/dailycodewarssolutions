// Love vs friendship

// If a = 1, b = 2, c = 3 ... z = 26

// Then l + o + v + e = 54

// and f + r + i + e + n + d + s + h + i + p = 108

// So friendship is twice stronger than love :-)

// The input will always be in lowercase and never be empty.

// -------------------------Solution-------------------------

function wordsToMarks(string){
    let sum = 0;
    
    for (let i = 0; i < string.length; i++) {
      let idx = string.toUpperCase().charCodeAt(i);
      if (idx > 64 && idx < 91) {
        sum += (idx - 64) 
      } 
    }
    return sum;
}