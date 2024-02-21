class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def hp(self):
        self.health_points * 2

    def __str__(self):
        return f'Имя: {self.name}\nПрозвище: {self.nickname}\nСпособность: {self.superpower}\nЗдоровье: ' \
               f'{self.health_points}\nБоевой клич: {self.catchphrase}'

class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False
    def two_hp(self):
        self.health_points **= 2
        self.fly = True
    def true_phrase(self):
        return True in self.catchphrase

class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.damage = damage
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = False
    def two_hp(self):
        self.health_points **= 2
        self.fly = True
    def true_phrase(self):
        return True in self.catchphrase

class Villain(SpaceHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.people = 'monster'
    def gen_x(self):...
    def crit(self):
        return self.damage ** 2

earth_man = EarthHero('Корней Михалыч', 'ЗемлеКоп', 'Бесперебойно копать землю. А ещё он полицейский(коп)',
                      100, 'Докопался я!', 20)
cosmo_man = SpaceHero('Гагар Юрьин', 'Восток 1', 'Лететь как ракета и дышать в ваккуме',
                      100, 'Ты Венера, Я Юпитер!', 50)
enemy = Villain('Элвуд Сильверсайд', 'Silver Side', 'Левитация, телекинез, телепатия', 200, 'Люк, я твой отец',
                80)
print(earth_man.people, cosmo_man.people, enemy.people)
print(earth_man)
print(cosmo_man)
print(enemy)

print(f'Летает? {earth_man.two_hp()}')
print(f'Летает? {cosmo_man.two_hp()}')
print(enemy.crit())




