from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from user_operation.models import UserFav
from user_operation.serializers import UserFavSerializer


class UserFavViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
