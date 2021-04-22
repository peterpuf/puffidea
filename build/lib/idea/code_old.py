# coding=utf-8

import requests
import re
import zipfile
import tempfile
import sys


class Main(object):
    def __init__(self):
        self.session = requests.session()

    def get_zip(self):
        """
        下载激活码文件,
        :return:
        """
        url = 'http://idea.medeming.com/jets/'
        res = self.session.get(url)
        if sys.version.split(".")[0] == "3":
            res.encoding = 'utf-8'
        if res.status_code == 200:
            d_url = "http://idea.medeming.com/jets/" + re.findall('<a href="(\S+)".*?="激活码.zip">点击下', res.text)[0]
            d_res = requests.get(d_url)
            return d_res
        else:
            print("请求失败, res: " + res.text)
            return None

    def parse_zip(self):
        zip_res = self.get_zip()
        rets = {"2017": "", "2018": ""}
        # 临时文件保存zip, 这样当上下文关闭时文件会自动删除
        with tempfile.TemporaryFile() as tmp_file:
            tmp_file.write(zip_res.content)

            # 使用zipfile打开这个临时文件
            s = zipfile.ZipFile(tmp_file)

            # 遍历文件列表, 通过当前zip对象读取每一项内容
            for each in s.namelist():
                if not str(each).endswith(".txt"):
                    continue

                with s.open(each, 'r') as code:
                    x = code.read()
                    if str(each).startswith("2018"):
                        rets['2018'] = bytes.decode(x)
                    else:
                        rets['2017'] = bytes.decode(x)

        return rets

    def run(self):
        return self.parse_zip()

    def get_from_new(self):
        url = "http://idea.94goo.com/key"
        res = self.session.get(url)
        return re.findall('class="new-key" value="(.*?)">', res.text)[0]


if __name__ == '__main__':
    # import argparse
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-n', help="2018版之后的激活码", action="store_true")
    # parser.add_argument('-o', help="2017年之前的激活码", action="store_true")
    # parser.add_argument('-x', help="最新的激活码", action="store_true")
    # args = parser.parse_args()
    # ret = Main().run()
    # if args.n:
    #     print(ret['2018'])
    #     exit()
    # if args.o:
    #     print(ret['2017'])
    #     exit()
    # if args.x:
    #     print(Main().get_from_new())
    #     exit()
    # print(ret['2018'])
    print("该地址已废弃, 请尝试使用其他方式获取")
