"""
这个是按照列写入
"""

import pandas as pd

def data_save(BJtime,speed):


    #a和b的长度必须保持一致，否则报错
    a = BJtime          
    b = speed
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'BJtime':a,'speed':b})

    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"D:\File\test2.csv",sep=',')   #这个地方需要自己先建一个csv文件，然后把路径复制进来，例如 dataframe.to_csv(r"F:\test2.csv",sep=',')

    # https://blog.csdn.net/weixin_43245453/article/details/90054820