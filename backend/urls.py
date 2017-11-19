"""im_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

import xadmin
from settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewset

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 配置category的url
router.register(r'categorys', CategoryViewset, base_name='categorys')


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 商品列表页 method 1
    # url(r'goods/$', GoodsListView.as_view(), name="goods_list"),

    # 商品列表页 method 2
    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title="游先生的生鲜")),
]
