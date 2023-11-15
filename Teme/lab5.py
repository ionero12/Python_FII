import math
from typing import Union, Optional


# 1. Create a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle,
# Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.

class Shape:
    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3


# 2 Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount.
# Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> Union[None, str]:
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient funds"

    def calculate_interest(self) -> float:
        return 0.0

class SavingsAccount(Account):
    def __init__(self, account_number: str, balance: float, interest_rate: float):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self) -> float:
        return self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number: str, balance: float, overdraft_limit: float):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> Union[None, str]:
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            return "Insufficient funds and overdraft limit exceeded"


# 3 Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific
# types of vehicles like Car, Motorcycle, and Truck. Add methods to calculate mileage or towing capacity based on the
# vehicle type.

class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def calculate_mileage(self) -> Optional[float]:
        return None


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, fuel_efficiency: float):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self) -> float:
        return self.fuel_efficiency


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, fuel_efficiency: float):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self) -> float:
        return self.fuel_efficiency


class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, towing_capacity: Union[float, None] = None):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self) -> Union[float, None]:
        return self.towing_capacity


# 4 Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like
# Manager, Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their
# roles.

class Employee:
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id

    def display_info(self) -> str:
        return f"{self.employee_id}: {self.name}"


class Manager(Employee):
    def __init__(self, name: str, employee_id: int, salary: float, department: str):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def calculate_bonus(self) -> float:
        return self.salary * 0.1


class Engineer(Employee):
    def __init__(self, name: str, employee_id: int, salary: float, programming_language: str):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def code(self) -> str:
        return f"{self.name} is coding in {self.programming_language}"


class Salesperson(Employee):
    def __init__(self, name: str, employee_id: int, salary: float, sales_target: float):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def calculate_commission(self) -> float:
        return self.sales_target * 0.05


# 5 Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal,
# Bird, and Fish. Add properties and methods to represent characteristics unique to each animal group.

class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def make_sound(self) -> str:
        return "Generic animal sound"


class Mammal(Animal):
    def __init__(self, name: str, species: str, fur_color: str):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self) -> str:
        return "Live birth"


class Bird(Animal):
    def __init__(self, name: str, species: str, wing_span: float):
        super().__init__(name, species)
        self.wing_span = wing_span

    def fly(self) -> str:
        return f"{self.name} is flying with a wing span of {self.wing_span} meters"


class Fish(Animal):
    def __init__(self, name: str, species: str, scale_color: str):
        super().__init__(name, species)
        self.scale_color = scale_color

    def swim(self) -> str:
        return f"{self.name} is swimming with {self.scale_color} scales"


# 6 Design a library catalog system with a base class LibraryItem and subclasses for different types of items like
# Book, DVD, and Magazine. Include methods to check out, return, and display information about each item.

class LibraryItem:
    def __init__(self, title: str, call_number: str, available: bool = True):
        self.title = title
        self.call_number = call_number
        self.available = available

    def display_info(self) -> str:
        return f"{self.title} ({self.call_number}) - {'Available' if self.available else 'Checked Out'}"

    def check_out(self) -> Optional[str]:
        if self.available:
            self.available = False
            return f"{self.title} has been checked out"
        else:
            return f"{self.title} is already checked out"

    def return_item(self) -> Optional[str]:
        if not self.available:
            self.available = True
            return f"{self.title} has been returned"
        else:
            return f"{self.title} is already available"


class Book(LibraryItem):
    def __init__(self, title: str, call_number: str, author: str, genre: str):
        super().__init__(title, call_number)
        self.author = author
        self.genre = genre


class DVD(LibraryItem):
    def __init__(self, title: str, call_number: str, director: str, duration: int):
        super().__init__(title, call_number)
        self.director = director
        self.duration = duration


class Magazine(LibraryItem):
    def __init__(self, title: str, call_number: str, issue_number: int):
        super().__init__(title, call_number)
        self.issue_number = issue_number


# Ex 1
circle = Circle(5)
print(f"The area for circle is: {circle.area()} and the perimeter is: {circle.perimeter()}")
rectangle = Rectangle(5, 10)
print(f"The area for rectangle is: {rectangle.area()} and the perimeter is: {rectangle.perimeter()}")
triangle = Triangle(3, 4, 5)
print(f"The area for triangle is: {triangle.area()} and the perimeter is: {triangle.perimeter()} \n")

# Ex 2
savings_account = SavingsAccount("SA123", 1000.0, 0.02)
checking_account = CheckingAccount("CA456", 500.0, 100.0)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_interest = savings_account.calculate_interest()
checking_account.deposit(200)
checking_account.withdraw(400)
print(f"Savings Account Balance: {savings_account.balance}")
print(f"Savings Account Interest: {savings_interest}")
print(f"Checking Account Balance: {checking_account.balance} \n")

# Ex 3
car = Car("Toyota", "Aygo", 2022, 30.0)
motorcycle = Motorcycle("Yamaha", "Kawasaki", 2020, 40.0)
truck = Truck("Ford", "F-150", 2018, 10000.0)
car_mileage = car.calculate_mileage()
motorcycle_mileage = motorcycle.calculate_mileage()
truck_towing_capacity = truck.calculate_towing_capacity()
print(f"{car.display_info()} - Mileage: {car_mileage} MPG")
print(f"{motorcycle.display_info()} - Mileage: {motorcycle_mileage} MPG")
print(f"{truck.display_info()} - Towing Capacity: {truck_towing_capacity} lbs \n")

# Ex 4
manager = Manager("Maria Catavencu", 101, 80000.0, "Sales")
engineer = Engineer("Marius Ion", 102, 70000.0, "Python")
salesperson = Salesperson("Denisa Lica", 103, 60000.0, 1000000.0)
manager_bonus = manager.calculate_bonus()
engineer_code = engineer.code()
salesperson_commission = salesperson.calculate_commission()
print(f"{manager.display_info()} - Bonus: ${manager_bonus}")
print(f"{engineer.display_info()} - {engineer_code}")
print(f"{salesperson.display_info()} - Commission: ${salesperson_commission} \n")

# Ex 5
mammal = Mammal("Leu", "Panthera Leo", "Auriu")
bird = Bird("Vultur", "Aquila chrysaetos", 2.5)
fish = Fish("Clownfish", "Amphiprioninae", "Orange")
mammal_birth = mammal.give_birth()
bird_flight = bird.fly()
fish_swim = fish.swim()
print(f"{mammal.name} ({mammal.species}) - Fur color: {mammal.fur_color}, Birth: {mammal_birth}")
print(f"{bird.name} ({bird.species}) - Wing span: {bird.wing_span} meters, {bird_flight}")
print(f"{fish.name} ({fish.species}) - Scale color: {fish.scale_color}, {fish_swim} \n")

# Ex 6
book = Book("Moara cu noroc", "F123.45", "Ioan Slavici", "Epic")
dvd = DVD("Inception", "D456.78", "Christopher Nolan", 150)
magazine = Magazine("National Geographic", "M789.01", 123)
book_check_out = book.check_out()
dvd_return = dvd.return_item()
magazine_check_out = magazine.check_out()
print(book.display_info())
print(f"Check Out: {book_check_out}")
print(dvd.display_info())
print(f"Return: {dvd_return}")
print(magazine.display_info())
print(f"Check Out: {magazine_check_out} \n")
