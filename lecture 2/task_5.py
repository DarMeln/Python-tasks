print('Username:')
name = input()
print('Password:')
password = input()

while password != 'kittens':
    print('Password for user: ' + name + ' is incorrect\nPlease try again...')
    password = input()
    
print('Password for user: ' + name + ' is correct')
