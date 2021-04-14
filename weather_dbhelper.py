import mysql.connector


# 返回一个连接
def get_conn():
    conn = mysql.connector.connect(
        host="127.0.0.1",  # 主机
        user="root",  # 用户
        passwd="root",  # 密码
        database="city_map",
        auth_plugin="mysql_native_password"
    )
    return conn


# 执行一个查询
def select(sql):
    conn = get_conn()
    # dictionary=True使得返回结果是字典的列表
    mycursor = conn.cursor(dictionary=True)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    mycursor.close()
    conn.close()
    return result


# 如何添加一条数据 解决更新 insert delete update
def update(sql, *param):
    conn = get_conn()
    mycursor = conn.cursor()
    mycursor.execute(sql, param)
    mycursor.close()
    conn.commit()
    conn.close()


def delete(sql, *param):
    conn = get_conn()
    mycursor = conn.cursor()
    mycursor.execute(sql, param)
    mycursor.close()
    conn.commit()
    conn.close()
