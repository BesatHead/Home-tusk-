class House:
    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self): # Специальные методы классов

        return self.number_of_floors

    def __str__(self): # Специальные методы классов

        return f'Дом {self.name} имеет {self.number_of_floors} этажей'

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 10) # Специальные методы классов
h4 = House('ЖК Акация', 20) # Специальные методы классов

h1.go_to(5)
h2.go_to(10)

print ('____________________________________________') # Специальные методы классов

print(h3)
print(h4)

print(len(h3))
print(len(h4))