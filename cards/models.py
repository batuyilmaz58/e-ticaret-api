from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.

class Card(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='card')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Card"

    def get_total_price(self):
        total_price = sum(item.get_total_price() for item in self.items.all())
        return total_price

class CardItem(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
    
    def get_total_price(self):
        return self.product.price * self.quantity