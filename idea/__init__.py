name = "puffidea"

from idea import get_code as c
import pyperclip
import signal


class InputTimeoutError(Exception):
    pass


def interrupted(signum, frame):
    raise InputTimeoutError


def set_clipboard(s):
    pyperclip.copy(s)


def main():
    input("获取激活码会覆盖当前剪贴板, 按回车键开始获取~")

    # 先获取A的
    A = c.Main().get_A()
    if A != "" and A is not None:
        set_clipboard(A)
        signal.signal(signal.SIGALRM, interrupted)
        signal.alarm(15)
        try:
            input('已赋值到剪贴板, 若本激活码不可用, 需要换另一个激活码, 回车即可. (15s后自动退出)   [code from: http://idea.94goo.com/key]')
        except InputTimeoutError:
            exit(0)
        signal.alarm(0)
    else:
        print("获取失败, 开始切换获取源重新尝试~")

    # 获取C1的
    print("切换激活码~")
    C = c.Main().get_C(1)
    if C != "" and C is not None:
        set_clipboard(C)
        signal.signal(signal.SIGALRM, interrupted)
        signal.alarm(15)
        try:
            input('已赋值到剪贴板, 若本激活码不可用, 需要换另一个激活码, 回车即可. (15s后自动退出)   [code from: http://idea521.com/]')
        except InputTimeoutError:
            exit(0)
        signal.alarm(0)
    else:
        print("获取失败, 开始切换获取源重新尝试~")

    # 获取C2的
    print("切换激活码~")
    C = c.Main().get_C(2)
    if C != "" and C is not None:
        set_clipboard(C)
        signal.signal(signal.SIGALRM, interrupted)
        signal.alarm(15)
        try:
            input('已赋值到剪贴板, 若本激活码不可用, 需要换另一个激活码, 回车即可. (15s后自动退出)   [code from: http://idea521.com/]')
        except InputTimeoutError:
            exit(0)
        signal.alarm(0)

    # 获取B的
    print("暂时没有更多通用的啦~ 请问是否需要尝试指定软件的激活码, 回复数字开始获取.\n1、IDEA\n2、Pycharm\n3、GoLand\n")
    i = input("请输入(回车退出本程序):")
    if i == "":
        print("Bye~")
        exit()

    if i == "3":
        B = c.Main().get_B(4)
    else:
        B = c.Main().get_B(int(i))

    if B != "" and B is not None:
        set_clipboard(B)
        print('已赋值到剪贴板～ [code from: http://idea.javatiku.cn/]')
        print("已经尽我所能, 如有新的地址, 可以去github下留言[https://github.com/puffhub/puffidea], 欢迎Star.. Bye~")
        exit()


if __name__ == '__main__':
    main()
