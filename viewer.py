# coding:utf8
 
# import matplotlib.pyplot as plt
# import numpy as np
# def viewer(num,speed):
#     x_axis_data = num #x
#     y_axis_data = speed

#     #for x, y in zip(x_axis_data, y_axis_data):
#         #plt.text(x, y+0.3, '%.00f' % y, ha='center', va='bottom', fontsize=7.5)#y_axis_data1加标签数据
#     plt.plot(x_axis_data, y_axis_data)#'bo-'表示蓝色实线，数据点实心原点标注
#     ## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，
#     plt.scatter(x_axis_data,  # 横坐标
#             y_axis_data,  # 纵坐标
#             c='red',  # 点的颜色
#             label='function')  # 标签 即为点代表的意思

#     plt.legend()  #显示上面的label
#     plt.xlabel('time_s') #x_label
#     plt.ylabel('speed_km/h')#y_label
    
#     plt.ylim(20,100)#仅设置y轴坐标范围
#     plt.xlim(19425.601,19425.603)
#     plt.show()
 
# #https://blog.csdn.net/qq_49641239/article/details/118784767





# import matplotlib.pyplot as plt
# import matplotlib.dates as md
# from matplotlib.dates import SECONDLY
# from matplotlib.dates import AutoDateLocator
# import pandas as pd
# import numpy as np
# import long_lat_convert
# from matplotlib.dates import DateFormatter




# def time_ticks(x, pos):
#     # 在 pandas 中，按 10min 生成的时间序列与 matplotlib 要求的类型不一致
#     # 需要转换成 matplotlib 支持的类型
#     x = md.num2date(x)
    
#     # 时间坐标是从坐标原点到结束一个一个标出的
#     # 如果是坐标原点的那个刻度则用下面的要求标出刻度
#     if pos == 0:
#         # %Y-%m-%d
#         # 时间格式化的标准是按 2020-10-01 10:10:10.0000 标记的
#         fmt = '%Y-%m-%d %H:%M:%S.%f'
#     # 如果不是是坐标原点的那个刻度则用下面的要求标出刻度
#     else:
#         # 时间格式化的标准是按 10:10:10.0000 标记的
#         fmt = '%H:%M:%S.%f'
#     # 根据 fmt 的要求画时间刻度
#     label = x.strftime(fmt)
    
#     # 当 fmt 有%s时需要下面的代码
#     label = label.rstrip("0")
#     label = label.rstrip(".")
    
#     # 截断了秒后面的 .000
#     return label
# #通过 figsize 调整图表的长宽比例，使得坐标轴上的刻度不至于太挤
# fig = plt.figure(figsize=(19, 7))
# ax = fig.add_subplot()
# n=len(long_lat_convert.BJtime)
# # 给定的日期格式可以有多种 20201001   2020-10-01  2020/10/01
# # start_time_string = long_lat_convert.BJtime[0]
# # end_time_string = long_lat_convert.BJtime[n-11]
# x=long_lat_convert.BJtime




# # 根据日期生成时间轴
# # freq 用来指明以多大间隔划分整个时间区间
# # 10T/10min 按 10 分钟划分，同理其他常见的时间跨度有
# # W 周、D 天（默认值）、H 小时、S 秒、L/ms 毫秒、U/us 微秒、N 纳秒
# # 其他具体的详见 https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
# #x = pd.date_range(start=start_time_string, end=end_time_string, freq="0.1S")

# #  二维上的点是相互对应的，根据 x 的个数随机生成 y 
# y = long_lat_convert.speed

# # x, y 按离散的关系添加在图中
# ax.plot(x, y)


# # 自定义时间刻度如何显示


# # 根据自己定义的方式去画时间刻度
# formatter =DateFormatter("%H:%M:%S.%f")


# # 在图中应用自定义的时间刻度
# ax.xaxis.set_major_formatter(formatter)

# # minticks 需要指出，值的大小决定了图是否能按 10min 为单位显示
# # 值越小可能只能按小时间隔显示
# locator = AutoDateLocator(minticks=10)
# # pandas 只生成了满足 10min 的 x 的值，而指定坐标轴以多少的时间间隔画的是下面的这行代码
# # 如果是小时，需要在上面导入相应的东东 YEARLY, MONTHLY, DAILY, HOURLY, MINUTELY, SECONDLY, MICROSECONDLY
# # 并按照下面的格式照葫芦画瓢
# locator.intervald[SECONDLY] = [0.1]  # 10min 为间隔
# ax.xaxis.set_major_locator(locator=locator)

