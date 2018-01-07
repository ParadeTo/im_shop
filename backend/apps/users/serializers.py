# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers

#手机号码正则表达式
from rest_framework.validators import UniqueValidator

from users.models import VerifyCode

REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
User = get_user_model()

class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param attrs: 
        :return: 
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')

        # 是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码非法')

        # 验证发送频率
        one_minute_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minute_ago, mobile=mobile).count():
            raise serializers.ValidationError('发送太频繁')

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    # 返回给前端结果的时候，不会有这个字段
    code = serializers.CharField(write_only=True, label="验证码", required=True, max_length=4, min_length=4, help_text="验证码")
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")])
    password = serializers.CharField(style={'input': 'password'}, write_only=True)

    # 保存密码的一种方式
    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    def validate_code(self, code):
        # try:
        #     verify_records = VerifyCode.objects.get(mobile=self.initial_data["username"], code=code)
        # except VerifyCode.DoesNotExist as e:
        #     pass
        # except VerifyCode.MultipleObjectsReturned as e:
        #     pass

        # 注册的时候 username 是 mobile
        verify_records = VerifyCode.objects\
                            .filter(mobile=self.initial_data["username"])\
                            .order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            # 验证发送频率
            five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minute_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

            # 不需要返回，code只是用来做验证
            # return code
        else:
            raise serializers.ValidationError("验证码错误")

    class Meta:
        model = User
        fields = ('username', 'code', 'mobile', 'password')
        # write_only_fields = ('code', ) # 返回给前端结果的时候，不会有这个字段