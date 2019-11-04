name= raw_input('What is your name?')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print 'Hello,%s' % name
    elif name.startswith('Mrs'):
        print 'hello,%s' % name
    else:
        print 'Hello,Gumby'
else:
    print 'Hello,stranger'


age=-1
assert  0<age<100, 'The age must be realistic'