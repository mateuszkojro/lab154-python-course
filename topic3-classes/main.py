class Person:
    def __init__(self, name):
        self.name = name

    def do_sth(self):
        print(self.name + " is doing something")
    
    def __repr__(self):
        return f"Person(name={self.name})"
    
class Student(Person):
    def __init__(self, name):
        super().__init__(name)

def main():
    p = Person("Mateusz")
    p.do_sth()
    print(p)

if __name__ == '__main__':
    main()