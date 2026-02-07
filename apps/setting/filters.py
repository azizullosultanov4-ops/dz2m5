import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    search = django_filters.CharFilter(method='filter_by_title')

    class Meta:
        model = Product
        fields = ['category', 'model']

    def filter_by_title(self, queryset, name, value):
        return queryset.filter(title__icontains=value)
