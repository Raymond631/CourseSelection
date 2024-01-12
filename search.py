import sys

import requests


# 选修选课-本学期计划选课（查询）
def zhuanye(Cookie, course_name):
    # query参数：sfym过滤已满、sfct过滤冲突
    url = f"http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/xsxkBxqjhxk?kcxx=&skls=&skxq=&skjc=&sfym=false&sfct=true"
    payload = {
        'iDisplayStart': 0,
        'iDisplayLength': 50
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': f'{Cookie}',
        'Host': 'csujwc.its.csu.edu.cn',
        'Origin': 'http://csujwc.its.csu.edu.cn',
        'Referer': 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()['aaData']
        for course in data:
            if course_name in course['kcmc']:
                print(f"时间：{course['sksj']}，地点：{course['skdd']}，课程号：{course['jx0404id']}，老师：{course['skls']}，课程名：{course['kcmc']}，余量：{course['syrs']}")
    else:
        print(f"API异常:\n{response.text}")
        sys.exit()


# 选修选课-公共选修课选课（查询）
def gongxuan(Cookie, course_name):
    # query参数：szjylb公选类别（1-5或不填）、szjylb过滤已满、szjylb过滤冲突
    url = f"http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/xsxkGgxxkxk?kcxx=&skls=&skxq=&skjc=&sfym=false&sfct=true&szjylb="
    payload = {
        'iDisplayStart': 0,
        'iDisplayLength': 500
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': f'{Cookie}',
        'Host': 'csujwc.its.csu.edu.cn',
        'Origin': 'http://csujwc.its.csu.edu.cn',
        'Referer': 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()['aaData']
        for course in data:
            if course_name in course['kcmc']:
                print(f"时间：{course['sksj']}，地点：{course['skdd']}，课程号：{course['jx0404id']}，老师：{course['skls']}，课程名：{course['kcmc']}，余量：{course['syrs']}")
    else:
        print(f"API异常:\n{response.text}")
        sys.exit()
