import requests
import json
import pandas as pd
import datetime

from pyecharts.charts import Map
from pyecharts import options as opts


#  腾讯数据接口获取json格式疫情数据
def get_ncp_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    data = requests.get(url).json()['data']
    print(data)
    return data


#  扁平化中国疫情数据
def flatten_ncp_data():
    all = json.loads(get_ncp_data())
    #  初始化结果链表
    provinces = []
    date = all['lastUpdateTime']
    #  获取各省份确诊病例
    china = all['areaTree'][0]['children']  # 获得中国数据
    for province in china:
        province_ncp = province['children']
        province_ncp = {
            '日期': date,
            '省份': province['name'],
            '累计确认': province['total']['confirm']
        }
        provinces.append(province_ncp)

    return provinces


#  渲染可视化地图
def render_map_chart():
    provinces = flatten_ncp_data()
    df = pd.DataFrame(provinces)

    map_chart = Map()
    map_chart.add(
        "全国NCP确诊病例分布图",
        [list(z) for z in zip(list(df["省份"]), list(df['累计确认']))],
        "china",
        is_map_symbol_show=False
    )
    map_chart.set_global_opts(
        title_opts=opts.TitleOpts(
            title="NCP疫情地图(" + str(datetime.date.today()) + ")"
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            pieces=[
                {"min": 1, "max": 9, "label": "1-9人", "color": "#FFE6BE"},
                {"min": 10, "max": 99, "label": "10-99人", "color": "#FFB769"},
                {"min": 100, "max": 499, "label": "100-499人", "color": "#FF8F66"},
                {"min": 500, "max": 999, "label": "500-999人", "color": "#ED514E"},
                {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CA0D11"},
                {"min": 10000, "max": 100000, "label": "10000人以上", "color": "#A52A2A"}
            ]))

    map_chart.render('ncp_map_{}.html'.format(datetime.date.today()))


if __name__ == '__main__':
    render_map_chart()