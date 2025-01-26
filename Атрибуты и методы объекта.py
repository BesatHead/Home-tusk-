class House:
    def __init__ (self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):

        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print ("Такого этажа не существует")

    def __len__ (self): # Специальные методы классов
        return self.number_of_floors

    def __str__ (self): # Специальные методы классов
        return f'Дом {self.name} имеет {self.number_of_floors} этажей'

    def __eq__ (self, other): # Перегрузка методов
        return self.number_of_floors == other.number_of_floors

    def __add__ (self, other): # Перегрузка методов
        return House(self.name, self.number_of_floors + other)

    def __iadd__ (self, other): # Перегрузка методов
        self.number_of_floors += other
        return self

    def __radd__ (self, other): # Перегрузка методов
        return House(self.name, self.number_of_floors + other)

    def __gt__ (self, other): # Перегрузка методов
        return self.number_of_floors > other.number_of_floors

    def __ge__ (self, other): # Перегрузка методов
        return self.number_of_floors >= other.number_of_floors

    def __ne__ (self, other): # Перегрузка методов
        return self.number_of_floors != other.number_of_floors

    def __lt__ (self, other): # Перегрузка методов
        return self.number_of_floors < other.number_of_floors

    def __le__ (self, other): # Перегрузка методов
        return self.number_of_floors <= other.number_of_floors

print ('___________Атрибуты и методы объекта_________________')  # Атрибуты и методы объекта

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 10) # Специальные методы классов
h4 = House('ЖК Акация', 20) # Специальные методы классов

h1.go_to(5)
h2.go_to(10)

print ('___________Специальные методы классов_________________') # Специальные методы классов

print(h3)
print(h4)

print(len(h3))
print(len(h4))

print ('________________Перегрузка методов__________________') # Перегрузка методов

print(h3)

print(h4)

print(h3 == h4) # __eq__

h3 = h3 + 10 # __add__

print(h3)

print(h3 == h4)

h3 += 10 # __iadd__

print(h3)

h4 = 10 + h4 # __radd__

print(h4)

print(h3 > h4) # __gt__

print (h3 >= h4) # __ge__

print(h3 < h4) # __lt__

print(h3 <= h4) # __le__

print(h3 != h4) # __ne__