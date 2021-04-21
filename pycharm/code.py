# coding=utf-8

import requests
import re
import zipfile
import tempfile


class Main(object):
    def __init__(self):
        self.session = requests.session()

    def get_zip(self):
        """
        下载激活码文件,
        :return:
        """
        url = "http://idea.medeming.com/a/jihuoma2.zip"
        res = requests.get(url)
        return res

    def parse_zip(self):
        zip_res = self.get_zip()
        rets = {"2019": "", "2018": ""}
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
                    if str(each).startswith("2018.1"):
                        rets['2018'] = bytes.decode(x)
                    elif str(each).startswith("2018.2"):
                        rets['2019'] = bytes.decode(x)

        return rets

    def run(self):
        return self.parse_zip()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="2018.2之后的激活码", action="store_true")
    parser.add_argument('-o', help="2018.1之前的激活码", action="store_true")
    args = parser.parse_args()
    ret = Main().run()
    if args.n:
        print(ret['2018'])
        exit()
    if args.o:
        print(ret['2019'])
        exit()
    print(ret['2019'])
