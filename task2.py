#Read file into texts and calls

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)    #convert All lines into list of values

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)    #convert All lines into list of values

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#Implementation

telephone_numbers = dict()
most_spent_duration = 0
most_spent_number = None
for call in calls:
    telephone_numbers[call[0]] = telephone_numbers.get(call[0], 0) + int(call[-1])
    telephone_numbers[call[1]] = telephone_numbers.get(call[1], 0) + int(call[-1])
    if telephone_numbers[call[0]] > most_spent_duration:
        most_spent_number = call[0]
        most_spent_duration = telephone_numbers[call[0]]
    if telephone_numbers[call[1]] > most_spent_duration:
        most_spent_number = call[1]
        most_spent_duration = telephone_numbers[call[1]]

#Print Number

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(most_spent_number, most_spent_duration))