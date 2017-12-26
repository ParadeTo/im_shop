from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from user_operation.models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    # 当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已收藏"
            )
        ]

        fields = ('user', 'goods', "id")