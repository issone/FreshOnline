# -*- coding: utf-8 -*-

import django_filters

from goods.models import Goods


# https://django-filter.readthedocs.io/en/master/guide/usage.html  filter使用方法
class GoodsFilter(django_filters.rest_framework.FilterSet):
    '''
    商品的过滤类
    '''
    # 两个参数，field_name是要过滤的字段，lookup是执行的行为
    # 指定字段以及字段上的行为，在shop_price上大于等于
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')

    # 行为: 名称中包含某字符，且字符不区分大小写
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']
