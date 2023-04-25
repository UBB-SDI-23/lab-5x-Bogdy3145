import random

ROWS_TO_GENERATE = 1000000
ROWS_PER_BATCH = 100

from faker import Faker
from constants import GENDER


class Customer:

    def __init__(self, name, year, address, gender, phone):
        self.name = name
        self.year = year
        self.address = address
        self.gender = gender
        self.phone = phone

    def __str__(self):
        return f'{self.name}, {self.year}, {self.address}, {self.gender}, {self.phone}'


def generate_customer(amount):
    faker: Faker = Faker()

    customers = []
    for i in range(amount):

        if i % (ROWS_PER_BATCH*50) == 0:
            print(f"Generated {i} rows")

        name = faker.name()
        year = faker.random_int(1920, 2023)
        address = faker.address()
        gender = random.choice(GENDER)
        phone = random.randint(100000000,999999999)

        customers.append(Customer(name, year, address, gender, phone))

    return customers


def generate_sql(customers):
    with open("customers.sql", "w") as file:
        file.write("TRUNCATE TABLE django1_customers RESTART IDENTITY CASCADE;")

    sql = "INSERT INTO django1_customers (name, year_of_birth, address, gender, phone) VALUES "
    i = 0
    for customer in customers:
        sql += f"('{customer.name}', '{customer.year}', '{customer.address}', '{customer.gender}', '{customer.phone}'),"
        if i % ROWS_PER_BATCH == 0:
            # write the sql to a file

            with open("customers.sql", "a") as file:
                file.write(sql[:-1] + ";")

            print(f"Written {i} rows to file")
            sql = "INSERT INTO django1_customers (name, year_of_birth, address, gender, phone) VALUES "

        i += 1

    if sql != "INSERT INTO django1_customers (name, year_of_birth, address, gender, phone) VALUES ":
        with open("customers.sql", "a") as file:
            file.write(sql[:-1] + ";")
        print(f"Written {i} rows to file - last batch")

    print("Done! :")


if __name__ == '__main__':
    customers = generate_customer(ROWS_TO_GENERATE)
    generate_sql(customers)