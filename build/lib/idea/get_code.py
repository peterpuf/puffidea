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

    def get_D(self):
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'Origin': 'https://www.ajihuo.com',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.ajihuo.com/pycharm/4197.html',
            'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
        }

        data = {
            'secret_key': '199992',
            'Submit': '\u9605\u8BFB\u5168\u6587',
        }

        response = self.session.post('https://www.ajihuo.com/pycharm/4197.html', headers=headers, data=data)
        return re.findall("<blockquote><p>(.*?)</p>", response.text)[0]

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
