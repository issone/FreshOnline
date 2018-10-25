# -*- coding: utf-8 -*-

from django.views import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        # for good in goods:
        #     json_dict = {}
        #    # 获取商品的每个字段，键值对形式
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_dict["add_time"] = good.add_time
        #     json_list.append(json_dict)

        # from django.http import HttpResponse
        # import json
        # #返回json，一定要指定类型content_type='application/json'
        # return HttpResponse(json.dumps(json_list),content_type="application/json")

        # from django.forms.models import model_to_dict  # model_to_dict 将model转换为字典，不用一个字段一个字段提取。
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # images field和 datetime直接dumps会出错
        # serializers 专门用于序列化，有了这个序列化，其实上面的model_to_dict都不用做了
        # 关于序列化，推荐阅读：https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138683221577998e407bb309542d9b6a68d9276bc3dbe000
        import json
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse

        # In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(json_data, safe=False)
        # jsonResponse做的工作也就是加上了dumps和content_type
        # return HttpResponse(json.dumps(json_data), content_type="application/json")
        # 注释掉loads，下面语句正常
        # return HttpResponse(json_data, content_type="application/json")

        #django的serializer虽然可以很简单实现序列化，但是字段序列化定死的，要想重组的话非常麻烦,image字段返回的是相对路径,需要补全前缀
