import winsound
from characters import *
import time

frequency = 750
string = 'abcdef'
convertedString = []
for i in string:
    if i.isdigit():
        convertedString.append(globals()['n' + i])

    elif i.isalpha():
        convertedString.append(globals()[i])

    elif i == ' ':
        convertedString.append(' ')

for a in convertedString:
    for b in a:
        if b == '.':
            winsound.Beep(frequency, 200)
            time.sleep(0.2)
        if b == '-':
            winsound.Beep(frequency, 600)
            time.sleep(0.2)
        if b == ' ':
            time.sleep(0.8)
    time.sleep(0.4)
