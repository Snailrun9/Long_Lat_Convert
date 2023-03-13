import math
raw_tar_list_0 = {'update_flag': 0,
            'raw_det_num': 0,
            'range': list(range(128)),
            'angle': list(range(128)),
            'speed': list(range(128)),
            'level': list(range(128)),
            'snr': list(range(128)),
            'x': list(range(128)),
            'y': list(range(128)),
            'rad':list(range(128))
            }
tmp_raw_det_num_0 = 0
raw_tar_num_0 = 0

def raw_data(can_data):
    rng = ((can_data[2] & 0xF0) >> 4 | (can_data[1] & 0xFF) << 4) * 0.1#距离
    speed = ((can_data[3] & 0xFF) >> 0 | (can_data[2] & 0x07) << 8) * 0.1 - 102.4
    angle = ((can_data[5] & 0xF0) >> 4 | (can_data[4] & 0x7F) << 4) * 0.1 - 102.4
    level = (can_data[6] & 0xFF) * 0.5 - 64
    snr = can_data[7] & 0xFF
    rad = angle * math.pi / 180+math.pi/2
    x = rng * math.sin(rad)
    y = rng * math.cos(rad)
    rng = float(format(rng, '.2f'))
    angle = float(format(angle, '.2f'))
    speed = float(format(speed, '.2f'))
    level = float(format(level, '.2f'))
    snr = float(format(snr, '.2f'))
    rad = float(format(rad,'.2f'))
    x = float(format(x, '.2f'))
    y = float(format(y, '.2f'))
    return {'range': rng, 'angle': angle, 'speed': speed, 'level': level, 'snr': snr,'x': x ,'y': y,'rad':rad}


def ORG_TAR_MSG(can_id,can_data):
    #声明全局变量
    global tmp_raw_det_num_0,raw_tar_num_0,raw_tar_list_0
    #原始状态信息解析
    if can_id == 0x501:
        tmp_raw_det_num_0 = can_data[0] & 0xFF#发送目标个数
        if raw_tar_num_0 != 0:#这个值是在哪里进行修改的，注意是个全局变量
            #和目标个数值一样，更新标识位为1
            if raw_tar_num_0 == raw_tar_list_0['raw_det_num']:
                raw_tar_list_0['update_flag'] = 1
            else:
                raw_tar_list_0['update_flag'] = -1
            #初始化
            raw_tar_num_0 = 0
    if can_id == 0x503:
        #赋值个数到raw_tar_list_0
        raw_tar_list_0['raw_det_num'] = tmp_raw_det_num_0
        data = raw_data(can_data)
        #raw_tar_num就是把这个数据放到range这个数据当中的多少位，可以同时添加多个元素
        raw_tar_list_0['range'][raw_tar_num_0] = data['range']
        raw_tar_list_0['speed'][raw_tar_num_0] = data['speed']
        raw_tar_list_0['angle'][raw_tar_num_0] = data['angle']
        raw_tar_list_0['level'][raw_tar_num_0] = data['level']
        raw_tar_list_0['snr'][raw_tar_num_0] = data['snr']
        raw_tar_list_0['x'][raw_tar_num_0] = data['x']
        raw_tar_list_0['y'][raw_tar_num_0] = data['y'] 
        raw_tar_list_0['rad'][raw_tar_num_0] = data['rad'] 
        raw_tar_num_0 += 1
        raw_tar_list_0['update_flag'] = 0

#将数据分割为只有num个数据
def data_num(radar_data,radar_data_num):
    num =radar_data_num['raw_det_num']
    radar_data['update_flag']=radar_data_num['update_flag']
    radar_data['raw_det_num']=radar_data_num['raw_det_num']
    radar_data['range']=radar_data_num['range'][:num]
    radar_data['angle']=radar_data_num['angle'][:num]
    radar_data['speed']=radar_data_num['speed'][:num]
    radar_data['level']=radar_data_num['level'][:num]
    radar_data['snr']=radar_data_num['snr'][:num]
    radar_data['x']=radar_data_num['x'][:num]
    radar_data['y']=radar_data_num['y'][:num]
    radar_data['rad']=radar_data_num['rad'][:num]
    return radar_data





