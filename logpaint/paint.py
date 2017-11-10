#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from logpaint import *
r=getresult()
font = FontProperties(fname=r"simsun.ttc", size=14)
def showresult(city):

    plt.plot(r[city])
    plt.title(u'App DianmiHR365 visit statistic')
    plt.ylabel('visit number')
    plt.xlabel('days from 2015-7-01 to 2015-9-30')
    plt.show()

if __name__ == '__main__':
    showresult('浙江省')