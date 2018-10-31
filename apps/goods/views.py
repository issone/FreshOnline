from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView

from goods.serializers import GoodsSerializer, CategorySerializer
from goods.filters import GoodsFilter
from goods.models import Goods, GoodsCategory


class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


# class GoodsListView(APIView):
#     '''
#     商品列表
#     '''
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serialzer = GoodsSerializer(goods,many=True)
#         return Response(goods_serialzer.data)

# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     '商品列表页'
#     # 用的时候需要定义queryset和serializer_class
#     # GenericAPIView里面默认为空
#     # queryset = None
#     # serializer_class = None
#     # ListModelMixin里面list方法帮我们做好了分页和序列化的工作，只要调用就好了
#     # 需要在settings中配置分页功能

#   #REST_FRAMEWORK = {
#       # 分页
#       # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#       # 每页显示的个数
#       #'PAGE_SIZE': 10,
#    }
#
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class GoodsListView(generics.ListAPIView):
#     '商品列表页'
#
#     pagination_class = GoodsPagination    #分页
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '商品列表页'

    # 分页
    pagination_class = GoodsPagination
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter

    # # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # 设置排序字段
    ordering_fields = ('sold_num', 'shop_price')

    # 设置我们的search字段
    # 搜索,=name表示精确搜索，
    # ^ Starts-with search.
    # = Exact matches.
    # @ Full-text search. (Currently only supported Django's MySQL backend.)
    # $ Regex search.
    search_fields = ('name', 'goods_brief', 'goods_desc')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
     list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    '''

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer