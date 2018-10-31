# encoding: utf-8

import json
import requests

# 线上部署时一定要将自己服务器的ip加入ip白名单中。测试时搜索本机ip地址。

class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【生鲜在线】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
            # 注意text内容必须要与后台已申请过签名并审核通过的模板保持一致
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("apikey的值")
    yun_pian.send_sms("2018", "手机号码")
