# /usr/bin/env python
#  -*- coding: utf-8 -*-
import re
import pickle


# 查看性别
def checksex(self):
    if len(self) == 18:
        if int(self[-2]) % 2 == 0:
            check = 'female'
        else:
            check = 'male'
    elif len(self) == 15:
        if int(self[-1]) % 2 == 0:
            check = 'female'
        else:
            check = 'male'
    else:
        check = 'sexerr'
    return check


# 地区校验
def checkcity(self):
    id_add = self[0:6]
    id_add1 = self[0:2] + '0000'
    id_add2 = self[0:4] + '00'
    pickle_file = open('cityid_data.pkl', 'rb')
    city = pickle.load(pickle_file)
    if id_add in city:
        check = '发证地区：' + city[id_add1] + city[id_add2] + city[id_add]
    else:
        check = '身份证地区非法'
    return check


# 出生日期以及字符的合法性校验
def checkdate(self):  # 出生日期以及字符的合法性校验
    if len(self) == 15:
        if (int(self[6:8]) + 1900) % 4 == 0 or \
                ((int(self[6:8]) + 1900) % 100 == 0 and (int(self[6:8]) + 1900) % 4 == 0):
            ereg = re.compile(
                '[1-9][0-9]{5}[0-9]{2}\
((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)\
(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}[0-9]{2}\
((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)\
(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
        if re.match(ereg, self):
            check = '出生日期:19' + self[6:8] + '年' + self[8:10] + '月' + self[10:12] + '日'
        else:
            check = 'illegal str'
        return check
    elif len(self) == 18:
        if int(self[6:10]) % 4 == 0 or (int(self[6:10]) % 100 == 0 and int(self[6:10]) % 4 == 0):
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})\
((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)\
(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})\
((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)\
(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
        if re.match(ereg, self):
            check = '出生日期:' + self[6:10] + '年' + self[10:12] + '月' + self[12:14] + '日'
        else:
            check = 'illegal str'
        return check
    else:
        check = 'date incorrect'
        return check


# 身份证长度校验
def checklen(self):
    if len(self) == 15 or 18:
        check = 'long correct'
    else:
        check = 'long incorrect'
    return check


# 计算校验位
def checkbyte(self):
    if len(self) == 18:
        id_list = list(self)
        s = (int(id_list[0]) + int(id_list[10])) * 7 + (int(id_list[1]) + int(id_list[11])) * 9 + \
            (int(id_list[2]) + int(id_list[12])) * 10 + (int(id_list[3]) + int(id_list[13])) * 5 + \
            (int(id_list[4]) + int(id_list[14])) * 8 + (int(id_list[5]) + int(id_list[15])) * 4 + \
            (int(id_list[6]) + int(id_list[16])) * 2 + int(id_list[7]) * 1 + int(id_list[8]) * 6 + int(id_list[9]) * 3
        y = s % 11
        # m = "F"
        jym = "10X98765432"
        m = jym[y]  # 判断校验位
        if m == id_list[17]:  # 检测ID的校验位
            check = 'verify correct'
        else:
            check = 'verify incorrect'
        return check
    else:
        pass
