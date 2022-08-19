num1 = 45 # variable num1 holding an integer value of 45
num2 = 12.0 #variable num2 holding a floating value of 12.0
name = 'simeon'# variable of name holding a string value of simeon
X = True # variable  X holding a boolean value True
print(num2)

word = 'we\'re brothers from the other side of the town' # backward slash (\) denotes escape chrarcter
print(word)

word2 = "we're brothers from the other side of the town"
print(word2)

word3 = 'Python is fun,\npython is easy,\npython is an highlevel languae' # backward slash + n (\n) denotes new line
print(word3)
print('\n')
word4 = '''Python is fun
python is easy
python is an highlevel languae
'''  # this is a multiline string
print(word4)

# STRING CONCATENATION
print('hello' + ' '+'world')# joining of string and string
print('hello ' + 'world')

print('Welcome to python class ' + name)# joining of string and variable also holding a string value

surname = 'Kanjuni'
print(surname, name) # joining of variable and variable holding string values

# STRING FORMATTING
price1 = 45000
price2 = 15000
price3 = 85000
report = 'I sold 3 pairs of shirt for {}, 2 pairs of shoe for {} and a suit for {}'
print(report.format(price1,price2,price3))

print(f'I sold 3 pairs of shirt for {price1}, 2 pairs of shoe for {price2} and a suit for {price3}')















