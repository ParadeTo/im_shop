from rest_framework import status, mixins, generics, viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .filters import GoodsFilter
from .pagination import CustomPagination
from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory


# method 1
# class GoodsListView(APIView):
#     """
#     返回列表
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() # 调用 create 方法
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# method 2
# class GoodsListView(mixins.ListModelMixin,
#                     generics.GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# method 3
# class GoodsListView(generics.ListAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = CustomPagination


# method 4
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = CustomPagination

    # django-filter +  restframework.filters
    """
    SearchFilter->filter_queryset->orm_lookups:
    ['name__icontains', 'goods_brief__icontains', 'goods_desc__icontains']
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('shop_price', 'sold_num')

    # def get_queryset(self):
    #     queryset = Goods.objects.all() # 并没有执行
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset = Goods.objects.filter(shop_price__gt=int(price_min))
    #     return queryset

class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    List:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer