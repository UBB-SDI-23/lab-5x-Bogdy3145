import random

ROWS_TO_GENERATE = 1000000
ROWS_PER_BATCH = 1000

from faker import Faker
from constants import TYPES, ENGINES


class Car:

    def __init__(self, name, description, engine, type, year, hp):
        self.name = name
        self.description = description
        self.engine = engine
        self.type = type
        self.year = year
        self.hp = hp

    def __str__(self):
        return f'{self.name}, {self.description}, {self.engine}, {self.type}, {self.year}, {self.hp}'


def generate_cars(amount):
    faker: Faker = Faker()

    with open('usedbrands.txt', 'r') as f:
        txt = f.read()
        used_brands = txt.split('#')


    cars = []
    for i in range(amount):

        if i % (ROWS_PER_BATCH*50) == 0:
            print(f"Generated {i} rows")

        name=""
        while (name==""):
            name = random.choice(used_brands)
        description = faker.text()[:20]
        engine = random.choice(ENGINES)
        type = random.choice(TYPES)
        year = faker.random_int(1850, 2023)
        hp = faker.random_int(50, 1000)

        cars.append(Car(name, description, engine, type, year, hp))

    return cars


def generate_sql(cars):
    with open("cars.sql", "w") as file:
        file.write("TRUNCATE TABLE django1_cars RESTART IDENTITY CASCADE;")

    sql = "INSERT INTO django1_cars (name, description, engine, type, year, horsepower) VALUES "
    i = 0
    for car in cars:
        sql += f"('{car.name}', '{car.description}', '{car.engine}', '{car.type}', '{car.year}', '{car.hp}'),"
        if i % ROWS_PER_BATCH == 0:
            # write the sql to a file

            with open("cars.sql", "a") as file:
                file.write(sql[:-1] + ";")

            print(f"Written {i} rows to file")
            sql = "INSERT INTO django1_cars (name, description, engine, type, year, horsepower) VALUES  "

        i += 1

    if sql != "INSERT INTO django1_cars (name, description, engine, type, year, horsepower) VALUES ":
        with open("cars.sql", "a") as file:
            file.write(sql[:-1] + ";")
        print(f"Written {i} rows to file - last batch")

    print("Done! :")


if __name__ == '__main__':
    cars = generate_cars(ROWS_TO_GENERATE)
    generate_sql(cars)