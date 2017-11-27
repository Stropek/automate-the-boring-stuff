# This program says hello and asks for my name.

print('Hello Wordl!')
print('What\'s your name?')

myName = input()

print(f'It\'s good to meet you, $myName')
print('The length of your name is: ')
print(len(myName))

print('What\'s your age?')

myAge = input()

print('You\'ll be ' + str(int(myAge) + 1) + ' in a year')
