# Наследование


# Родительский|Супер класс
class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} base action!"

kirito = Hero("Kirito", 100, 1000)

# Дочерний класс
class HeroMage(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp


    def action(self):
        return f"{self.name} new action mage hero"

    def cast_spell(self):
        return f"{self.name} cast spell!!"


gendalf = HeroMage("Gendalf", 100, 1000, 99)

# print(gendalf.name)
# print(gendalf.action())
# print(gendalf.action())
# print(kirito.action())
# print(type(gendalf))


class Animal:
    def action(self):
        return print('Animal action')

class Fly(Animal):
    def action(self):
        super().action()
        return print('Fly')

class Swim(Animal):
    def action(self):
        super().action()
        return print('Swim')

class Duck(Swim, Fly):
    ...

donald_duck = Duck()
donald_duck.action()
print(Duck.mro())
