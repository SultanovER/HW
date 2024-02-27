
class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.money = money
        self.__key = key

class NewClass(Bank):
    def set_additional_property(self, value):
        pass
    def get_additional_property(self):
        pass

    additional_property = property(get_additional_property, set_additional_property)

class NewNewClass(NewClass):
    def __init__(self, name, age, money, key, additional_property):
        super().__init__(name, age, money, key)
        self._additional_property = additional_property
    def get_additional_property(self):
        return self._additional_property

    def set_additional_property(self, value):
        self._additional_property = value

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, Money: {self.money}, Additional Property: {self._additional_property}"

    additional_property = property(get_additional_property, set_additional_property)
