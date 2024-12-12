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


h1 = House('ЖК Богатырь', 10)
h2 = House('ЖК Династия', 7)
h1.go_to(5)
h2.go_to(8)