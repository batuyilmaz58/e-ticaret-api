from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
ADDRESS_TYPE = [
    ('home','Home'),
    ('work','Work'),
    ('billing','Billing'),
    ('shipping','Shipping')
]

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    user = models.ForeignKey(User, related_name="adresses", on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address_line = models.CharField(max_length=255)
    district = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, related_name="adresses", on_delete=models.PROTECT)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    address_type = models.CharField(max_length=15, choices= ADDRESS_TYPE, default='home')
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.fullname} - {self.address_line} - {self.city}"
    
    class Meta:
        ordering = ["-created_at"]
