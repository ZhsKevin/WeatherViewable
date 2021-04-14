import weather_dbhelper



def add_weather_io(city_number, city_name):
    sql = 'insert into city_weather(city_number,city_name) values(%s,%s)'
    weather_dbhelper.update(sql, city_number, city_name)

def update_predict_byid(idd,tem_ave,tem_max,tem_min,rain,cloud):
    sql='UPDATE weather_predict SET tem_ave = %s , tem_max = %s , tem_min = %s , rain = %s , cloud = %s WHERE predict_id = %s '
    weather_dbhelper.update(sql, tem_ave, tem_max, tem_min, rain, cloud, idd)
# city_number,city_name,today_time,update_time,today_wether,today_temperature,today_ziwaixian,today_yundong,today_wear


def update_weather_spider( city_number, today_time, update_time, today_wether, today_temperature,
                          today_ziwaixian,
                          today_yundong, today_wear):
    sql = 'UPDATE city_weather SET today_time = %s , update_time = %s,today_wether = %s,' \
          'today_temperature = %s ,today_ziwaixian = %s,today_yundong = %s,today_wear = %s WHERE city_number = %s '
    weather_dbhelper.update(sql, today_time, update_time, today_wether, today_temperature, today_ziwaixian,
                            today_yundong, today_wear, city_number)


def find_city_number(idd):
    sql = 'SELECT * FROM city_weather where data_id  = "{}" '.format(idd)
    results = weather_dbhelper.select(sql)
    for result in results:
        return result['city_number']

def find_all_weather_predict():
    sql = 'SELECT * FROM weather_predict '
    results = weather_dbhelper.select(sql)
    return results


def find_city_name(city_number):
    sql = 'SELECT * FROM city_weather where city_number  = "{}" '.format(city_number)
    results = weather_dbhelper.select(sql)
    for result in results:
        return result['city_name']

