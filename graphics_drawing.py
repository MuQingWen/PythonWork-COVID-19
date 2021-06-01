from pyecharts.charts import Map
from pyecharts.charts import Line
from pyecharts import options
from data_process import *


# 绘制中国疫情数据图
def render_china_map_chart(t_date):
    province_data = deal_china_data(t_date)
    map_country = Map()
    map_country.set_global_opts(title_opts=options.TitleOpts(title="中国疫情图-确诊人数"),
                                visualmap_opts=options.VisualMapOpts(is_piecewise=True,
                                                                     pieces=[
                                                                         {"min": 1000, "label": '>1000人',
                                                                          "color": "#6F171F"},
                                                                         # 不指定 max，表示 max 为无限大（Infinity）。
                                                                         {"min": 500, "max": 1000,
                                                                          "label": '500-1000人', "color": "#C92C34"},
                                                                         {"min": 100, "max": 499,
                                                                          "label": '100-499人', "color": "#E35B52"},
                                                                         {"min": 10, "max": 99, "label": '10-99人',
                                                                          "color": "#F39E86"},
                                                                         {"min": 1, "max": 9, "label": '1-9人',
                                                                          "color": "#FDEBD0"}]))
    # 将数据导入地图内，地图模式选择china
    map_country.add("确诊", list(province_data), maptype="china")
    # 生成html文件
    map_country.render("country.html")


def render_dayly_chart(begin_date, end_date, t_country):
    date = []
    confirmed = []
    deaths = []
    recovered = []
    data = get_date_period_data(begin_date, end_date, t_country)
    for i in data:
        date.append(i[1])
        confirmed.append(i[2])
        deaths.append(i[3])
        recovered.append(i[4])
    line = Line()
    line.add_xaxis(date)
    line.add_yaxis("确诊人数", confirmed, is_smooth = True)
    line.add_yaxis("死亡人数", deaths, is_smooth = True)
    line.add_yaxis("恢复人数", recovered, is_smooth = True)
    line.set_global_opts(title_opts=options.TitleOpts(title = "{}疫情数据统计图".format(t_country)))
    line.set_series_opts(label_opts=options.LabelOpts(is_show=False))
    line.render("line.html")

