import random

ROWS_TO_GENERATE = 10000000
ROWS_PER_BATCH = 1000

from faker import Faker
from constants import GENDER


class CarOwnership:

    def __init__(self, car_id, customer_id, date, name_dealer, price):
        self.car_id = car_id
        self.customer_id = customer_id
        self.date = date
        self.name_dealer = name_dealer
        self.price = price


    def __str__(self):
        return f'{self.car_id}, {self.customer_id}, {self.date}, {self.name_dealer}, {self.price}'


def generate_carownership(amount):
    faker: Faker = Faker()

    carownership = []
    for i in range(amount):

        if i % (ROWS_PER_BATCH*50) == 0:
            print(f"Generated {i} rows")

        car_id = random.randint(1,999)
        customer_id = random.randint(1,999)
        date = faker.date()
        #date = faker.date_between(start_date='2000-01-01', end_date='2023-12-31')
        name_dealer = faker.name()
        price = random.randint(1000,9999999)

        carownership.append(CarOwnership(car_id, customer_id, date, name_dealer, price))

    return carownership


def generate_sql(carownerships):
    with open("carownership.sql", "w") as file:
        file.write("TRUNCATE TABLE django1_carownership RESTART IDENTITY CASCADE;")

    sql = "INSERT INTO django1_carownership (car_id_id, customer_id_id, date, name_of_dealer, price) VALUES "
    i = 0
    for carownership in carownerships:
        sql += f"('{carownership.car_id}', '{carownership.customer_id}', '{carownership.date}', '{carownership.name_dealer}', '{carownership.price}'),"
        if i % ROWS_PER_BATCH == 0:
            # write the sql to a file

            with open("carownership.sql", "a") as file:
                file.write(sql[:-1] + ";")

            print(f"Written {i} rows to file")
            sql = "INSERT INTO django1_carownership (car_id_id, customer_id_id, date, name_of_dealer, price) VALUES "

        i += 1

    if sql != "INSERT INTO django1_carownership (car_id_id, customer_id_id, date, name_of_dealer, price) VALUES ":
        with open("carownership.sql", "a") as file:
            file.write(sql[:-1] + ";")
        print(f"Written {i} rows to file - last batch")

    print("Done! :")


if __name__ == '__main__':
    carownerships = generate_carownership(ROWS_TO_GENERATE)
    generate_sql(carownerships)