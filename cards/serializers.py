from rest_framework import serializers
from .models import Card, CardItem
from decimal import Decimal

class EmptySerializer(serializers.Serializer):
    pass

class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1, min_value=1)

class CartItemUpdateSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=0)

class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product.id", read_only=True)  # Product id
    name = serializers.CharField(source="product.name", read_only=True)
    price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2, read_only=True)
    image = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CardItem
        fields = [
            "id",   
            "product_id",     
            "name",
            "price",
            "image",
            "quantity",
            "total_price",
        ]

    def get_image(self, obj) -> str:
        image = obj.product.images.first()
        if image:
            return image.image.url
        return None

    def get_total_price(self, obj) -> Decimal:
        return obj.get_total_price()

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Card
        fields = ['id','user','items','total_price']

    def get_total_price(self, obj) -> Decimal:
        return obj.get_total_price()
