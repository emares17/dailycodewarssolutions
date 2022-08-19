// Break camelCase

// Complete the solution so that the function will break up camel casing, using a space between words.

// Example
// "camelCasing"  =>  "camel Casing"
// "identifier"   =>  "identifier"
// ""             =>  ""

// ----------------Solution------------------

const solution = string => string.split('').map((element) => element.match(/[A-Z]/) ? ' ' + element : element).join('');