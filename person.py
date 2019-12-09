
class Person():
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def last_name(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return f'Person: {self.name}, {self.pay}'

class Manager(Person):
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus = 10):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __str__(self):
        return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)





"""
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay = 10000)
    print(sue)
    print(bob)
    print(bob.last_name(), sue.last_name())
    sue.giveRaise(.1)
    print(sue)
    tom = Manager('Tom Jones', 5000)
    tom.giveRaise(.10)
    print(tom.last_name())
    print(tom)
"""



