from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product
from users.models import CustomUser

# Create your models here.

class Comment(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(max_length=500, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment {self.id} - Rating: {self.rating}"