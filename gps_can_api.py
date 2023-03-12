import csv
import math
import pandas as pd

from geographiclib.geodesic import Geodesic
from geopy import distance


#WGS-84坐标系
def data_convert(lat1,long1,lat2,long2):
    coords_1 = (float(lat1), float(long1))
    coords_2 = (float(lat2), float(long2))
    # print(coords_1)
    # print(coords_2)
    r = distance.distance(coords_1, coords_2).m
    return r
#https://blog.csdn.net/weixin_42512684/article/details/115843448

# #直线距离
# from math import sin, asin, cos, radians, fabs, sqrt
 
# EARTH_RADIUS = 6371000  # 地球平均半径，6371km
 
 
# def hav(theta):
#     s = sin(theta / 2)
#     return s * s
 
 
# def get_distance_hav(lat0, lng0, lat1, lng1):
#     """用haversine公式计算球面两点间的距离。"""
#     # 经纬度转换成弧度
#     lat0 = radians(lat0)
#     lat1 = radians(lat1)
#     lng0 = radians(lng0)
#     lng1 = radians(lng1)
 
#     dlng = fabs(lng0 - lng1)
#     dlat = fabs(lat0 - lat1)
#     h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
#     distance = 2 * EARTH_RADIUS * asin(sqrt(h))
#     return distance



# def geodistance(lat1,lng1,lat2,lng2):
# #lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
#     lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]) # 经纬度转换成弧度
#     dlon=lng2-lng1
#     dlat=lat2-lat1
#     a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     distance=2*asin(sqrt(a))*6371000*1000 # 地球平均半径，6371km
#     distance=round(distance/1000,3)
#     return distance



from geopy.distance import geodesic
def distance_range(lat1,lng1,lat2,lng2):
    distance=geodesic((lat1,lng1),(lat2,lng2)).m
    return distance




#import math
#from math import radians,cos,sin,asin,sqrt,pi,atan,tan,atan2
# 这个算法和 geographiclib 算的几乎一样，相差<0.2米
# def distVincenty(lat1,lon1,lat2,lon2):
#     '精度更高的椭球计算,计算两个 WGS84 经纬度点的距离'
#     a=6378137.0       #vincentyConstantA(WGS84) ##单位:米
#     b=6356752.3142451 #vincentyConstantB(WGS84) ##单位:米
#     f=1/298.257223563 #vincentyConstantF(WGS84)
#     L = math.radians(lon2 - lon1)
#     U1 = math.atan((1 - f) *math.tan(math.radians(lat1)))
#     U2 = math.atan((1 - f) *math.tan(math.radians(lat2)))
#     sinU1 =math.sin(U1)
#     cosU1 =math.cos(U1)
#     sinU2 =math.sin(U2)
#     cosU2 =math.cos(U2)
#     lambda1 = L
#     lambdaP = 2 * math.pi
#     iterLimit = 20

#     sinLambda = 0.0
#     cosLambda = 0.0
#     sinSigma = 0.0
#     cosSigma = 0.0
#     sigma = 0.0
#     alpha = 0.0
#     cosSqAlpha = 0.0
#     cos2SigmaM = 0.0
#     C = 0.0
#     while (abs(lambda1 - lambdaP) > 1e-12 and --iterLimit > 0) :
#         sinLambda =math.sin(lambda1)
#         cosLambda =math.cos(lambda1)
#         sinSigma = math.sqrt((cosU2 * sinLambda) * (cosU2 * sinLambda) + (cosU1 * sinU2 - sinU1 * cosU2 * cosLambda) * (cosU1 * sinU2 - sinU1 * cosU2 * cosLambda))
#         if (sinSigma == 0) :
#             return 0
#         cosSigma = sinU1 * sinU2 + cosU1 * cosU2 * cosLambda
#         sigma = math.atan2(sinSigma, cosSigma)
#         alpha = math.asin(cosU1 * cosU2 * sinLambda / sinSigma)
#         cosSqAlpha = math.cos(alpha) * math.cos(alpha)
#         cos2SigmaM = cosSigma - 2 * sinU1 * sinU2 / cosSqAlpha
#         C = f / 16 * cosSqAlpha * (4 + f * (4 - 3 * cosSqAlpha))
#         lambdaP = lambda1
#         lambda1 = L + (1 - C) * f * math.sin(alpha)* (sigma + C * sinSigma * (cos2SigmaM + C * cosSigma * (-1 + 2 * cos2SigmaM * cos2SigmaM)))

#     if iterLimit == 0 :
#         return 0.0

