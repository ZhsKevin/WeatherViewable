import json
import pymysql


def get_data():
    # 打开数据库连接
    db = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="city_map", port=3306)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * from city_weather")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    result = []
    for i in data:
        result.append({
            "city_number": i[1],
            "city_name": i[2],
            "today_time": i[3],
            "update_time": i[4],
            "today_wether": i[5],
            "today_temperature": i[6],
            "today_ziwaixian": i[7],
            "today_yundong": i[8],
            "today_wear": i[9],

        })

    # 打印数据
    # print(json.dumps(result, indent=1, ensure_ascii=False))
    # 关闭数据库连接
    db.close()
    # return json.dumps(result, indent=1, ensure_ascii=False)
    return result


# if __name__ == '__main__':
#     results=get_data()
#     print(results)