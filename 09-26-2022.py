# Name That Number!

# In this kata, you'll be given an integer of range 0 <= x <= 99 and have to return that number spelt out in English. A few examples:

# name_that_number(4)   # returns "four"
# name_that_number(19)  # returns "nineteen"
# name_that_number(99)  # returns "ninety nine"
# Words should be separated by only spaces and not hyphens. No need to validate parameters, they will always be 
# in the range [0, 99]. Make sure that the returned String has no leading of trailing spaces. Good luck!

# ----------------------------Solution--------------------------------

def name_that_number(x):
    numbers = "zero one two three four five six seven eight nine".split()
    numbers.extend("ten eleven twelve thirteen fourteen fifteen sixteen".split())
    numbers.extend("seventeen eighteen nineteen".split())
    numbers.extend(tens if ones == "zero" else (tens + ' ' + ones) 
        for tens in "twenty thirty forty fifty sixty seventy eighty ninety".split()
        for ones in numbers[0:10])

    return numbers[x]    