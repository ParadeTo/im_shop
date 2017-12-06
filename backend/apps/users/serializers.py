# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers

#手机号码正则表达式
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