# # 旋转刻度坐标的字符，使得字符之间不要太拥挤
# fig.autofmt_xdate()
# plt.show()
# #https://developer.aliyun.com/article/775721





import datetime
import matplotlib.pyplot as plt
#导入中文字体，避免显示乱码
import pylab as mpl
import numpy as np
import long_lat_convert
from datetime import datetime
 
 
    #数据源
list_count = long_lat_convert.speed
    #中文乱码问题
mpl.rcParams['font.sans-serif'] = ['SimHei']
 
    # 生成figure对象,相当于准备一个画板
fig = plt.figure(figsize=(21, 7))
 
    # 生成axis对象，相当于在画板上准备一张白纸，111，11表示只有一个表格，
    #第3个1，表示在第1个表格上画图
ax = fig.add_subplot(111)
 

plt.xlabel('时间')
 
plt.ylabel('speed')
 
    #将字符串的日期，转换成日期对象
xs =long_lat_convert.BJtime 
    #日期对象作为参数设置到横坐标,并且使用list_date中的字符串日志作为对象的标签（别名）
    #x坐标的刻度值
ar_xticks = np.arange(1, len(long_lat_convert.BJtime )+1, step=1)
x_data=[]
for i in xs:
    data_format=i.strftime('%H:%M:%S.%f')
    x_data.append(data_format)

#时间格式

#xticks是显示的核心
plt.xticks(ar_xticks, x_data, rotation=45, fontsize=10)
plt.yticks(np.arange(0, 100, step=2), fontsize=10)
ax.plot(ar_xticks, list_count, color='r')

 
    #下方图片显示不完整的问题
plt.tight_layout()
 
    #在点阵上方标明数值
for x, y in zip(ar_xticks, list_count):
       plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10)
fig.autofmt_xdate()
plt.show()



#

# 自定义时间刻度如何显示
# def time_ticks(x, pos):
#     # 在 pandas 中，按 10min 生成的时间序列与 matplotlib 要求的类型不一致
#     # 需要转换成 matplotlib 支持的类型
#     #x = md.num2date(x)
    
#     # 时间坐标是从坐标原点到结束一个一个标出的
#     # 如果是坐标原点的那个刻度则用下面的要求标出刻度
#     if pos == 0:
#         # %Y-%m-%d
#         # 时间格式化的标准是按 2020-10-01 10:10:10.0000 标记的
#         fmt = '%Y-%m-%d %H:%M:%S.%f'
#     # 如果不是是坐标原点的那个刻度则用下面的要求标出刻度
#     else:
#         # 时间格式化的标准是按 10:10:10.0000 标记的
#         fmt = '%H:%M:%S.%f'
#     # 根据 fmt 的要求画时间刻度
#     label = x.strftime(fmt)
    
#     # 当 fmt 有%s时需要下面的代码
#     label = label.rstrip("0")
#     label = label.rstrip(".")
    
#     # 截断了秒后面的 .000
#     return label

# # 根据自己定义的方式去画时间刻度
# formatter = plt.FuncFormatter(time_ticks)

# # 在图中应用自定义的时间刻度
# ax.xaxis.set_major_formatter(formatter)

# # minticks 需要指出，值的大小决定了图是否能按 10min 为单位显示
# # 值越小可能只能按小时间隔显示
# locator = AutoDateLocator(minticks=20)
# # pandas 只生成了满足 10min 的 x 的值，而指定坐标轴以多少的时间间隔画的是下面的这行代码
# # 如果是小时，需要在上面导入相应的东东 YEARLY, MONTHLY, DAILY, HOURLY, MINUTELY, SECONDLY, MICROSECONDLY
# # 并按照下面的格式照葫芦画瓢
# locator.intervald[ MICROSECONDLY] = [100]  # 10min 为间隔
# ax.xaxis.set_major_locator(locator=locator)

# # 旋转刻度坐标的字符，使得字符之间不要太拥挤
# fig.autofmt_xdate()
#plt.show()