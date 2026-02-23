from .models import Comment
import django_filters


class CommentFilter(django_filters.FilterSet):
    product = django_filters.NumberFilter(field_name='product_id')
    user = django_filters.NumberFilter(field_name='user_id')
    
    class Meta:
        model = Comment
        fields = ['product', 'user']