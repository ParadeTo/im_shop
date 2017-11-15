import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        # method1
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market'] = good.market_price
        #     json_list.append(json_dict)

        # method2 ImageField 不能序列化
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        # method3 多了 pk 和 model
        json_data = serializers.serialize("json", goods)
        json_list = json.loads(json_data)


        return JsonResponse(json_list, safe=False)