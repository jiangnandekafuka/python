x=1
while x<=12:
    print x
    x+=1

words=['this','is','an','ex','parrot']
for word in words:
    print word


print range(0,10)
print xrange(10)

for number in range(1,11):
    print number


names=['anne','beth','george','damon']
ages=[12,45,32,102]
for i in range(len(names)):
    print names[i],'is',ages[i],'years old'

print zip(names,ages)
for name,age  in zip(names,ages):
    print name, 'is', age, 'years old'


from math import  sqrt
for n in range(99,0,-1):
    root=sqrt(n)
    if root==int(root):
        print n
        break
word='dummy'
while word:
    word=raw_input('Please enter a word:')
    print 'The word was ' + word
    break
while True:
    word=raw_input('Please enter a word:')
    if not word: break
    print 'The word was ' + word


from math import sqrt
b=raw_input('imput a number between 1 to 100:')
for n in range(99,81,-1):
    root=sqrt(n)
    if root==int(n):
        print n
        break
    else:
        print 'Did not find it!'


result=[]
for x in range(3):
    for y in range(3):
     print result.append((x,y))