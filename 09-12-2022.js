// Count the days!

// Little Annie is very excited for upcoming events. She wants to know how many days she has 
// to wait for a specific event.

// Your job is to help her out.

// Task: Write a function which returns the number of days from today till the given date. 
// The function will take a Date object as parameter. You have to round the amount of days.

// If the event is in the past, return "The day is in the past!"
// If the event is today, return "Today is the day!"
// Else, return "x days"

// PS: This is my first kata. I hope you have fun^^

// --------------------------Solution----------------------------

function countDays(d){
    let date = d
    let today = new Date()
    let dateCheck = date.getFullYear() === today.getFullYear() && date.getMonth() === today.getMonth() && date.getDay() === today.getDay()
    
    if (dateCheck) return "Today is the day!"
    if (today.getTime() > date.getTime()) return "The day is in the past!";
    return `${Math.round((date.getTime() - today.getTime()) / 1000 / 60 / 60 / 24)} days`
}
  