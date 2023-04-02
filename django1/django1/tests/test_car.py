from django.test import TestCase
from django1.models import Cars
from django1.models import Brand


class CarModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name="TestName", founding_year=2000, owner_name="Bogdan", hq_address="Cugir", rarity="com")

       # Cars.objects.create(name=Brand.objects.get(name=1), type="roa", description="desc", year="2000", horsepower=100, engine="V12")

    #def test_string_method(self):
        #c = Cars.objects.get(name="TestName")
        #expected_string = "TestName desc V12 roa 2000"
        #print(str(c))
        #self.assertEqual(str(c), expected_string)

