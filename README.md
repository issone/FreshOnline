#环境搭建
##1.django2.0需要安装的xadmin版本，
1.源码包下载地址：
https://github.com/sshwsfc/xadmin/tree/django2
下载完成后
2.pip install 你下载的压缩包的位置
3. 安装成功后，在settings.py中的INSTALLED_APPS里加入'xadmin','crispy_forms'
4.在urls.py 中导入xadmin,并配置url

## 安装适合python3版本的DjangoUeditor
# 直接复制extra_apps中的包文件，
把extra_apps  进行Mark Directory as sources root操作,然后settings中也要加路径,方便导入
import sys
sys.path.insert(0,BASE_DIR)
sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))
在settings.py中的INSTALLED_APPS里加入'DjangoUeditor'