from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
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
    authentication_classes = (JSONWebTokenAuthentication, )

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)
