// Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

// [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

// ---------Solution----------------
const grow = x => x.reduce((acc, c) => acc * c, 1) 