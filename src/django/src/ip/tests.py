
import requests

from bs4 import BeautifulSoup
def get(city,cityname_zh):
    url = "https://www.tianqi.com/"+ city +"/"
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
        }
    print(url)
    print(cityname_zh,"天气预报\n---------------------")
    res = requests.get(url,headers=headers).text
    # print(res)
    soup = BeautifulSoup(res,'lxml')
    weather = soup.find('dd', class_='weather')
    # 温度情况
    ctemperature_now = weather.find('p', class_='now').text
    temperature_today = weather.find('span')
    # 天气情况
    csituation_now = temperature_today.find('b').text
    # 当日温度区间
    csituation_temperature = temperature_today.text.replace(csituation_now,"")

    print("温度情况:",ctemperature_now)
    print("天气情况:",csituation_now)
    print("当日温度区间:",csituation_temperature)


    #
    shidu_atart = soup.find("dd",class_="shidu")
    shidu = shidu_atart.find_all("b")
    # 湿度
    humidity = shidu[0].text.split("：")[1]
    # 风向
    wind = shidu[1].text.split("：")[1]
    # 紫外线
    ultraviolet = shidu[2].text.split("：")[1]

    print("湿度:", humidity)
    print("风向:", wind)
    print("紫外线:", ultraviolet)


    #
    kongqi_atart = soup.find("dd", class_="kongqi")
    # 空气质量
    air = kongqi_atart.find("h5").text.split("：")[1]
    # PM
    pm = kongqi_atart.find("h6").text.split(": ")[1]
    # 日出
    sun_start = kongqi_atart.find("span").text.split(": ")[1].replace("日落","")
    # 日落
    sun_end = kongqi_atart.find("span").text.split(": ")[2]

    print("空气质量:", air)
    print("PM:", pm)
    print("日出:", sun_start)
    print("日落:", sun_end)


city = "luchengqu"
city_start = "鹿城区"

get(city,city_start)




















# # coding: UTF-8
#
# from django.test import TestCase
#
# # Create your tests here.
#
# import requests,xml.dom.minidom
#
# res_xml = requests.get("http://flash.weather.com.cn/wmaps/xml/china.xml").text
# DOMTree = xml.dom.minidom.parseString(res_xml)
# china = DOMTree.documentElement
# citys = china.getElementsByTagName('city')
# for city in citys:
#     city = city.getAttribute('quName')
#     if city == '浙江':
#         print(city.getAttribute('pyName'))
#
#
#
# import urllib.parse
# a="黑龙江"
# import binascii,math
# print(int(res_xml[0x1f]))
# print(res_xml[0x20])
# print(res_xml[0x21])
#
#
# hei_quote = urllib.parse.quote(a)
# # print(type())
# print(hei_quote)
# hei = urllib.parse.unquote(hei_quote)
# print(hei)
