# Cat years, Dog years

# Kata Task
# I have a cat and a dog.

# I got them at the same time as kitten/puppy. That was humanYears years ago.

# Return their respective ages now as [humanYears,catYears,dogYears]

# NOTES:

# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

# --------------------------------------Solution---------------------------------------

def human_years_cat_years_dog_years(human_years):
    return [human_years, 16 + 4 * human_years, 14 + 5 * human_years] if human_years > 1 else [1,15,15]