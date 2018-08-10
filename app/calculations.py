import locale
locale.setlocale( locale.LC_ALL, '' )

class Calculations():
    def __init__(self, age, salary, risk):
        self.age = age
        self.salary = float(salary)
        self.risk = risk

    #method is called if user is risky
    def stocks_yes(self):
        user_stock = (120 - self.age)
        return locale.currency(user_stock, grouping=True)

    #method is called if user is risk averse
    def stocks_no(self):
        user_stock = (98 - self.age)
        return locale.currency(user_stock, grouping=True)

    #calculates how much $ the user should hold
    def five_percent(self):
        user_salary = (self.salary * 0.05)
        return locale.currency(user_salary, grouping=True)

    #displayed in table header
    def get_age(self):
        return self.age

    #displayed in table header
    def get_salary(self):
        return locale.currency(self.salary, grouping=True)

    #displayed in table header
    def is_risky(self):
        return self.risk

    #determines how much we recommend the user invest in stocks
    def get_risk(self):
        if self.age == 'yes' or 'Yes':
            return Calculations.stocks_yes(self)
        else:
            return Calculations.stocks_no(self)
