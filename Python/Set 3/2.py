import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = input('Enter email address: ')
if (re.search(regex, email)):
    print('Valid')

else:
    print('invalid')