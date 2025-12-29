# class HeroMage
# hero_mage
# lesson 1.py
# урок1.py

my_int = 123
class Hero:
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} base action!!"


# Объект/Экзеспляр класса
kirito = Hero("Ardager", 100, 1000)
asuna = Hero("Asuna", 99, 999)
my_str = "text"
my_flout = 1.12
my_list = [1,2,"123"]