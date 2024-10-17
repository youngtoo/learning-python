alphabet = 'abcdefghijklmnopqrstuvwxyz'
position = alphabet.find('z')

for a in alphabet:
    print(a, end=', ')

print('\n', position)

def say_hello():
    print("Hello there!")

say_hello()

for letter in range(0,len(alphabet), 5):
    print(alphabet[letter])
