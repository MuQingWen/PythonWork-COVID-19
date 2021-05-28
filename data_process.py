import pandas as pd


# 读取指定日期的csv数据文件
def get_date_data(t_date):
    root_directory = 'DOVID-19_main_data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/'
    date = str(t_date)
    suffix = '.csv'
    file_directory = root_directory + date + suffix
    data = pd.read_csv(file_directory)
    return data


# 将数据扁平化为列表
def flat_total_data(t_date):
    total = get_date_data(t_date)
    country = []
    provence = []
    confirmed = []
    for i in total['Country_Region']:
        country.append(i)
    for i in total['Province_State']:
        provence.append(i)
    for i in total['Confirmed']:
        confirmed.append(i)
    ls = zip(country, provence, confirmed)
    return ls


# 读取中国各省份疫情数据
def deal_china_data(t_date):
    ls = flat_total_data(t_date)
    t_ls = []
    c_ls = []
    pinyin = {'Anhui': '安徽', 'Beijing': '北京', 'Chongqing': '重庆', 'Fujian': '福建', 'Gansu': '甘肃', 'Guangdong': '广东',
              'Guangxi': '广西', 'Guizhou': '贵州', 'Hainan': '海南', 'Hebei': '河北', 'Heilongjiang': '黑龙江', 'Henan': '河南',
              'Hong Kong': '香港', 'Hubei': '湖北', 'Hunan': '湖南', 'Inner Mongolia': '内蒙古', 'Jiangsu': '江苏',
              'Jiangxi': '江西', 'Jilin': '吉林', 'Liaoning': '辽宁', 'Macau': '澳门', 'Ningxia': '宁夏', 'Qinghai': '青海',
              'Shaanxi': '陕西', 'Shandong': '山东', 'Shanghai': '上海', 'Shanxi': '山西', 'Sichuan': '四川', 'Tianjin': '天津',
              'Tibet': '西藏', 'Xinjiang': '新疆', 'Yunnan': '云南', 'Zhejiang': '浙江', 'Unknown': '曾母暗沙'}
    for i in ls:
        if 'China' in i:
            t_ls.append(list(i))
    for i in t_ls:
        temp = i[1]
        temp = pinyin.get(temp)
        i[1] = temp
        c_ls.append(i[1:3])
    return c_ls


print(deal_china_data('01-01-2021'))
