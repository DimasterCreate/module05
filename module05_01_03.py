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

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"

    def __radd__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"

    def __sub__(self, value):
        if isinstance(value, int):
            return self.number_of_floors - value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"

    def __mul__(self, value):
        if isinstance(value, int):
            return self.number_of_floors * value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"

    def __floordiv__(self, value):
        if isinstance(value, int):
            return self.number_of_floors // value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"

    def __div__(self, value):
        if isinstance(value, int):
            return self.number_of_floors / value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"

    def __mod__(self, value):
        if isinstance(value, int):
            return self.number_of_floors % value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"

    def __pow__(self, value):
        if isinstance(value, int):
            return self.number_of_floors ** value
        elif not isinstance(value, int):
            return "Ошибка, введите целое число"



h1 = House('ЖК Богатырь', 10)
h2 = House('ЖК Династия', 7)

h1.go_to(5)
h2.go_to(8)

print('')
print(h1)
print(h2)
print(len(h1))
print(len(h2))

print('')
print(h1 == h2) #eq
h1 = h1 + 2 #add
print(h1)
print(h1 == h2)
h1 += 3 #iadd
print(h1)
h2 = 7 + h2 #radd
print(h2)
print(h1 > h2) #gt
print(h1 >= h2) #ge
print(h1 < h2) #lt
print(h1 <= h2) #le
print(h1 != h2) #ne

