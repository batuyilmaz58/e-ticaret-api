from .models import Product
from categories.models import Category
import django_filters

class ProductFilter(django_filters.FilterSet):
    '''Product Filter'''
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='exact')
    
    class Meta:
        model = Product
        fields = {
            'name': ['iexact','exact','icontains'],
            'price': ['gte', 'lte'],
        }