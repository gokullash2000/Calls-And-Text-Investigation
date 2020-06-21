
#Read file into texts and calls.

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)    #convert All lines into list of values

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)    #convert All lines into list of values

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#Implementation

unique_tel_numbers = []     #Empty List

for text in texts:
    if text[0] not in unique_tel_numbers:
        unique_tel_numbers.append(text[0])  #Append the number that not in that list
    if text[1] not in unique_tel_numbers:
        unique_tel_numbers.append(text[1])

for call in calls:
    if call[0] not in unique_tel_numbers:
        unique_tel_numbers.append(call[0])  #Append the number that not in that list
    if call[1] not in unique_tel_numbers:
        unique_tel_numbers.append(call[1])

#Print Statement


print("There are {} different telephone numbers in the records.".format(len(unique_tel_numbers)))