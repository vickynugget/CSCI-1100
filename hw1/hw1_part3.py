word = input('Word => ')
print(word)

c = input('#columns => ')
print(c)

r = input('#rows => ')
print(r)

r = int(r)
c = int(c)
print('Your word is:', word)

print('\n(a)')
print((('*** ' * c).rstrip(' ') + '\n')*r)

print('(b)')
print(((('*** ' * c).rstrip(' ') + '\n')*(r//2)).rstrip('\n'))
print(('*** ' * (c//2)) + 'CS1' + (' ***' * (c//2)))
print((('*** ' * c).rstrip(' ') + '\n')*(r//2))

print('(c)')
print(('*** ' * (c//2)) + ' | ' + (' ***' * (c//2)))
print(((('*** ' * c).rstrip(' ') + '\n')*(r//2-1)),end='')
print(' |  ' + '*** ' * ((c-3)//2) + 'CS1 ' + '*** ' * ((c-3)//2) + ' | ')
print(((('*** ' * c).rstrip(' ') + '\n')*(r//2-1)),end='')
print(('*** ' * (c//2)) + ' | ' + (' ***' * (c//2)))      