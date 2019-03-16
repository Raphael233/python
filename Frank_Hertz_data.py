# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.interpolate import spline

#导入csv数据
csv = pd.read_csv('fh.csv',names=['x','y'])

#转换文本数据为int64
csv.apply(type).value_counts()

fig = plt.figure()

#绘制数据点，点宽为3
#plt.scatter(csv.x, csv.y,s=8,marker='+')

#计算spline
xnew = np.linspace(csv.x.min(),csv.x.max(),1000)
#500 represents number of points to make between T.min and T.max 
power_smooth = spline(csv.x,csv.y,xnew)

#绘制plot，线宽为1，标记为5
#plt.plot(xnew,power_smooth,lw=1,ms=5)


#寻找极值点
y = power_smooth
y_max = y[signal.argrelextrema(y, np.greater)]
y_min = y[signal.argrelextrema(-y, np.greater)]
x_min = [xnew[int(np.argwhere(y==y_min[i]))] for i in range(0,6)]
x_max = [xnew[int(np.argwhere(y==y_max[i]))] for i in range(0,7)]
#plt.scatter(x_max,y_max,marker='*',s=20)
#plt.scatter(x_min,y_min,marker='+',s=20)


#写入csv文件
'''data_set = list(zip(x_min,y_min,x_max,y_max))
df = pd.DataFrame(data = data_set)
df.to_csv(path_or_buf='C:/Users/acer/Desktop/9_18_fh/baoluoxian.csv',sep=',')'''



#拟合包络线
z = np.polyfit(x_min, y_min, 3)
f = np.poly1d(z)
#print(z,f)
plt.scatter(x_max,y_max/2,marker='*',s=20)
plt.scatter(x_min,np.array([0.02,0.02,0.02,0.02,0.02,0.02]),marker='+',s=20)
plt.plot(xnew,y-f(xnew))



#plt.title('U随I变化曲线',fontsize=16)

#导出图片设置精度
#plt.savefig('1.png',dpi=500)
#plt.savefig('2.png',dpi=500)
plt.savefig('3.png',dpi=500)
plt.show()
