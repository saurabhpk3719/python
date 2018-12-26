class parent :
    'what its do'
    ''
    age =10    #class variable

    def __init__(self,name):
        self.name=name
        print('object created')

    def hello(self):
        print (f'parent name is {self.name} and age is {self.age} ')

o=parent ('cosmic')
o.hello()

class child (parent):
    def __init__(self,age):
        self.age=age
        print ('child obj created')

    def name(self):
        
