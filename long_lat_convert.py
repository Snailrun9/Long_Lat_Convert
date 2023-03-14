import gps_radar_api
import csv
#import viewer
from datetime import datetime
import data_save
from gps_radar_viewer import *
filename_gps0='D:\\File\\Radar\\20230310\\GPS\\GPS_来向90\\1-90-LAI-1-2023-03-10-14-16-15-RTK1-data.csv'
filename_gps1='D:\\File\\Radar\\20230310\\GPS\\GPS_来向90\\1-90-LAI-1-2023-03-10-14-16-15-RTK2-data.csv'
#filename_radar='D:\\File\\Radar\\20230310\\GPS\\GPS_来向70\\1-70-LAI-1-2023-03-10-14-15-00-RTK2-data.csv'

# (gps_speed0,gps_BJtime0)=gps_radar_api.gps_speed_convert(filename_gps0)
(gps_speed1,gps_BJtime1)=gps_radar_api.gps_speed_convert(filename_gps1)
# (gps_speed,gps_BJtime)=gps_radar_api.radar_speed_convert(filename_gps0)
#gps_radar_viewer(gps_speed0,gps_speed1,gps_BJtime1)

(rng_delt,BJ_time0,BJ_time1)=gps_radar_api.gps_range_delt(filename_gps0,filename_gps1)


data_save.data_save(gps_BJtime1[:165],rng_delt[:165],gps_speed1[:165])#注意截取的长度要一致

#viewer.viewer(BJtime,speed)
