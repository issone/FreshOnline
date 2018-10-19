# 扩展包安装
1.此处引用了xadmin和django-ueditor,因为django-ueditor不支持python3，且要给xadmin添加富文本插件，所以需要对源码进行修改，
故采用的源码安装方式，存于extra_apps中，方法自定制


# 常见问题
1.在django源码安装xadmin过程中遇到的问题，启动报错缺少模块的解决办法，如No module named 'crispy_forms'等问题解决办法
,参见
https://www.cnblogs.com/huchong/p/9818270.html

2.goods、trade等app中的配置没生效
 解决办法：
 方法一：如在goods中的__init__.py文件中写入default_app_config = 'goods.apps.GoodsConfig'，修改默认配置
 trade、user、user_operation中方法相同
 方法二：不用在app中的__init__.py里声明默认配置，直接在settings的INSTALLED_APPS中加入
 INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'goods.apps.GoodsConfig',
    'trade.apps.TradeConfig',
    'user_operation.apps.UserOperationConfig',
]

3.RuntimeError: Model class goods.models.GoodsCategory doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.这种类似的错误，
跟apps中的Config里的name有关，因为此处已将apps Mark Directory as Source Root，所以goods中的name=goods，而不是name=apps.goods
