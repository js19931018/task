# /usr/bin/env python
#  -*- coding: utf-8 -*-
import re


def checksex(ID):
    # 查看性别
    if int(ID[-2]) % 2 == 0:
        return 'female'
    else:
        return 'male'

def checkCity(ID):
    # 地区校验
    ID_add = ID[0:6]
    ID_add1 = ID[0:2] + '0000'
    ID_add2 = ID[0:4] + '00'
    city = {}
    rage = ['198012.tsv', '198112.tsv', '198212.tsv', '198312.tsv', '198412.tsv', '198512.tsv', '198612.tsv','198712.tsv', '198812.tsv', '198912.tsv',
            '199012.tsv', '199112.tsv', '199212.tsv', '199312.tsv', '199412.tsv', '199512.tsv', '199612.tsv','199712.tsv', '199812.tsv', '199912.tsv',
            '200012.tsv', '200112.tsv', '200212.tsv', '200312.tsv', '200412.tsv', '200512.tsv', '200612.tsv','200712.tsv', '200812.tsv', '200912.tsv',
            '201012.tsv', '201112.tsv', '201312.tsv', '201412.tsv', '201512.tsv', '201612.tsv']
    for i in rage:
        with open(i) as f:
            cfile = f.read()
            clst = cfile.split("\n")
            for r in clst:
                if not r == '':
                    l = r.split()
                    city[l[2]] = l[3]
    if ID_add in city:
        check = '发证地区：' + city[ID_add1] + city[ID_add2] + city[ID_add]
    else:
        check = 'region incorrect'
    return check

def checkDate(ID):
    # 出生日期的合法性检查
    if (len(ID) == 15):
        if ((int(ID[6:8]) + 1900) % 4 == 0 or ((int(ID[6:8]) + 1900) % 100 == 0 and (int(ID[6:8]) + 1900) % 4 == 0)):
            ereg = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
        if (re.match(ereg, ID)):
            check = '出生日期:19' + ID[6:8] + '年' + ID[8:10] + '月' + ID[10:12] + '日'
        else:
            check = 'date incorrect'
    elif (len(ID) == 18):
        if (int(ID[6:10]) % 4 == 0 or (int(ID[6:10]) % 100 == 0 and int(ID[6:10]) % 4 == 0)):
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
        if (re.match(ereg, ID)):
            check = '出生日期:' + ID[6:10] + '年' + ID[10:12] + '月' + ID[12:14] + '日'
        else:
            check = 'date incorrect'
    return check

def checkLen(ID):
    #身份证长度校验
    if (len(ID) != 15 or 18):
         check = 'long incorrect'
    return check

def checkByte(ID):
    # 计算校验位
    if (len(ID) == 18):
      ID_list = list(ID)
      S = (int(ID_list[0]) + int(ID_list[10])) * 7 + (int(ID_list[1]) + int(ID_list[11])) * 9 + \
            (int(ID_list[2]) + int(ID_list[12])) * 10 + (int(ID_list[3]) + int(ID_list[13])) * 5 + \
            (int(ID_list[4]) + int(ID_list[14])) * 8 + (int(ID_list[5]) + int(ID_list[15])) * 4 + \
            (int(ID_list[6]) + int(ID_list[16])) * 2 + int(ID_list[7]) * 1 + int(ID_list[8]) * 6 + int(ID_list[9]) * 3
      Y = S % 11
      M = "F"
      JYM = "10X98765432"
      M = JYM[Y]  # 判断校验位
      if (M == ID_list[17]):  # 检测ID的校验位
        check = 'correct'
      else:
        check = 'verify incorrect'
      return check






