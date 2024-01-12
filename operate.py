import sys

import requests


# 本学期计划选课（专业选修）
def bxqjhxkOper(Cookie, id):
    url = f"http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/bxqjhxkOper?jx0404id={id}&xkzy=&trjf="
    headers = {
        'Cookie': f'{Cookie}',
        'Host': 'csujwc.its.csu.edu.cn',
        'Referer': 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if (response.json()['success']):
            print("选课成功！")
            return True
        else:
            print("选课失败...")
            return False
    else:
        print(f"API异常:\n{response.text}")
        sys.exit()


# 公共选修课选课（公选）
def ggxxkxkOper(Cookie, id):
    url = f"http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/ggxxkxkOper?jx0404id={id}&xkzy=&trjf="
    headers = {
        'Cookie': f'{Cookie}',
        'Host': 'csujwc.its.csu.edu.cn',
        'Referer': 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if (response.json()['success']):
            print("选课成功！")
            return True
        else:
            print("选课失败...")
            return False
    else:
        print(f"API异常:\n{response.text}")
        sys.exit()


# 选修退课
def xstkOper(Cookie, id):
    url = f"http://csujwc.its.csu.edu.cn/jsxsd/xsxkjg/xstkOper?jx0404id={id}"
    headers = {
        'Cookie': f'{Cookie}',
        'Host': 'csujwc.its.csu.edu.cn',
        'Referer': 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if (response.json()['success']):
            print("退课成功！")
            return True
        else:
            print("退课失败...")
            return False
    else:
        print(f"API异常:\n{response.text}")
        sys.exit()
