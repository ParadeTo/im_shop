# -*- coding: utf-8 -*-
from django.db.models import Q
from django_filters import rest_framework as filters

from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    price_min = filters.NumberFilter(name="shop_price", lookup_expr="gte")
    price_max = filters.NumberFilter(name="shop_price", lookup_expr="lte")
    top_category = filters.NumberFilter(name="category", method='top_category_filter')
    # name = filters.CharFilter(name="name", lookup_expr="contains")

    # https://django-filter.readthedocs.io/en/latest/ref/filters.html
    # 得到一级类别下的所有商品
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value)|
                                   Q(category__parent_category_id=value)|
                                   Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']