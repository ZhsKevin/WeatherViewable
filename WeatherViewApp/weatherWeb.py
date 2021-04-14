from flask import Flask, render_template, request
import weather_dao

import time

app = Flask(__name__)

@app.route("/")
def weather_view():
    predicts = weather_dao.find_all_weather_predict()
    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return render_template('WeatherView.html', predict1=predicts[0], predict2=predicts[1], predict3=predicts[2],
                           timenow=timenow)


if __name__ == '__main__':


    app.run(
        port=5001,
        debug=True
    )
    # 默认绑定的IP是127.0.0.1
