
# 云片
短信验证码

# json web token
简书->日记本

将jwt的cookie设置到顶级域名之下！

## 认证接口的流程

```
# jwt 的认证接口
url(r'^login/', rest_framework_jwt.views.obtain_jwt_token)


class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer
    
from django.contrib.auth import authenticate
class JSONWebTokenSerializer(Serializer):
    ...
    user = authenticate(**credentials)
    
def authenticate(request=None, **credentials):
    """
    If the given credentials are valid, return a User object.
    """
    # backend_path = 'django.contrib.auth.backends.ModelBackend'
    for backend, backend_path in _get_backends(return_tuples=True):
        try:
            user = _authenticate_with_backend(backend, backend_path, request, credentials)
        except PermissionDenied:
        
class ModelBackend(object):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
```

## 自己实现这个backend
setting.py

```
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
```


# django shell
```
python manage.py shell
import django
django.setup()
```

# drf 的 request 和 response

# Apiview, GenericView, Viewset 和 router 的原理分析
```javascript
View (django)
^
|
APIView (drf)
^
|
GenericAPIView (drf)
^
|
GenericViewSet(ViewSetMixin, generics.GenericAPIView) (drf)

    ReadOnlyModelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet)
    ...
    
    

mixin
    CreateModelMixin + GenericAPIView => CreateAPIView
    ListModelMixin                    => ListAPIView
        f: get => list
    RetrieveModelMixin                => RetrieveAPIView
        f: get => retrieve
    UpdateModelMixin
    DestroyModelMixin

ViewSetMixin
    f: initialize_request
    f: as_view 通过该方法实现路由到方法的绑定
    goods_list = GoodsListViewSet.as_view({'get': 'list'})
    或者通过router来默认绑定
    router.register(r'goods', GoodsListViewSet)

```


# restful 优点
* 轻量，不需要额外的协议，http method 本身有语义
* 面向资源，自解释性

# 为什么前后端分离
* pc，app，pad 多端适应
* SPA 开发流行
* 前后端开发职责不清
* 开发效率
* 模板与后端语言耦合

# 前后端分离的缺点
* 学习门槛增加
* 文档重要性增加
* SEO难度增加

# migration
django_migrations 这张表记录了已执行过的命令

# 问题
* 使用pymysql
```python
__init__.py
import pymysql
pymysql.install_as_MySQLdb()
```

* python 包地址
www.lfd.uci.edu/~gohlke/pythonlibs/

* 创建innodb的表
settings.py

'OPTIONS': { 'init_command': 'SET default_storage_engine=INNODB' },

* 用户

```angular2html
{"username":"admin", "password":"admin123"}
```

* 博客地址

`http://projectsedu.com`