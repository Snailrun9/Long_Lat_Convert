# -*- coding:utf-8-*-
import gps_radar_api
import csv
#import viewer
from datetime import datetime
import data_save
from gps_radar_viewer import *
filename_gps0=r'D:/File/Radar/20230310/GPS/GPS_来向90/1-90-LAI-1-2023-03-10-14-16-15-RTK1-data.csv'
filename_gps1=r'D:/File/Radar/20230310/GPS/GPS_来向90/1-90-LAI-1-2023-03-10-14-16-15-RTK2-data.csv'
print (gps_radar_api.data_convert(0,0,0,1))
#filename_radar='D:\\File\\Radar\\20230310\\GPS\\GPS_来向70\\1-70-LAI-1-2023-03-10-14-15-00-RTK2-data.csv'

# (gps_speed0,gps_BJtime0)=gps_radar_api.gps_speed_convert(filename_gps0)
(gps_speed1,gps_BJtime1)=gps_radar_api.gps_speed_convert(filename_gps1)
# (gps_speed,gps_BJtime)=gps_radar_api.radar_speed_convert(filename_gps0)
#gps_radar_viewer(gps_speed0,gps_speed1,gps_BJtime1)

(rng_delt,BJ_time0,BJ_time1)=gps_radar_api.gps_range_delt(filename_gps0,filename_gps1)


#保证文件长度一致
time_num = len(BJ_time1)
rng_num = len(rng_delt)
speed_num = len(gps_speed1)
if time_num >= rng_num:
    if speed_num >=rng_num:
        num = rng_num
    else:
        num = speed_num
else:
    if speed_num >=time_num:
        num =time_num
    else:
        num = speed_num
        
        


data_save.data_save(BJ_time1[:num],rng_delt[:num],gps_speed1[:num])#注意截取的长度要一致

#viewer.viewer(BJtime,speed)
