from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, default="0",null=False, unique=True)
    founding_year = models.IntegerField(default="0", null=True)
    owner_name = models.CharField(max_length=200, default="0", null=True)
    rarity = models.CharField(max_length=200, default="0", null=True)
    hq_address = models.CharField(max_length=200, default="0", null=True)
    # no_of_employees = models.IntegerField(default="0", null=True)

    # car = models.CharField(max_length=200, default="-1", null=True)

    def __str__(self):
        #return self.name + ' ' + str(self.founding_year) + ' ' + self.owner_name + ' ' + self.rarity + ' ' + self.hq_address
        return self.name


class Cars(models.Model):
    name = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    # name = models.CharField(max_length=200, default="0")
    description = models.CharField(max_length=500, default="0")
    engine = models.CharField(max_length=100, default="0")
    type = models.CharField(max_length=100, default="0")
    year = models.IntegerField(default="0")
    horsepower = models.IntegerField(default="0")

    def __str__(self):
        return str(self.name) + ' ' + self.description + ' ' + self.engine + ' ' + self.type + ' ' + str(self.year) + ' ' + str(self.horsepower)


class Customers(models.Model):
    name = models.CharField(max_length=200)
    year_of_birth = models.IntegerField(default="0")
    address = models.CharField(max_length=500, default="0")
    gender = models.CharField(max_length=100, default="0")
    phone = models.IntegerField(default="0")

    def __str__(self):
        return str(self.name)


class CarOwnership(models.Model):
    car_id=models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="car_id")
    customer_id=models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="customer_id")
    date=models.DateField(default="2000-10-10")
    name_of_dealer = models.CharField(max_length=200, default="0")
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.customer_id) + " " + str(self.car_id)