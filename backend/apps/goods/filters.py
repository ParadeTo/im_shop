# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters

from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    price_min = filters.NumberFilter(name="shop_price", lookup_expr="gte")
    price_max = filters.NumberFilter(name="shop_price", lookup_expr="lte")
    name = filters.CharFilter(name="name", lookup_expr="contains")

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']