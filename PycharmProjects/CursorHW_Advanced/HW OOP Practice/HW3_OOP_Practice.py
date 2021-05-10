from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, house):
        raise NotImplementedError

    @abstractmethod
    def income(self, freelancer, service_cost):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, own_money, salary,  new_house=None):
        if new_house is None:
            new_house = []
        self.name = name
        self.age = age
        self.own_money = own_money
        self.salary = salary
        self.new_house = new_house

    def info(self):
        print(f'{self.age} years old man named {self.name} got his sevings: {self.own_money} dollars'
              f' - for buying a new house')

    def make_money(self):
        print(f"\t{self.own_money} dollars")
        self.own_money = self.own_money + self.salary
        print(f'\tToday I have got my salary - {self.salary} dollars, so for now - {self.own_money} dollars')

    def buy_house(self, house):
        if self.own_money < house.cost:
            print("Not enough money to buy this house. It's time to earn some extra money.")
        else:
            self.own_money = self.own_money - house.cost
            print(f"Nice. I bought a new house. It's cost - {house.cost}. i think it's time to move to a new home")

    def income(self, freelancer, service_cost=50):
        if freelancer > 15:
            self.own_money = self.own_money + (service_cost * freelancer)
            print(f'{self.name} work hard and get - {self.own_money} dollars!')


class House(ABC):
    def __init__(self, cost: (float, int), area: (float, int)):
        self.cost = cost
        self.area = area


class NewHouse(House):
    def __init__(self, cost, area):
        super().__init__(cost, area)

    def discount(self, disc):
        self.cost -= self.cost*disc
        return self.cost


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name: str, discount: (float, int), houses=None):
        if houses is None:
            houses = []
        self.name = name
        self.discount = discount
        self.av_houses = houses

    def info(self):
        if self.av_houses is not None:
            print(f'{self.name} provide a list of the houses (cost, area):')
            for home in self.av_houses:
                print(f'{home.cost}, {home.area}')
        else:
            print(f'The realtor {self.name} has no suitable houses for sale')

    def give_discount(self):
        return self.give_discount

    def steal_money(self):
        if random.randint(0, 10) == 10:
            print(f'Realtor {self.name} have stolen your money')


if __name__ == '__main__':
    person_instance = Person("John", 32, 25000, 3000)
    house_instances1 = House(45000, 100)
    house_instances2 = House(50000, 120)
    house_instances3 = House(40150, 85)
    realtor_instance = Realtor("Mike", 0.20, [house_instances1, house_instances2, house_instances3])

    person_instance.info()
    person_instance.make_money()
    person_instance.income(100)
    realtor_instance.info()
    realtor_instance.give_discount()
    person_instance.buy_house(house_instances3)
    person_instance.income(180)
    person_instance.buy_house(house_instances3)

# Output:
# 32 years old man named John got his sevings: 25000 dollars - for buying a new house
# 	25000 dollars
# 	Today I have got my salary - 3000 dollars, so for now - 28000 dollars
# John work hard and get - 33000 dollars!
# Mike provide a list of the houses (cost, area):
# 45000, 100
# 50000, 120
# 40150, 85
# Not enough money to buy this house. It's time to earn some extra money.
# John work hard and get - 42000 dollars!
# Nice. I bought a new house. It's cost - 40150. i think it's time to move to a new home
