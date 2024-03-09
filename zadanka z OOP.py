class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f'added {num1} to {num2} got {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f'multiplied {num1} with {num2} got {result}')
        return result


calc = Calculator()
history = calc.history
operation = calc.add(3, 10)


# print(history)


class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        return self.x, self.y, self.color

    def distance(self, other_shape):
        result1 = self.x - other_shape.x
        result2 = self.y - other_shape.y
        return result1 + result2

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie ({self.x, self.y})"


shape1 = Shape(2, 15, 'white')
shape2 = Shape(20, 5, 'blue')
print(shape1.describe())
print(shape2.describe())
print(shape2.distance(shape1))
print(shape1)
print(shape2)


class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0.0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if self.cash - amount < 0:
            cash = self.cash
            self.cash = 0
            return cash
        else:
            self.cash -= amount
            return amount

    def print_info(self):
        print(f'Numer konta {self.number}, stan konta {self.cash}')


class Employee:
    def __init__(self, id_, first_name, last_name):
        self.id_ = id_
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0.0

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0.0:
            self._salary = salary
        else:
            print('Podana wartość jest nieprawidłowa')


employee1 = Employee(1, 'Klaudia', 'Kochanie')
employee1.set_salary(500000000)
print(employee1._salary)
