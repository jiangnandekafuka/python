def story(**kwds):
    return  'Once upon a time, there was a '\
            '%(job)s called %(name)s.' % kwds
def power(x,y, *others):
    if others:
        print 'Received redundant parameters:', others
    else:
        return  pow(x,y)
def interval(start , stop=None, step=1):
      'Imitates range() for step > 0'
      if stop is None:
          start , stop = 0,start
      result=[]
      i = start
      while i < stop:
          result.append(i)
          i+=step
      return  result
print story(job='king',name='Gumby')
print story(name='Sir Robin',job='brave knight')
params={'name':'Python','job':'language'}
print story(**params)
del params['job']
print story(job='Stroke of genius',**params)
print power(2,3,1)
print power(3,2,0)
print power(y=3,x=2)
