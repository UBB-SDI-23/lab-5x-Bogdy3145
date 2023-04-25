import random

ROWS_TO_GENERATE = 1000000
ROWS_PER_BATCH = 1000

from faker import Faker
from constants import BRANDS, RARITY, CAR_NOUNS

used_brands = []

class Brand:
    # name = models.CharField(max_length = 128)
    # description = models.CharField(max_length = 512)
    # teacher = models.ForeignKey('Teacher', on_delete = models.CASCADE, related_name = "courses")
    # students = models.ManyToManyField('Student', through = 'StudentCourse')
    # fee = models.IntegerField()
    # size = models.IntegerField()

    def __init__(self, name, fy, on, rarity, hq, desc):
        self.name = name
        self.founding_year = fy
        self.owner_name = on
        self.rarity = rarity
        self.hq_address = hq
        self.description = desc

    def __str__(self):
        return f'{self.name}, {self.founding_year}, {self.owner_name}, {self.rarity}, {self.hq_address}, {self.description}'


def generate_brands(amount):
    faker: Faker = Faker()

    used_brands = []
    brands = []
    f = open("usedbrands.txt", "w")

    for i in range(amount):

        if i % (ROWS_PER_BATCH*50) == 0:
            print(f"Generated {i} rows")


        name = faker.company() + ' ' + faker.random_element(CAR_NOUNS) + ' ' + str(i)

        if (i<2000):
            f.write(str(name) + '#')
            #used_brands.append(name)

        fy = random.randint(1800,2023)
        on = faker.name()
        rarity = random.choice(RARITY)
        hq = faker.address()
        desc = faker.sentence(nb_words=10) + " " + faker.sentence(nb_words=10)

        brands.append(Brand(name, fy, on, rarity, hq, desc))

    f.close()
    return brands



def generate_sql(brands):
    with open("brands.sql", "w") as file:
        file.write("TRUNCATE TABLE django1_brand RESTART IDENTITY CASCADE;")

    sql = "INSERT INTO django1_brand (name, founding_year, owner_name, rarity, hq_address, description) VALUES "
    i = 0
    for brand in brands:
        sql += f"('{brand.name}', '{brand.founding_year}', '{brand.owner_name}', '{brand.rarity}', '{brand.hq_address}', '{brand.description}'),"
        if i % ROWS_PER_BATCH == 0:
            # write the sql to a file

            with open("brands.sql", "a") as file:
                file.write(sql[:-1] + ";")

            print(f"Written {i} rows to file")
            sql = "INSERT INTO django1_brand (name, founding_year, owner_name, rarity, hq_address, description) VALUES "

        i += 1

    if sql != "INSERT INTO django1_brand (name, founding_year, owner_name, rarity, hq_address, description) VALUES ":
        with open("brands.sql", "a") as file:
            file.write(sql[:-1] + ";")
        print(f"Written {i} rows to file - last batch")

    print("Done! :")


if __name__ == '__main__':
    brands = generate_brands(ROWS_TO_GENERATE)
    generate_sql(brands)