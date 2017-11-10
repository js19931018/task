from numpy import *
from logpaint import getresult


import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d  import Axes3D

arr=[]

mpl.rcParams['font.size'] = 10

fig=plt.figure()

ax=fig.add_subplot(111,projection='3d')
lgd=[]

prearr=getresult()

print arr

for i in range(88):
     if i==0 or i==22 or i==44 or i==66:
        prov=prearr.popitem()
        arr.append(prov[1])
        lgd.append(prov[0])
     else:
        arr.append([0 for i in range(88)])
        lgd.append('')
print 'arr', arr
xs=range(len(arr))

ys=range(len(arr[0]))

for z in range(len(arr)):

    xs=range(len(arr))

    ys=arr[z]
    print ys


    color=plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))

    ax.bar(xs,ys,zs=z,zdir='y',color=color,alpha=0.5,)

    ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))

    ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))

ax.legend(['one','two','three','','five'])

ax.set_xlabel('date')

ax.set_ylabel('province')

ax.set_zlabel('visits')

plt.show()