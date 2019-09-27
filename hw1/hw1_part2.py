
first_word = input('First => ')
first_word = first_word.lower()
print(first_word)

second_word = input('Second => ')
second_word = second_word.lower()
print(second_word)

combination = first_word + '_' +second_word

print('Example variable names')

print('Lower case: ' + combination.lower())
print('For constants: ' + combination.upper())
print('Camel case: ' + (combination.title()).replace('_', ''))
print('System variables: ' + '_' + combination.lower())

case1 = combination.replace('a','_')
case2 = case1.replace('e','_')
print('Silly variable: '+ case2)