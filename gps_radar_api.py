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
#https://www.osgeo.cn/geopy/#geopy.distance.Distance

def geodistance(lat1,lng1,lat2,lng2):
#lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]) # 经纬度转换成弧度
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance=2*asin(sqrt(a))*6371000*1000 # 地球平均半径，6371km
    distance=round(distance/1000,3)
    return distance

import math
from math import radians,cos,sin,asin,sqrt,pi,atan,tan,atan2
#这个算法和 geographiclib 算的几乎一样，相差<0.2米
def distVincenty(lat1,lon1,lat2,lon2):
    '精度更高的椭球计算,计算两个 WGS84 经纬度点的距离'
    a=6378137.0       #vincentyConstantA(WGS84) ##单位:米
    b=6356752.3142451 #vincentyConstantB(WGS84) ##单位:米
    f=1/298.257223563 #vincentyConstantF(WGS84)
    L = math.radians(lon2 - lon1)
    U1 = math.atan((1 - f) *math.tan(math.radians(lat1)))
    U2 = math.atan((1 - f) *math.tan(math.radians(lat2)))
    sinU1 =math.sin(U1)
    cosU1 =math.cos(U1)
    sinU2 =math.sin(U2)
    cosU2 =math.cos(U2)
    lambda1 = L
    lambdaP = 2 * math.pi
    iterLimit = 20

    sinLambda = 0.0
    cosLambda = 0.0
    sinSigma = 0.0
    cosSigma = 0.0
    sigma = 0.0
    alpha = 0.0
    cosSqAlpha = 0.0
    cos2SigmaM = 0.0
    C = 0.0
    while (abs(lambda1 - lambdaP) > 1e-12 and --iterLimit > 0) :
        sinLambda =math.sin(lambda1)
        cosLambda =math.cos(lambda1)
        sinSigma = math.sqrt((cosU2 * sinLambda) * (cosU2 * sinLambda) + (cosU1 * sinU2 - sinU1 * cosU2 * cosLambda) * (cosU1 * sinU2 - sinU1 * cosU2 * cosLambda))
        if (sinSigma == 0) :
            return 0
        cosSigma = sinU1 * sinU2 + cosU1 * cosU2 * cosLambda
        sigma = math.atan2(sinSigma, cosSigma)
        alpha = math.asin(cosU1 * cosU2 * sinLambda / sinSigma)
        cosSqAlpha = math.cos(alpha) * math.cos(alpha)
        cos2SigmaM = cosSigma - 2 * sinU1 * sinU2 / cosSqAlpha
        C = f / 16 * cosSqAlpha * (4 + f * (4 - 3 * cosSqAlpha))
        lambdaP = lambda1
        lambda1 = L + (1 - C) * f * math.sin(alpha)* (sigma + C * sinSigma * (cos2SigmaM + C * cosSigma * (-1 + 2 * cos2SigmaM * cos2SigmaM)))

    if iterLimit == 0 :
        return 0.0

    uSq = cosSqAlpha * (a * a - b * b) / (b * b)
    A = 1 + uSq / 16384 * (4096 + uSq * (-768 + uSq * (320 - 175 * uSq)))
    B = uSq / 1024 * (256 + uSq * (-128 + uSq * (74 - 47 * uSq)))
    deltaSigma = B * sinSigma * (cos2SigmaM + B / 4 * (cosSigma * (-1 + 2 * cos2SigmaM * cos2SigmaM) - B / 6 * cos2SigmaM * (-3 + 4 * sinSigma * sinSigma) * (-3 + 4 * cos2SigmaM * cos2SigmaM)))
    s = b * A * (sigma - deltaSigma)
    d = s  ##单位:米
    return d


#gps时间转换为北京时间
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


#计算速度
def gps_speed_convert(filename):
    i=0
    j=0
    BJtime=[]
    speed=[]
    #数组有多少个就要初始化多少
    # lat_1=[0]*2 
    # long_1=[0]*2
    lat=[0]*2   #初始化
    long=[0]*2
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        header =next(csv_reader)
        for row in csv_reader:
            lat[i]=float(row[7])
            long[i]=float(row[8])
            gps_week=int(row[2])
            gps_seconds=float(row[3])
            utc_time=gps_week_seconds_to_utc(gps_week,gps_seconds,18)#转UTC时间
            BJ_time=utc_to_local(utc_time)#UTC转北京时间

            #求总距离
            # lat_1[k]=float(row[7])
            # long_1[k]=float(row[8])
            # if k==1:
            #     k=0
            # k+=1
            # rng=data_convert(lat_1[0],long_1[0],lat_1[1],long_1[1])
           
            #间隔距离；当然也可以相加，但是这样不准确
            if i==1:                        #保证初次数据不进行比较
                rng_interval=data_convert(lat[0],long[0],lat[1],long[1])

                #几种数据计算方式对比
                #rng_interval1=distVincenty(lat[0],long[0],lat[1],long[1])
                # print('rng_interval:',rng_interval)
                # print('rng_interval1:',rng_interval1)
                
                j+=0.1                      #设置间隔
                i=0                         #保持数据更新
                if j==0.1:                  #时间间隔
                    speed.append(rng_interval/0.1*3.6)
                    BJtime.append(BJ_time)
                    j=0
                lat[0]=lat[1]               #数据替换，保持两两做差
                long[0]=long[1]
            i+=1
    return speed,BJtime

#计算雷达的速度，方便添加到新的csv文件中
def radar_speed_convert(filename):
    speed=[]
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        header =next(csv_reader)
        for row in csv_reader:
            speed.append(float(row[3])) 
    return speed

#计算两个gps距离差
def gps_range_delt(filename0,filename1):
     rng_delt=[]
     BJtime0=[]
     BJtime1=[]

     with open(filename0) as csvfile0,open(filename1) as csvfile1:
        csv_reader0 = csv.reader(csvfile0)
        header =next(csv_reader0)
        csv_reader1 = csv.reader(csvfile1)
        header =next(csv_reader1)
        for row0 in csv_reader0:
            for row1 in csv_reader1:
                lat0=float(row0[7])
                long0=float(row0[8])
                lat1 =float(row1[7])
                long1=float(row1[8])
                #时间计算
                gps_week0=int(row0[2])
                gps_seconds0=float(row0[3])
                utc_time0=gps_week_seconds_to_utc(gps_week0,gps_seconds0,18)#转UTC时间
                BJ_time0=utc_to_local(utc_time0)#UTC转北京时间

                gps_week1=int(row1[2])
                gps_seconds1=float(row1[3])
                utc_time1=gps_week_seconds_to_utc(gps_week1,gps_seconds1,18)#转UTC时间
                BJ_time1=utc_to_local(utc_time1)#UTC转北京时间

                #距离计算
                rng_delt.append(data_convert(lat0,long0,lat1,long1))
                BJtime0.append(BJ_time0)
                BJtime1.append(BJ_time1)
        return rng_delt,BJtime0,BJtime1
     

#GPS数据提取



