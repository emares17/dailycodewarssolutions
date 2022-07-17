// Find the position!

// When provided with a letter, return its position in the alphabet.

// Input :: "a"

// Ouput :: "Position of alphabet: 1"

// ---------------------Solution-----------------------
function position(letter){
    let alphabet = "abcdefghijklmnopqrstuvwxyz".split('');
    
    let position = letter => letter.split('').map(x => alphabet.indexOf(x) + 1);
    
    return `Position of alphabet: ${position(letter)}`
  }

// ---------------------------------------------------------------------------

// Transportation on vacation

// After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for 
// you and your girlfriend and try to leave all the mess behind you.

// You will need a rental car in order for you to get around in your vacation. The manager of the car rental 
// makes you some good offers.

// Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. 
// Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

// Write a code that gives out the total amount for different days(d).

// -----------------------Solution------------------------

function rentalCarCost(d) {
    if (d >= 7) {
      return (d * 40) - 50;
    } else if (d >= 3) {
      return (d * 40) - 20;
    } else {
      return d * 40;
    }
  }

// ---------------------------------------------------------------------------

// Race Ceremony

// The national go-kart racing competition is taking place in your local town and you've been called for building the winners podium with the available wooden blocks. Thankfully you are in a wood-rich area, number of blocks are always at least 6.

// Remember a classic racing podium have three platforms for first, second and third places. First place is the highest and 
// second place is higher than third. Also notice that platforms are arranged as 2nd - 1st - 3rd.

// The organizers want a podium that satisfies:

// The first place platform has the minimum height posible
// The second place platform has the closest height to first place
// All platforms have heights greater than zero.
// Task
// Given the numbers of blocks available, return an array / tuple or another data structure depending on the language 
// (refer sample tests) with the heights of 2nd, 1st, 3rd places platforms.

// Examples (input -> output)
// 11 ->   [4, 5, 2]
// 6  ->   [2, 3, 1]
// 10 ->   [4, 5, 1]

// --------------------------Solution----------------------------

function racePodium(blocks) {
    let position2 = blocks / 3 + 2/3 | 0;
    let position1 = position2 + 1;
    let position3 = blocks - position1 - position2;
    
    if (blocks === 7) {
      return [2, 4, 1];
    } else {
      return [position2, position1, position3];
    }
  }

// -----------------------------------------------------------------

// Beginner Series #1 School Paperwork

// Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork 
// has 'm' pages.

// Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

// Example:
// n= 5, m=5: 25
// n=-5, m=5:  0

// --------------------------Solution----------------------------

const paperwork = (n, m) => n < 0 || m < 0 ? 0 : n * m;

// --------------------------------------------------------------------------------

// Driving School Series #2

// Fast & Furious Driving School's (F&F) charges for lessons are as below:

// Time	Cost
// Up to 1st hour	$30
// Every subsequent half hour**	$10
// ** Subsequent charges are calculated by rounding up to nearest half hour.
// For example, if student X has a lesson for 1hr 20 minutes, he will be charged $40 (30+10) for 1 hr 30 mins and if 
// he has a lesson for 5 minutes, he will be charged $30 for the full hour.

// Out of the kindness of its heart, F&F also provides a 5 minutes grace period. So, if student X were to have a lesson 
// for 65 minutes or 1 hr 35 mins, he will only have to pay for an hour or 1hr 30 minutes respectively.

// For a given lesson time in minutes (min) , write a function cost to calculate how much the lesson costs. Input is always > 0.

// ---------------------------Solution-------------------------------

const cost = mins => 30 + (mins > 65 ? Math.ceil((mins - 65) / 30) : 0) * 10;

// --------------------------------------------------------------------------------

// Is he gonna survive?

// A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a 
// couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.
//  Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, 
//  will he survive?

// Return True if yes, False otherwise :)

// ----------------------------------Solution----------------------------------

const hero = (bullets, dragons) => bullets / 2 >= dragons ? true : false;

// -------------------------------------------------------------------------------