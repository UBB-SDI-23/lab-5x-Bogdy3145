from django.test import TestCase
from django1.models import Brand


class BrandModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name="TestName", founding_year=2000, owner_name="Bogdan", hq_address="Cugir", rarity="com")

    def test_string_method(self):
        b = Brand.objects.get(name="TestName")
        expected_string = "TestName"
        self.assertEqual(str(b),expected_string)

        