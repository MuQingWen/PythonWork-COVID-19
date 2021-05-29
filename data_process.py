import pandas as pd
import datetime


# 日期字符串拼接
def date_stitch(t_date):
    root_directory = 'DOVID-19_main_data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/'
    date = str(t_date)
    suffix = '.csv'
    file_directory = root_directory + date + suffix
    return file_directory


# 日期分割
def split_date(t_date):
    date = str(t_date).split('-')
    return date


# 读取指定日期的csv数据文件
def get_date_data(t_date):
    data = pd.read_csv(date_stitch(t_date))
    return data


# 读取日期段的csv数据文件并处理
def get_date_period_data(begin_date, end_date, t_country):
    begin = datetime.date(int(split_date(begin_date)[2]), int(split_date(begin_date)[0]),
                          int(split_date(begin_date)[1]))
    end = datetime.date(int(split_date(end_date)[2]), int(split_date(end_date)[0]), int(split_date(end_date)[1]))
    d = begin
    delta = datetime.timedelta(days=1)
    total_data = []
    country = t_country
    while d <= end:
        date = str(d.strftime("%m-%d-%Y"))
        total_data.append(flat_country_data(date,country))
        d += delta
    return total_data


# 读取制定日期的某国家的疫情数据
def flat_country_data(t_date, t_country):
    total = get_date_data(t_date)
    country = []
    provence = []
    confirmed = []
    deaths = []
    recovered = []
    active = []
    all_confirmed = 0
    all_deaths = 0
    all_recovered = 0
    all_active = 0
    for i in total['Country_Region']:
        country.append(i)
    for i in total['Province_State']:
        provence.append(i)
    for i in total['Confirmed']:
        confirmed.append(i)
    for i in total['Deaths']:
        deaths.append(i)
    for i in total['Recovered']:
        recovered.append(i)
    for i in total['Active']:
        active.append((i))
    t_ls = zip(country, provence, confirmed, deaths, recovered, active)
    tt_ls = get_country_data(t_ls, t_country)
    temp = tt_ls[0]
    all_country = temp[0]
    for i in tt_ls:
        all_confirmed = all_confirmed + float(i[2])
        all_deaths = all_deaths + float(i[3])
        all_recovered = all_recovered + float(i[4])
        all_active = all_active + float(i[5])
    ls = [all_country, t_date, all_confirmed, all_deaths, all_recovered, all_active]
    return ls


# 读取某国家的疫情数据
def get_country_data(t_list, t_country):
    t_ls = t_list
    ls = []
    for i in t_ls:
        if str(i[0]) == str(t_country):
            ls.append(i)
    return ls


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
