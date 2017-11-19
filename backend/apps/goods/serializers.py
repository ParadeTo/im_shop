# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Goods
from .models import GoodsCategory

# method 1 自己一个个写字段
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField() # 会加上 media
#
#     def create(self, validated_data):
#         """
#         validated_data 就是上面的那些字段
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Goods.objects.create(**validated_data)

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    # 子类别即三级类别
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# method 2 直接用Model中的字段
class CategorySerializer(serializers.ModelSerializer):
    # 子类别即二级类别
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"
        # fields = ('name', 'click_num', 'market_price', 'add_time') # 需要的字段