#     uSq = cosSqAlpha * (a * a - b * b) / (b * b)
#     A = 1 + uSq / 16384 * (4096 + uSq * (-768 + uSq * (320 - 175 * uSq)))
#     B = uSq / 1024 * (256 + uSq * (-128 + uSq * (74 - 47 * uSq)))
#     deltaSigma = B * sinSigma * (cos2SigmaM + B / 4 * (cosSigma * (-1 + 2 * cos2SigmaM * cos2SigmaM) - B / 6 * cos2SigmaM * (-3 + 4 * sinSigma * sinSigma) * (-3 + 4 * cos2SigmaM * cos2SigmaM)))
#     s = b * A * (sigma - deltaSigma)
#     d = s  ##单位:米
#     return d






#     #以M为单位显示
#     # print(geopy.distance.geodesic(coords_1, coords_2).m)
#     #以KM为单位显示
#     # print(geopy.distance.geodesic(coords_1, coords_2).km)


# def get_gps_start_time(file_name):
#     f = open(file_name,'r')
#     for i in range(5):
#         line = f.readline()
#     start_time = line[12:]
#     i = 0
#     while True:
#         if start_time[i] == ',':
#             start_time = float(start_time[0:i]) * 1000
#             break
#         else:
#             i += 1
#     f.close()
#     return start_time





# def get_csv_rowdata(filename,i):
#     with open(filename, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         row_i = [row[i] for row in reader]
#     row_list = []
#     for i in range(len(row_i)):
#         try:
#             row_list.append(float(row_i[i]))
#         except:
#             pass
#     return row_list

# def millerToXY(lon, lat):

#     """
#     经纬度转换为平面坐标系中的x,y 利用米勒坐标系
#     :param xy_coordinate:
#     :param lon: 经度
#     :param lat: 维度
#     :return:
#     """
#     L = 6381372 * math.pi * 2
#     W = L
#     H = L / 2
#     mill = 2.3
#     x = lon * math.pi / 180
#     y = lat * math.pi / 180
#     y = 1.25 * math.log(math.tan(0.25 * math.pi + 0.4 * y))
#     x = (W / 2) + (W / (2 * math.pi)) * x
#     y = (H / 2) - (H / (2 * mill)) * y
#     return [x,y]


# def get_gps_origin(file_name):
#     f = open(file_name,'r')

#     for i in range(5):
#         line = f.readline()

#     i = 0
#     star_idx = 0
#     stop_idx = 0
#     while True:
#         if line[i] == ',':
#             i += 1
#             if i == 6:
#                 star_idx = i+1
#             if i == 7:
#                 stop_idx = i

#             break

#     f.close()
#     return 0


# # origin = [31.3572173616,118.5302960871]
# origin = [31.3560760599,118.5365480273]  #[lat,lon]



# def get_gps_tar_list(file_name):
#     gps_tar_list = []
#     gps_frame = get_csv_rowdata(file_name, 0)
#     gps_t = get_csv_rowdata(file_name, 3)
#     gps_lat = get_csv_rowdata(file_name, 7)
#     gps_lon = get_csv_rowdata(file_name, 8)
#     gps_vx = get_csv_rowdata(file_name, 10)
#     gps_vy = get_csv_rowdata(file_name, 11)

#     for i in range(len(gps_t)):
#         # x_0 = origin[0]
#         # y_0 = origin[1]
#         # x = millerToXY(gps_lon[i],gps_lat[i])[0]
#         # y = millerToXY(gps_lon[i],gps_lat[i])[1]
#         # rng = math.sqrt((x - x_0) ** 2 + (y - y_0) ** 2) - 10

#         lat1 = origin[0]
#         long1 = origin[1]
#         lat2 = gps_lat[i]
#         long2 = gps_lon[i]
#         rng = get_gps_range(lat1, long1, lat2, long2) - 6

#         rng = float(format(rng, '.2f'))
#         v = math.sqrt(float(gps_vx[i]) ** 2 + float(gps_vy[i]) ** 2)
#         t = gps_t[i] * 1000
#         frame_t = gps_frame[i]
#         gps_tar_list += [{'t':t,'v':v,'r':rng,'frame':frame_t}]
#     # print(gps_tar_list)
#     return gps_tar_list


