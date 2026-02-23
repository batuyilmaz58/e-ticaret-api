from rest_framework import serializers
from .models import Address, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name']

class AddressListSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = ['id','fullname','district','city', 'street','address_type','user']

class AddressDetailsSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = ['id','fullname','phone','address_line','district','city', 'street','postal_code','address_type',
                  'is_default']

class AddressSerializer(serializers.ModelSerializer):
    # 'city' alanını ID yerine 'name' sütunu üzerinden eşleştirir
    city = serializers.SlugRelatedField(
        slug_field='name', 
        queryset=City.objects.all()
    )

    class Meta:
        model = Address
        fields = ['id', 'fullname', 'phone', 'address_line', 'district', 'city', 'street', 'postal_code', 'address_type', 'is_default']