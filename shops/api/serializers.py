from shops.models import *
from rest_framework import serializers


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields=[field.name for field in Shop._meta.fields if field.name not in ['id']]

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields=[field.name for field in City._meta.fields if field.name not in ['id']]

class StreetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields=[field.name for field in Street._meta.fields if field.name not in ['id']]
