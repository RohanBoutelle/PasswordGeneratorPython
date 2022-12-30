import string
from secrets import choice

length = int(input('How long would you like your passcode to be? '))

chars = list(string.printable)
del chars[-6:]

passcode = []

while len(passcode) < length:
    passcode.append(choice(chars))
    
finalPasscode = ''.join([str(item) for item in passcode])
    
print(finalPasscode)
