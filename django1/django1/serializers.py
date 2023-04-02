from rest_framework import serializers
from .models import Cars
from .models import Brand
from .models import Customers
from .models import CarOwnership

class CarsSerializer(serializers.ModelSerializer):

    #id = serializers.IntegerField(write_only=True)
    #name = serializers.CharField(max_length=255)
    name = serializers.SlugRelatedField(queryset=Brand.objects.all(),slug_field='name')

    description = serializers.CharField(max_length=255)
    engine = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    year = serializers.IntegerField(read_only=True)
    horsepower = serializers.IntegerField(read_only=True)


    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', 'engine', 'type', 'year', 'horsepower']


class CarsSerializer2(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(queryset=Brand.objects.all(), slug_field='name')
    description = serializers.CharField(max_length=255)
    engine = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    horsepower = serializers.IntegerField()

    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', 'engine', 'type', 'year', 'horsepower']

    def validate_year(self,value):
        if value < 1800:
            raise serializers.ValidationError("Year can not be less than 1800")
        return value

    def validate_horsepower(self,value):
        if value < 0:
            raise serializers.ValidationError("Hp can not be less than 0")
        return value

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', 'engine', 'type', 'year', 'horsepower']
        depth=1


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name', 'founding_year', 'owner_name', 'rarity', 'hq_address']




class BrandDetailSerializer(serializers.ModelSerializer):
    cars = CarsSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'founding_year', 'owner_name', 'rarity', 'hq_address', 'cars']


class BrandWithCarSerializer(serializers.ModelSerializer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.car = serializers.IntegerField(required=False)

    name = serializers.CharField(max_length=255)
    founding_year = serializers.IntegerField()
    owner_name = serializers.CharField(read_only=True)
    rarity = serializers.CharField(read_only=True)
    hq_address = serializers.CharField(read_only=True)

    # car = serializers.SlugRelatedField(queryset=Cars.objects.all(), slug_field='id', required=False)
    #car = serializers.IntegerField(required=False)

    def update_car(self):
        Cars.objects.filter(id=int(str(self.car))).update(name=self.name)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'founding_year', 'owner_name', 'rarity', 'hq_address', 'car']

class BrandCarSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(max_length=255)
    car_id = serializers.CharField(max_length=255)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'car_id']


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = ['id', 'name', 'year_of_birth', 'address','gender', 'phone']


class CustomerDetailSerializer(serializers.ModelSerializer):
    cars_sold = serializers.SerializerMethodField()

    class Meta:
        model = Customers
        fields = ['id', 'name', 'year_of_birth', 'address','gender', 'phone', 'cars_sold']

    def get_cars_sold(self,obj):

        cars_sold = CarOwnership.objects.filter(customer_id=obj)
        return CarOwnershipSerializer(cars_sold, many=True).data


class CarOwnershipSerializer(serializers.ModelSerializer):
    car_id = serializers.SlugRelatedField(queryset=Cars.objects.all(), slug_field='id')
    customer_id = serializers.SlugRelatedField(queryset=Customers.objects.all(), slug_field='name')
    date = serializers.DateField()
    name_of_dealer = serializers.CharField(max_length=200, default="0")
    price = serializers.IntegerField(default="0")

    class Meta:
        model = CarOwnership
        fields = ['id', 'car_id', 'customer_id', 'date', 'name_of_dealer', 'price']


class CarOwnershipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOwnership
        fields = ['id', 'car_id', 'customer_id', 'date', 'name_of_dealer', 'price']
        depth=1


class StatisticSerializer(serializers.ModelSerializer):
    avg_production_year = serializers.IntegerField(read_only=True)
    car_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'avg_production_year', 'car_count']


class StatisticFoundingSerializer(serializers.ModelSerializer):
    avg_hp = serializers.IntegerField(read_only=True)
    car_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'avg_hp', 'car_count']