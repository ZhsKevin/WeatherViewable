import dataexct
import get_exatdata

if __name__ == '__main__':
    append_result = get_exatdata.get_data()
    final = dataexct.save(append_result)
    url = "D:\phython\pythonProjects\weatherDataView\WeatherViewApp\static\js\data.js"
    dataexct.write_to_js(final, url)