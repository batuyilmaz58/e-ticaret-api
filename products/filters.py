from .models import Product
import django_filters

class ProductFilter(django_filters.FilterSet):
    '''Product Filter'''
    class Meta:
        model = Product
        fields = {
            'name': ['iexact','exact','icontains'], # name alanında arama yaparken büyük küçük harf duyarsız arama yapar
            'price': ['gte', 'lte'], # price alanında greater than or equal (gte) ve less than or equal (lte) filtreleri ekler
            'category': ['exact'], # category alanında tam eşleşme yapar
            }