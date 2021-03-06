# @Time    : 2020/3/29 14:30
# @Author  : LavÖz
# @File    : 京东.py
# @Software: PyCharm
import random

import frida, sys

with open("./index.js", "r", encoding="utf8") as f:
    jscode = f.read()


def message(message, data):
    if message["type"] == "send":
        try:
            print("[*]", message["payload"])
        except:
            print("============")

            print(message)
            print("============")

    else:
        print(message)


if __name__ == '__main__':
    # 先打开app进程
    process = frida.get_remote_device().attach("com.taobao.taobao")
    script = process.create_script(jscode)
    script.on("message", message)
    script.load()
    sys.stdin.read()
