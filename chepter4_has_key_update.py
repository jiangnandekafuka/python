d={}
print d.has_key('name')
d['name']='Eric'
print d.has_key('name')

e={
    'title':'python web site',
    'url':'http://www.python.org',
    'changed':'Mar 14 22:09:15 MET 2008'
}
x={'title':'python laguage website'}
e.update(x)
print e