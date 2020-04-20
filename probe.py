# Полиморфизм является еще одним базовым аспектом объектно-ориентированного программирования и предполагает
# способность к изменению функционала, унаследованного от базового класса.

class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company

    # переопределение метода display_info
    def display_info(self):
        Person.display_info(self)
        print("Компания:", self.company)


class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)


people = [Person(name="Tom", age=34),
          Student(name="Bob", age=19, university="Harvard"),
          Employee(name="Sam", age=35, company="Google")]

for man in people:
    man.display_info()
    print()