# # 车辆数据
# def get_can_tar_list(can_data_name):
#     # can_data_name = filename_no_txt + '-can-data.csv'
#     can_data = pd.read_csv(can_data_name, encoding='gbk')  # 读取csv文件 gbk防止有中文乱码
#     can_data_filiter = pd.DataFrame(can_data)
#     vehicle_speed_frame = can_data_filiter[(can_data_filiter['CanID'] ==168)]
#     data_filiter_speed = pd.DataFrame( vehicle_speed_frame)
#     warning_frame_byte0 = data_filiter_speed['Byte0'].to_list()
#     warning_frame_byte1 = data_filiter_speed['Byte1'].to_list()
#     warning_frame_byte2 = data_filiter_speed['Byte2'].to_list()
#     warning_frame_byte3 = data_filiter_speed['Byte3'].to_list()
#     warning_frame_byte4 = data_filiter_speed['Byte4'].to_list()
#     warning_frame_byte5 = data_filiter_speed['Byte5'].to_list()
#     warning_frame_byte6 = data_filiter_speed['Byte6'].to_list()
#     warning_frame_byte7 = data_filiter_speed['Byte7'].to_list()
#     can_data_time = data_filiter_speed['Time(ms)'].to_list()

#     speed_h = list(map(lambda x: x *256,warning_frame_byte5))
#     speed_l = list(map(lambda x: x , warning_frame_byte6))
#     speed_t = list(map(lambda x: x , can_data_time))

#     real_vehicle_speed=list(map(lambda x,y,t:{'t':t,'v':( x +y)*0.075/3.6},speed_h,speed_l,speed_t))

#     return real_vehicle_speed
# from geopy.distance import geodesic
# from scipy.spatial.distance import cdist

# rng_m=geodesic((31.35675381,118.5325003),(31.35675324,118.5325035)).m
# rng_km=geodesic((31.35675381,118.5325003),(31.35675324,118.5325035)).km




#将GPS时间戳数据批量转化为日期时间
# import numpy as np
# import pandas as pd
# import time
# def gps_time_convert(data):
#     #设置Spyder右侧console区的print输出行列数无限制
#     pd.set_option('display.max_columns', None)
#     pd.set_option('display.max_rows', None)
#     #读取数据储存为结构体类型的数据
#     data=pd.read_excel('C:/Users/Administrator/Desktop/GPS时间.xlsx') #excel文件的路径，命名为GPS时间.xlsx
#     print(data)
#     data.loc[:, 'localminute'] = data['gps_ts'].apply(lambda x :time.localtime(x)) #gps_ts为GPS时间.xlsx的列名，具体见图1
#     #转换的时间格式为"年-月-日 时:分:秒"
#     data.loc[:, 'time'] = data['localminute'].apply(lambda x :time.strftime("%Y-%m-%d %H:%M:%S", x))
#     return data
# #https://blog.csdn.net/qq_38773993/article/details/118931190


from datetime import datetime, timedelta

# 闰秒

# 输入：GPS周、GPS周内秒、闰秒（可选，gps时间不同，闰秒值也不同，由Leap_Second.dat文件决定）
# 输出：UTC时间（格林尼治时间）
# 输入示例： gps_week_seconds_to_utc(2119, 214365.000)
# 输出示例： '2020-08-18 11:32:27.000000'
def gps_week_seconds_to_utc(gpsweek, gpsseconds, leapseconds):
    datetimeformat = "%Y-%m-%d %H:%M:%S.%f"
    epoch = datetime.strptime("1980-01-06 00:00:00.000", datetimeformat)
    # timedelta函数会处理seconds为负数的情况
    elapsed = timedelta(days=(gpsweek*7), seconds=(gpsseconds-leapseconds))
    return datetime.strftime(epoch+elapsed, datetimeformat)
#https://blog.whuzfb.cn/blog/2020/08/19/time_system/


from datetime import datetime, timedelta, timezone

# UTC时间转本地时间（北京）时间
# 1. 把utc的str转为datetime（无时区信息）
# 2. 添加时区信息为utc时区
# 3. datetime转为时间戳
# 4. 从时间戳得到本地时间datetime
# 输入格式为：'2020-08-05 02:03:03.815650'
# 输出格式为：datetime.datetime(2020, 8, 5, 10, 3, 3, 815650)
def utc_to_local(utc_time):
    datetimeformat =  "%Y-%m-%d %H:%M:%S.%f"
    # 得到不包含时区的datetime
    dt_no_tz = datetime.strptime(utc_time, datetimeformat)
    # 设置时区为UTC
    # timezone.utc与timezone(timedelta(hours=0))一样
    utc_datetime = dt_no_tz.replace(tzinfo=timezone(timedelta(hours=0)))
    t = utc_datetime.timestamp()
    # 根据时间戳得到UTC时间
    # datetime.utcfromtimestamp(t)
    # 如果要将时间戳转化为东八区datetime
    # fromtimestamp(timestamp, timezone(timedelta(hours=8)))
    # 根据时间戳得到本地时间fromtimestamp(t, tz=None)
    return  datetime.fromtimestamp(t)

