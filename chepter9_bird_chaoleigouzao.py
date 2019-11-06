__metaclass__=type
class Bird:
    def __init__(self):
        self.hugry=True
    def eat(self):
        if self.hugry:
            print 'Aaaah...'
            self.hugry=False
        else:
            print 'No,thanks!'


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound='Squawk!'
    def sing(self):
        print self.sound

b=Bird()
b.eat()
b.eat()
sb=SongBird()
sb.sing()
sb.eat()
sb.eat()