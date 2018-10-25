# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Goods

#Serializer实现商品列表页
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()


#ModelSerializer实现商品列表页
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'
#     #  category只显示分类的id，Serialzer还可以嵌套使用，覆盖外键字段


# class GoodsSerializer(serializers.ModelSerializer):
#     #覆盖外键字段
#     category = CategorySerializer()
#     class Meta:
#         model = Goods
#         fields = '__all__'