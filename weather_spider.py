import re
import requests
import weather_dao
from requests.exceptions import RequestException


def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        return None


def parse_weather(idd):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'}
    ccnumber = weather_dao.find_city_number(idd)
    city_number = str(ccnumber)

    html = get_one_page('http://www.weather.com.cn/weather1d/' + city_number + '.shtml', headers)
    if not html:
        print("城市代码有误！")
        exit(1)
    city_name = weather_dao.find_city_name(city_number)
    aim = re.findall('<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日(.*?)时(.*?) (.*?)  (.*?)  (.*?)"',
                     html,re.S)

    lightdata = re.findall('<li class="li1 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>',
                           html, re.S)
    colddata = re.findall('<li class="li2 hot">\n(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>', html, re.S)
    weardata = re.findall(
        '<li class="li3 hot" id="chuanyi">\n(.*?)<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>',
        html, re.S)

    print(city_name)
    today_time = "当前日期：%s月%s日,%s" % (aim[0][0], aim[0][1], aim[0][4])
    print(today_time)
    update_time = "更新时间：%s:00" % aim[0][2]
    print(update_time)
    today_wether = "当前天气：%s" % aim[0][5]
    print(today_wether)
    today_temperature = "今日温度：%s" % aim[0][6]
    print(today_temperature)


    today_ziwaixian = "%s:%s  %s" % (lightdata[0][1], lightdata[0][0], lightdata[0][2])
    print(today_ziwaixian)
    today_yundong = "%s:%s" % (colddata[0][1], colddata[0][2])
    print(today_yundong)
    today_wear = "%s:%s  %s" % (weardata[0][2], weardata[0][1], weardata[0][3])
    print(today_wear)

    print("--" * 40)


    weather_dao.update_weather_spider(city_number, today_time, update_time, today_wether, today_temperature,
                                      today_ziwaixian,
                                      today_yundong, today_wear)


def mistaken():
    try:
        print('*****循环跳过，本页无内容*****')
        ######采集代码##########
        print('——————————正常运行——————————')
    except:
        mistaken()


if __name__ == '__main__':
    for idd in range(1, 448):
        try:
            parse_weather(idd)
            # time.sleep(random.randint(1, 5))
        except:
            mistaken()
            idd += 1
            fo = open("D:\phython\dataaaaa\mistakes.txt", "a")
            fo.write(f"第{idd}条对应的城市代码有问题\n")
            fo.close()

