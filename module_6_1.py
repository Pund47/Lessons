class animal:
    alive = True
    fed = False
    def __init__(self,name):
        self.name = name
    def eat(self, food):
        if food.edible == True:
            print (f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}  и сдох')
            self.alive = False
class plant:
    edible = False
    def __init__(self,name):
        self.name = name

class Mammal(animal):
    pass
class Predator(animal):
    pass
class Flower(plant):
    pass
class Fruit(plant):
    def __init__(self, name):
        self.edible = True
        self.name = name






a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)