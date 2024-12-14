class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        floor = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            while floor <= new_floor:
                print(floor)
                floor += 1


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
h1 = House('ЖК Богатырь', 10)
h2 = House('ЖК Династия', 7)

h1.go_to(5)
h2.go_to(8)

print('')
print(h1)
print(h2)
print(len(h1))
print(len(h2))