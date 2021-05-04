# 1.
# Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class

from abc import abstractmethod, ABC

class Animal:
    """
    Parent class, should have eat, sleep
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.__class__.__name__} is eating")

    def sleep(self):
        print(f"{self.__class__.__name__} is sleeping")

    """
    Some of the animal with 1-2 extra methods related to this animal
    """


class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks!")

    def run(self):
        print(f"{self.name} is running for a ball")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing!")


class Owl(Animal):
    def hoot(self):
        print(f"{self.name} is hooting!")


class Frog(Animal):
    def caw(self):
        print(f"{self.name} is cawing!")


class Penguin(Animal):
    def __init__(self, color, name, age):
        super().__init__(name, age)
        self.color = color

    def croak(self):
        print(f"{self.name} is a {self.age} y.o. ROyal penguin. Most of them lives in the archipelagos of the Pacific "
              f"and Indian oceans. They have {self.color} color of plumage and usually croaking!")


dog = Dog('Jack', 4)
cat = Cat('Mikky', 7)
owl = Owl('Phoenix', 2)
frog = Frog('Jumpy', 1)
penguin = Penguin('rich black, white and yellow', 'Jimbo', 3)

dog.bark()
dog.run()
cat.meow()
owl.hoot()
frog.caw()
penguin.croak()

for animal in (dog, cat, owl, frog, penguin):
    print(isinstance(animal, Animal))

# Output:
# Jack barks!
# Jack is running for a ball
# Mikky is meowing!
# Phoenix is hooting!
# Jumpy is cawing!
# Jimbo is a 3 y.o. Royal penguin. Most of them lives in the archipelagos of the Pacific and Indian oceans.
# They have rich black, white and yellow color of plumage and usually croaking!
# True
# True
# True
# True
# True

# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
# create an instance of Centaur class and call the common method of these classes and unique.


class Human:
    """
    Human class, should have eat, sleep, study, work
    """

    def eat(self):
        print(f"{self.__class__.__name__} is eating")

    def sleep(self):
        print(f"{self.__class__.__name__} is sleeping")

    def study(self):
        print(f"{self.__class__.__name__} is studying")

    def work(self):
        print(f"{self.__class__.__name__} is working")


class Centaur(Human, Animal):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """
    def run(self):
        print(f"{self.__class__.__name__} is running away")


Argon = Centaur("Argon", 72)
Argon.eat()
Argon.sleep()
Argon.run()

# Output:
# Centaur is eating
# Centaur is sleeping
# Centaur is running away

# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
# a.


class Person:
    """
    Make the class with composition.
    """
    def __init__(self):
        left_arm = Arm("This is left arm")
        right_arm = Arm("This is right arm")
        self.arms = [left_arm, right_arm]


class Arm:
    """
    Make the class with composition.
    """
    def __init__(self, inf):
        self.inf = inf


person = Person()
for arm in person.arms:
    print(arm.inf)

# Output:
# This is left arm
# This is right arm

# b.


class CellPhone:
    """
    Make the class with aggregation
    """
    def __init__(self, screen):
        self.screen = screen


class Screen:
    """
    Make the class with aggregation
    """
    def __init__(self, screen_type):
        self.screen_type = screen_type


screen = Screen('Touch screen')
cell_phone = CellPhone(Screen)
print(screen.screen_type)

# Output:
# Touch screen

# 3.


class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """

    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.info = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age,
                     self.sex]

    def __repr__(self):
        return f"Profile for review: {self.info}"


profile = Profile("Mikhail", "Chabanenko", "+380688678554", "Kiev, Dovzenko str.", "mikhail.chabanenko@gmail.com",
                  "15.07.1991", "129", "man")
print(profile)

# Output:
# Profile for review: ['Mikhail', 'Chabanenko', '+380688678554', 'Kiev, Dovzenko str.', 'mikhail.chabanenko@gmail.com',
# '15.07.1991', '129', 'man']

# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.


class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, laptop_screen, laptop_keyboard, laptop_touchpad, laptop_webcam, laptop_ports, laptop_dynamics):
        self.laptop_screen = laptop_screen
        self.laptop_keyboard = laptop_keyboard
        self.laptop_touchpad = laptop_touchpad
        self.laptop_webcam = laptop_webcam
        self.laptop_ports = laptop_ports
        self.laptop_dynamics = laptop_dynamics

    def screen(self):
        print(f'Screen: {self.laptop_screen}')

    def keyboard(self):
        print(f'Keyboard language: {self.laptop_keyboard}')

    def touchpad(self):
        print(f'Touchpad: {self.laptop_touchpad}')

    def webcam(self):
        print(f'Webcam: {self.laptop_webcam}')

    def ports(self):
        print(f'Ports: {self.laptop_ports}')

    def dynamics(self):
        print(f'Dynamics: {self.laptop_dynamics}')


laptop = HPLaptop("IPS", "Rus", "Touchpad with on/off button", "Integrated HD 720p webcam with dual-microphone array",
                  "2 SuperSpeed USB Type-A, 1 SuperSpeed USB, Type-C®, 1 RJ-45, 1 headphone/microphone combo, 1 HDMI 1.4b, 1 AC power",
                  "Dual stereo speakers, dual array microphone")

laptop.screen()
laptop.keyboard()
laptop.touchpad()
laptop.webcam()
laptop.ports()
laptop.dynamics()

# Output:
# Screen: IPS
# Keyboard language: Rus
# Touchpad: Touchpad with on/off button
# Webcam: Integrated HD 720p webcam with dual-microphone array
# Ports: 2 SuperSpeed USB Type-A, 1 SuperSpeed USB, Type-C®, 1 RJ-45, 1 headphone/microphone combo, 1 HDMI 1.4b, 1 AC power
# Dynamics: Dual stereo speakers, dual array microphone