// There is a queue for the self-checkout tills at the supermarket. Your task is write a function to 
// calculate the total time required for all the customers to check out!

// input
// customers: an array of positive integers representing the queue. Each integer represents a customer, and its value 
// is the amount of time they require to check out.
// n: a positive integer, the number of checkout tills.
// output
// The function should return an integer, the total time required.

// Important
// Please look at the examples and clarifications below, to ensure you understand the task correctly :)

// -------------------------Solution---------------------------------
function queueTime(customers, n) {
    const arr = new Array(n).fill(0);
    
    for (let i = 0; i < customers.length; i++) {
      const idx = arr.indexOf(Math.min(...arr));
      arr[idx] += customers[i];
    }
    return Math.max(...arr);
  }

// -----------------------------------------------------------------------------------------------------------------------
// There is a bus moving in the city, and it takes and drop some people in each bus stop.

// You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get 
// into bus (The first item) and number of people get off the bus (The second item) in a bus stop.

// Your task is to return number of people who are still in the bus after the last bus station (after the last array). 
// Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping 
// there :D

// Take a look on the test cases.

// Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer 
// can't be negative.

// The second value in the first integer array is 0, since the bus is empty in the first bus stop.

// -----------------------------Solution----------------------------
const number = function(busStops) {
  let people = 0;
  busStops.forEach(a => people = people + a[0] - a[1]);
  return people;
}