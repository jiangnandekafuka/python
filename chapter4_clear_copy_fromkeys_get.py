phonebook={
    'beth':'9102',
    'Alice':'2341',
    'Cecil':['3258','4567']
}
print "Cecil's phone number is %(Cecil)s." % phonebook

b=phonebook
print b['beth']
c=b.clear()
print c

people={
    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23'
    },
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
    },
    'Cecil':{
        'phone':'3158',
        'addr':'Baz avenue 90'
    }
}
d=people.copy()
print d
print d['Beth']['phone']
from copy import  deepcopy
c=deepcopy(people)
print c


print {}.fromkeys(['name','age'])
print dict.fromkeys(['name','age'],'unknown')

print people.get('Beth')
print {}.get('Beth','N/A')