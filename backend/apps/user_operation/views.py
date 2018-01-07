from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.models import UserFav
from user_operation.permissions import IsOwnerOrReadOnly
from user_operation.serializers import UserFavSerializer


class UserFavViewset(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    用户收藏
    """
    serializer_class = UserFavSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly) # 只能删除自己的收藏
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 搜索详情的时候所用的字段，默认是pk
    lookup_field = 'goods_id'

    # 这里其实已经过滤出来了只属于这个用户的商品
    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)
