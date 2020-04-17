class Person:
    def __init__(self, name):
        self._name = name   # name is property object by default it invokes getter
        # actual variable where name is stored is _name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

p = Person('Adam')
print('The name is:', p.name) #getter
p.name = 'John' #setter
del p.name #deleter

# O/P
# Getting name
# The name is: Adam
# Setting name to John
# Deleting name