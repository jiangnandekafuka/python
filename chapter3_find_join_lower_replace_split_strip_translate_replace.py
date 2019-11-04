title='Monty  python is flying  circus'
print title.find('python')

seq=['1','2','3','4','5']
sep='+'
print sep.join(seq)


name='GUMby'
print name.lower()

print title.replace('Monty','haha')

b=sep.join(seq)
print b
print b.split('+')

c='*****aduhfuishdfhuisdhfsuhieushi!!!!******'
print c.strip('*!')

from string import  maketrans
table=maketrans('cs','kz')
len(table)
table[97:123]
maketrans('','')[97:123]
print 'this is an incredible test'.translate(table)