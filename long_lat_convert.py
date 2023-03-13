# from geopy.distance import geodesic
# #print(geodesic((30.28708,120.12802999999997),(28.7427,115.86572000000001)).m)
# #print(geodesic((31.35675381,118.5325003),(31.35675324,118.5325035)).m)
# rng_interval_m=geodesic((31.35675381,118.5325003),(31.35675324,118.5325035)).m
# rng_interval_km=geodesic((31.35675381,118.5325003),(31.35675324,118.5325035)).km
# print(rng_interval_m)
# speed_m = rng_interval_m/0.1
# print(speed_m)
# speed_km=speed_m*3.6
# print(speed_km)
import gps_can_api
import csv
#import viewer
from datetime import datetime
import data_save
filename='D:\\File\\Radar\\20230310\\GPS\\GPS_来向70\\1-70-LAI-1-2023-03-10-14-15-00-RTK2-data.csv'
i=0
j=0
k=0
n=0
BJtime=[]
speed=[]
#数组有多少个就要初始化多少
lat_1=[0]*2 
long_1=[0]*2
lat=[0]*2   #初始化
long=[0]*2
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    header =next(csv_reader)
    for row in csv_reader:
        lat[i]=float(row[7])#未进行格式转换
        long[i]=float(row[8])
        gps_week=int(row[2])
        gps_seconds=float(row[3])
        utc_time=gps_can_api.gps_week_seconds_to_utc(gps_week,gps_seconds,18)#转UTC时间
        BJ_time=gps_can_api.utc_to_local(utc_time)#UTC转北京时间
        #排查数据异常是在哪一行
        # n+=1
        # print(n)

        #求总距离
        lat_1[k]=float(row[7])#未进行格式转换
        long_1[k]=float(row[8])
        if k==1:
            k=0
        k+=1
        rng=gps_can_api.data_convert(lat_1[0],long_1[0],lat_1[1],long_1[1])
        #print(rng)
        #print(BJ_time)
        #间隔距离；当然也可以相加，但是这样不准确
        if i==1:    #保证初次数据不进行比较
            rng_interval=gps_can_api.data_convert(lat[0],long[0],lat[1],long[1])

            rng_interval1=gps_can_api.distVincenty(lat[0],long[0],lat[1],long[1])
            # rng_interval2=gps_can_api.geodistance(lat[0],long[0],lat[1],long[1])
            # rng_interval3=gps_can_api.distance_range(lat[0],long[0],lat[1],long[1])
            # print('rng_interval:',rng_interval)
            # print('rng_interval1:',rng_interval1)
            # print('rng_interval2:',rng_interval2)
            # print('rng_interval3:',rng_interval3)
            # print('rng_interval:',rng_interval)
            # print('rng_interval1:',rng_interval1)
            
            ins_speed=rng_interval/0.1*3.6
            j+=0.1
            i=0#保持数据更新
            if j==0.5:  #时间间隔
                speed.append(rng_interval/0.1*3.6)
                BJtime.append(BJ_time)
                #print('speed',ins_speed)
                #print(BJ_time)
                # print(ins_speed)
                # print(BJtime)
                j=0
            lat[0]=lat[1]
            long[0]=long[1]
            #print(BJtime)
            #print(speed)
        i+=1


#data_save.data_save(BJtime,speed)
#viewer.viewer(BJtime,speed)

      



