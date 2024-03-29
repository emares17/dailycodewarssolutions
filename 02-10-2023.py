# Roman Numerals Decoder

# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
# You don't need to validate the form of the Roman numeral.

# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, 
# starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) 
# and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

# Example:

# solution('XXI') # should return 21
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

# -----------------------------Solution--------------------------------

def solution(roman):
        dicti = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        count = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i] == 'I' and (roman[i+1] == 'V' or roman[i+1] == 'X'):
                count += dicti[roman[i+1]] - dicti[roman[i]]
                i += 2
            elif i + 1 < len(roman) and roman[i] == 'X' and (roman[i+1] == 'L' or roman[i+1] == 'C'):
                count += dicti[roman[i+1]] - dicti[roman[i]]
                i += 2
            elif i + 1 < len(roman) and roman[i] == 'C' and (roman[i+1] == 'D' or roman[i+1] == 'M'):
                count += dicti[roman[i+1]] - dicti[roman[i]]
                i += 2
            else:
                count += dicti[roman[i]]
                i += 1
        return count