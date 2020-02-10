from letters import *

string = 'aye my name is tokyo'

for line in range(6):
    for letter in string:
        if letter == " ":
            print('    ', end='')
        else:
            print(globals()[letter][line], end='')
    print()
