import time

import operate
import search

# TODO 教务系统sessionID（浏览器F12获取）
Cookie = 'JSESSIONID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# 选公选课
def gongxuan():
    # 1.查询课程ID
    course_name = input("请输入课程名称：")
    search.gongxuan(Cookie, course_name)
    course_id = input("请输入课程ID：")
    # 2.选课
    while True:
        success = operate.ggxxkxkOper(Cookie, course_id)
        if success:
            break
        else:
            time.sleep(60)


# 选专业课
def zhuanye():
    # 1.查询课程ID
    course_name = input("请输入课程名称：")
    search.zhuanye(Cookie, course_name)
    course_id = input("请输入课程ID：")
    # 2.选课
    while True:
        success = operate.bxqjhxkOper(Cookie, course_id)
        if success:
            break
        else:
            time.sleep(60)


# 退课
def tuike():
    course_id = input("请输入课程ID：")
    operate.xstkOper(Cookie, course_id)


if __name__ == '__main__':
    # TODO 自行调用
    gongxuan()
    tuike()
