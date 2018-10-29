# -*- coding: utf-8 -*-

from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    '''三级分类'''

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    '''
    二级分类
    '''
    # 在parent_category字段中定义的related_name="sub_cat" ,这里的sub_cat 是因为我们在自身的继承关系中将这种关系进行了命名

    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    # 如何通过一级分类(parents)拿到二级分类，一类对象直接father.subcat
    # 此时的sub_cat就变成了拿到的二类数据，但是对于此时拿到的二类数据，我们依然希望它进行序列化。
    # 因为我们此时通过一类拿到的二类有很多，所以必须加上many = True的参数
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# Serializer实现商品列表页
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()


# ModelSerializer实现商品列表页
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
