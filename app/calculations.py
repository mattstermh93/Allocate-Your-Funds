class Calculations():
    def __init__(self, age, salary):
        self.age = age
        self.salary = salary

    def stocks(self):
        pass

    def holdCash(self):
        return 'This is a string, going to the results.html file'

    def bonds(self):
        pass

    def five_percent(self):
        user_salary = (self.salary * 0.05)
        return int(user_salary)
