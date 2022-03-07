# coding=utf-8

import requests
import re


class Main(object):
    def __init__(self):
        self.session = requests.session()
        self.session.headers.update({
                                        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/WIFI Language/zh_CN"})

    def get_A(self):
        try:
            url = "http://idea.94goo.com/key"
            res = self.session.get(url)
            return re.findall('class="new-key" value="(.*?)">', res.text)[0]
        except Exception:
            return None

    def get_B(self, actype):
        '''
        修改actype可以获得4个激活码
        :return:
        '''
        try:
            url = "http://idea.javatiku.cn/gencode.action"
            res = self.session.get(url)
            vf_code = re.findall("<h1>(\S+)</h1>", res.text)

            self.session.get("http://idea.javatiku.cn/")
            url2 = "http://idea.javatiku.cn/rpc/getkey.action"
            data = {"validCode": vf_code[0], "actype": actype}
            res1 = self.session.post(url2, data=data).json()['data']
            return res1
        except Exception:
            return None

    def get_C(self, case):
        '''
        存在两个激活码
        :return:
        '''
        self.session.headers.update({
                                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"})
        url = 'http://idea521.com/downloadcode'
        res = self.session.get(url)
        vf_code = res.text

        url2 = 'http://idea521.com/idea'
        data = {"key": vf_code}
        res1 = self.session.post(url2, json=data)
        if case == 1:
            return res1.json()['activationCode1']
        if case == 2:
            return res1.json()['activationCode2']


if __name__ == '__main__':
    Main().get_B(1)
