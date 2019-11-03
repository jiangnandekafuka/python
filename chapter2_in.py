database=[
    ['albert','1234'],
    ['dilbert','4242'],
    ['smith','7524'],
    ['jones','9843']
]
usrname=input('User name:')
pin=input('PIN code:')

if [usrname,pin] in database: print('Access granted')
else :print('Wrong access')