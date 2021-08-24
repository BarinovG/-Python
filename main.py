from application import salary
from application.db import people
from datetime import datetime


def hello():
    print('Hello World!')

if __name__ == '__main__':
    print(datetime.now())
    hello()
    salary.calculate_salary()
    people.get_employees('Ivan')
