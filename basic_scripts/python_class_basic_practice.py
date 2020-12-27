''' If this example makes any sense! '''

class Monkey:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_age(self):
        return self.age

    @staticmethod
    def print_welcome():
        return 'welcome'

    def king_kong(self):
        # Abstract Class Method
        raise NotImplementedError

class KingKong(Monkey):
    hair = 1

    def __init__(self, weight):
        # Guide for inheriting constructor:
        # -> call the constructor of the base class
        super().__init__(name='KingKong', age=40)
        self.weight = weight

    def king_kong(self):
        print(self.name)
        print(self.weight)
        print(self.age)
        print('I am king kong.')

if __name__ == '__main__':
    mn = Monkey('Chimp', 80)
    print(mn.get_age)
    print(mn.print_welcome())

    kk = KingKong(500)
    kk.king_kong()
