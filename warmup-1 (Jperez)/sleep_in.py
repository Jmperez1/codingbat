def sleep_in(weekday, vacation):
    """The parameter weekday is True if it is a weekday, and the parameter vacation is True
    if we are on vacation. We sleep in if it is not a weekday or we're on vacation.
    Return True if we sleep in."""

    return not weekday or vacation

print(sleep_in(False, False)) #It is not a weekday(false) and we are not on vacation, so we sleep in--> True
print(sleep_in(True, False))  #It is a weekday and we are not on vacation, so we do not sleep in --> False
print(sleep_in(False, True))  #It is not a weekday and we are on vacation, so we sleep in --> True
print(sleep_in(True, True)) #It is a weekday and we are on vacation, so we sleep in --> True

def taco_tuesday(Tuesday, HispanicHoliday):
    """The parameter Tuedsay is True if it is Tuesday, and the parameter hispanic holiday is True if it is a Hispanic Holiday. 
    We eat tacos if it is Tuesday or if it is a hispanic holiday"""

    return Tuesday or HispanicHoliday

print(taco_tuesday(False, False)) #It is not Tuesday or a HispanicHoliday so I will not eat tacos. --> False)
print(taco_tuesday(True, False))  #It is a Tuesday, but not a Hispanic Holiday so I will eat tacos. --> True) 
print(taco_tuesday(False, True))  #It is not Tuesday but it is a Hispanic Holidya so I will eat tacos. --> True)
