"""FreshMartOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from FreshMartOnline.settings import MEDIA_ROOT
# from goods.views import GoodsListView,
# from goods.views_base import GoodsListView

from goods.views import GoodsListViewSet, CategoryViewSet

# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet)

# 配置Category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    path(r'ueditor/', include('DjangoUeditor.urls')),
    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # 商品列表页
    # path('goods/', GoodsListView.as_view(),name="goods-list"),
    # path('goods/', goods_list,name="goods-list"),

    # router的path路径
    re_path('^', include(router.urls)),

    # drf自动化文档，title自定义
    path('docs', include_docs_urls(title='生鲜超市文档')),
    # 调试登录
    path('api-auth/', include('rest_framework.urls')),
]
