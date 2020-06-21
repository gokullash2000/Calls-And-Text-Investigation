
#Read file into texts and calls

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)    #convert All lines into list of values

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)    #convert All lines into list of values



"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
#implementation

first_text = texts[0]   #This gives the first row in the csv file  as list
last_call = calls[-1]   #This gives the last row in the csv file as list

#Print Statements

print("First record of texts, {} texts {} at time {}".format(first_text[0], first_text[1], first_text[2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_call[0], last_call[1], last_call[2], last_call[3]))