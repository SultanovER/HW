class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def moneyX(self):
        vvod = int(input('Добавить на счёт: '))
        self.balance += vvod
        print(f'Баланс:{self.balance}')
    def kill(self):
        self.balance = 0
        print(f'Обнуление счёта!:{self.balance}')
    def _jackpot(self):
        self.balance *= 10
        print(f'Джекпот!{self.balance}')
    def _soviet_union(self, other_object):
        other_object.balance = other_object.balance
        self.balance += other_object.balance
        other_object.balance = 0
        print(f'Новый баланс:{self.balance}')

klient1 = Bank('klient1', 100)
klient2 = Bank('klient2', 200)
klient1.moneyX()
klient1._jackpot()
klient1._soviet_union(klient2)
klient1.kill()


