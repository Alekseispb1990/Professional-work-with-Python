from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees
from application.srapping import pars_url


def main():
    print(datetime.now().strftime('%X %A %d-%m-%Y'))
    calculate_salary()
    get_employees()
    pars_url('https://ya.ru/')


if __name__ == '__main__':
    main()
