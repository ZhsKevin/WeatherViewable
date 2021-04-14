# coding:utf-8
# 源数据
import json
# # append_result 为从数据库提取的数据
# append_result = [
#     {'city_number': 101010100, 'city_name': '北京', 'today_time': '当前日期：01月10日,周日', 'update_time': '更新时间：08:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：2/-7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101010300, 'city_name': '朝阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-7/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101010400, 'city_name': '顺义', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101010500, 'city_name': '怀柔', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-13/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101010600, 'city_name': '通州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-9/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101010700, 'city_name': '昌平', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101010800, 'city_name': '延庆', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-15/-2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101010900, 'city_name': '丰台', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/4°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011000, 'city_name': '石景山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011100, 'city_name': '大兴', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011200, 'city_name': '房山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-12/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011300, 'city_name': '密云', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-15/0°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011400, 'city_name': '门头沟', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011500, 'city_name': '平谷', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-14/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011600, 'city_name': '八达岭', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-7/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011700, 'city_name': '佛爷顶', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/3°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101011800, 'city_name': '汤河口', 'today_time': None, 'update_time': None, 'today_wether': None,
#      'today_temperature': None, 'today_ziwaixian': None, 'today_yundong': None, 'today_wear': None},
#     {'city_number': 101011900, 'city_name': '密云上甸子', 'today_time': None, 'update_time': None, 'today_wether': None,
#      'today_temperature': None, 'today_ziwaixian': None, 'today_yundong': None, 'today_wear': None},
#     {'city_number': 101012000, 'city_name': '斋堂', 'today_time': None, 'update_time': None, 'today_wether': None,
#      'today_temperature': None, 'today_ziwaixian': None, 'today_yundong': None, 'today_wear': None},
#     {'city_number': 101012100, 'city_name': '霞云岭', 'today_time': None, 'update_time': None, 'today_wether': None,
#      'today_temperature': None, 'today_ziwaixian': None, 'today_yundong': None, 'today_wear': None},
#     {'city_number': 101012200, 'city_name': '北京城区', 'today_time': None, 'update_time': None, 'today_wether': None,
#      'today_temperature': None, 'today_ziwaixian': None, 'today_yundong': None, 'today_wear': None},
#     {'city_number': 101010200, 'city_name': '海淀', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/3°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030100, 'city_name': '天津', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-7/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030300, 'city_name': '宝坻', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030400, 'city_name': '东丽', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030500, 'city_name': '西青', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030600, 'city_name': '北辰', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101031400, 'city_name': '蓟县', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-11/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030800, 'city_name': '汉沽', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-7/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030900, 'city_name': '静海', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101031000, 'city_name': '津南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-9/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101031100, 'city_name': '塘沽', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101031200, 'city_name': '大港', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-7/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030200, 'city_name': '武清', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-9/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101030700, 'city_name': '宁河', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-11/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101020100, 'city_name': '上海', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101020300, 'city_name': '宝山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-3/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101020500, 'city_name': '嘉定', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101020600, 'city_name': '南汇', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-2/5°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天气较舒适，减肥正当时。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101021300, 'city_name': '浦东', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101020800, 'city_name': '青浦', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101020900, 'city_name': '松江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101021000, 'city_name': '奉贤', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101021100, 'city_name': '崇明', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101021200, 'city_name': '徐家汇', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101020200, 'city_name': '闵行', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101020700, 'city_name': '金山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090101, 'city_name': '石家庄', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-6/3°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090301, 'city_name': '张家口', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-15/-5°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090402, 'city_name': '承德', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-16/-3°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090501, 'city_name': '唐山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-13/1°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101091101, 'city_name': '秦皇岛', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-13/-1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090701, 'city_name': '沧州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-11/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090801, 'city_name': '衡水', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090901, 'city_name': '邢台', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-7/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101091001, 'city_name': '邯郸', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-7/3°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090201, 'city_name': '保定', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-12/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101090601, 'city_name': '廊坊', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101180101, 'city_name': '郑州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：-4/4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101180301, 'city_name': '新乡', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-7/3°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101180401, 'city_name': '许昌', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-6/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101180501, 'city_name': '平顶山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-2/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101180601, 'city_name': '信阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-3/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101180701, 'city_name': '南阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-4/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101180801, 'city_name': '开封', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-3/3°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101180901, 'city_name': '洛阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-3/4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101181001, 'city_name': '商丘', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-7/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101181101, 'city_name': '焦作', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-3/6°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101181201, 'city_name': '鹤壁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-11/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101181301, 'city_name': '濮阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-7/3°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101181401, 'city_name': '周口', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-3/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101181501, 'city_name': '漯河', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-5/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101181601, 'city_name': '驻马店', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：-5/4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101181701, 'city_name': '三门峡', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-6/2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101181801, 'city_name': '济源', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101180201, 'city_name': '安阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-6/2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220101, 'city_name': '合肥', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220301, 'city_name': '芜湖', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220401, 'city_name': '淮南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220501, 'city_name': '马鞍山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220601, 'city_name': '安庆', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220701, 'city_name': '宿州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-8/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220801, 'city_name': '阜阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220901, 'city_name': '亳州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-7/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101221001, 'city_name': '黄山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101221101, 'city_name': '滁州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101221201, 'city_name': '淮北', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-7/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101221301, 'city_name': '铜陵', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-3/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101221401, 'city_name': '宣城', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101221501, 'city_name': '六安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101221601, 'city_name': '巢湖', 'today_time': None, 'update_time': None, 'today_wether': None,
#      'today_temperature': None, 'today_ziwaixian': None, 'today_yundong': None, 'today_wear': None},
#     {'city_number': 101221701, 'city_name': '池州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101220201, 'city_name': '蚌埠', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-6/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101210101, 'city_name': '杭州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-2/6°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101211101, 'city_name': '舟山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-3/4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101210201, 'city_name': '湖州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-3/6°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101210301, 'city_name': '嘉兴', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-3/5°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101210901, 'city_name': '金华', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-2/7°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101210501, 'city_name': '绍兴', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-3/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101210601, 'city_name': '台州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-3/7°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101210701, 'city_name': '温州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-4/9°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101210801, 'city_name': '丽水', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-3/10°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101211001, 'city_name': '衢州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-3/7°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101210401, 'city_name': '宁波', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101040100, 'city_name': '重庆', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：4/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101040300, 'city_name': '合川', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：3/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101040400, 'city_name': '南川', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101040500, 'city_name': '江津', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：4/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101040600, 'city_name': '万盛', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：3/8°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101040700, 'city_name': '渝北', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101040800, 'city_name': '北碚', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：3/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101040900, 'city_name': '巴南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101041000, 'city_name': '长寿', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：3/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101041100, 'city_name': '黔江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：0/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101041200, 'city_name': '万州天城', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：4/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101041300, 'city_name': '万州龙宝', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：3/8°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101041400, 'city_name': '涪陵', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：3/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101041500, 'city_name': '开县', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：2/7°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101041600, 'city_name': '城口', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-2/3°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101041700, 'city_name': '云阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：4/7°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101041800, 'city_name': '巫溪', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：1/8°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101041900, 'city_name': '奉节', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：4/8°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101042000, 'city_name': '巫山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：1/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101042100, 'city_name': '潼南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：2/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101042200, 'city_name': '垫江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：1/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101042300, 'city_name': '梁平', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：0/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101042400, 'city_name': '忠县', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/7°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101042500, 'city_name': '石柱', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：-1/5°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101042600, 'city_name': '大足', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：2/4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101042700, 'city_name': '荣昌', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：3/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101042800, 'city_name': '铜梁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：2/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101042900, 'city_name': '璧山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：3/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101043000, 'city_name': '丰都', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101043100, 'city_name': '武隆', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101043200, 'city_name': '彭水', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101043300, 'city_name': '綦江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101043400, 'city_name': '酉阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-1/2°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101043600, 'city_name': '秀山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：0/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101043700, 'city_name': '沙坪坝', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：4/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101040200, 'city_name': '永川', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：3/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101230101, 'city_name': '福州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：2/11°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101230501, 'city_name': '泉州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：5/12°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101230601, 'city_name': '漳州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：4/15°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101230701, 'city_name': '龙岩', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：0/14°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101230509, 'city_name': '晋江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：5/12°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101230901, 'city_name': '南平', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：0/11°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101230201, 'city_name': '厦门', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：5/13°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101230301, 'city_name': '宁德', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：1/9°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101230401, 'city_name': '莆田', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：5/12°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101230801, 'city_name': '三明', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：0/11°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101160101, 'city_name': '兰州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雪', 'today_temperature': '今日温度：-10/-4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101160301, 'city_name': '平凉', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-12/-4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101160401, 'city_name': '庆阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-8/-4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101160501, 'city_name': '武威', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雪', 'today_temperature': '今日温度：-16/-7°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101160601, 'city_name': '金昌', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雪', 'today_temperature': '今日温度：-14/-6°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101161401, 'city_name': '嘉峪关', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雪', 'today_temperature': '今日温度：-16/-6°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101160801, 'city_name': '酒泉', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雪转晴', 'today_temperature': '今日温度：-14/-5°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101160901, 'city_name': '天水', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-7/-2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101161001, 'city_name': '武都', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-8/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101161101, 'city_name': '临夏', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雪转阴', 'today_temperature': '今日温度：-12/-4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101161201, 'city_name': '合作', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雪转多云', 'today_temperature': '今日温度：-16/-4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101161301, 'city_name': '白银', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-14/-7°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101160201, 'city_name': '定西', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-14/-6°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101160701, 'city_name': '张掖', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雪转多云', 'today_temperature': '今日温度：-20/-9°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101280101, 'city_name': '广州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：7/12°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101280301, 'city_name': '惠州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：6/12°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101280401, 'city_name': '梅州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：2/12°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101280501, 'city_name': '汕头', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：7/14°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101280601, 'city_name': '深圳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/12°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101280701, 'city_name': '珠海', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：9/13°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101280800, 'city_name': '佛山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/12°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101280901, 'city_name': '肇庆', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/11°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101281001, 'city_name': '湛江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/13°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281101, 'city_name': '江门', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/12°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281201, 'city_name': '河源', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：5/13°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281301, 'city_name': '清远', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：7/12°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281401, 'city_name': '云浮', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/12°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281501, 'city_name': '潮州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：4/14°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281601, 'city_name': '东莞', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：8/12°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281701, 'city_name': '中山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：8/12°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281801, 'city_name': '阳江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：8/14°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101281901, 'city_name': '揭阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：5/13°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101282001, 'city_name': '茂名', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：10/14°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101282101, 'city_name': '汕尾', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：7/13°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101280201, 'city_name': '韶关', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：4/10°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101300101, 'city_name': '南宁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/12°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101300301, 'city_name': '柳州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：5/10°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101300401, 'city_name': '来宾', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：5/10°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101300501, 'city_name': '桂林', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：3/8°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101300601, 'city_name': '梧州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：5/9°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101301401, 'city_name': '防城港', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/11°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101300801, 'city_name': '贵港', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：6/11°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101300901, 'city_name': '玉林', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/12°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101301001, 'city_name': '百色', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：6/11°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101301101, 'city_name': '钦州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：7/11°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101301201, 'city_name': '河池', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：5/10°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101301301, 'city_name': '北海', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：8/12°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101300201, 'city_name': '崇左', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：7/10°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101300701, 'city_name': '贺州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：4/8°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101260101, 'city_name': '贵阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-2/0°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101260301, 'city_name': '安顺', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-2/0°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101260401, 'city_name': '都匀', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：0/2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101260906, 'city_name': '兴义', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：冻雨转阴', 'today_temperature': '今日温度：0/1°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101260601, 'city_name': '铜仁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：2/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101260701, 'city_name': '毕节', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：冻雨转雨夹雪', 'today_temperature': '今日温度：-3/-1°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101260801, 'city_name': '六盘水', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：雨夹雪', 'today_temperature': '今日温度：-3/-2°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101260201, 'city_name': '遵义', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：0/2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101260501, 'city_name': '凯里', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：1/3°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101290101, 'city_name': '昆明', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：4/10°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101290301, 'city_name': '红河', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：8/15°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天快来了，雨天坚持室内运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101290601, 'city_name': '文山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：5/11°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天快来了，雨天坚持室内运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101290701, 'city_name': '玉溪', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：7/15°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101290801, 'city_name': '楚雄', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：7/19°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101290901, 'city_name': '普洱', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：12/19°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天快来了，雨天坚持室内运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101291001, 'city_name': '昭通', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：雨夹雪', 'today_temperature': '今日温度：0/1°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101291101, 'city_name': '临沧', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：8/22°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101291201, 'city_name': '怒江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：9/23°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101291301, 'city_name': '香格里拉', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-2/6°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101291401, 'city_name': '丽江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：1/15°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101291501, 'city_name': '德宏', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：11/23°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天气较舒适，减肥正当时。', 'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101291601, 'city_name': '景洪', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：15/22°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:春天快来了，雨天坚持室内运动吧。',
#      'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101290201, 'city_name': '大理', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：5/18°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101290401, 'city_name': '曲靖', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：2/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101290501, 'city_name': '保山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：7/18°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101080101, 'city_name': '呼和浩特', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：-19/-9°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101080301, 'city_name': '乌海', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-18/-5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101080401, 'city_name': '集宁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-19/-8°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101080501, 'city_name': '通辽', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-18/-9°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101081201, 'city_name': '阿拉善左旗', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转扬沙', 'today_temperature': '今日温度：-15/-9°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101080701, 'city_name': '鄂尔多斯', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-15/-9°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101080801, 'city_name': '临河', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-17/-7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101080901, 'city_name': '锡林浩特', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-25/-17°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101081000, 'city_name': '呼伦贝尔', 'today_time': None, 'update_time': None, 'today_wether': None,
#      'today_temperature': None, 'today_ziwaixian': None, 'today_yundong': None, 'today_wear': None},
#     {'city_number': 101081101, 'city_name': '乌兰浩特', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-18/-8°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101080201, 'city_name': '包头', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-18/-6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101080601, 'city_name': '赤峰', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-18/-6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101240101, 'city_name': '南昌', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-2/8°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101240301, 'city_name': '上饶', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-3/10°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101240401, 'city_name': '抚州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-3/9°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101240501, 'city_name': '宜春', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：-1/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101241101, 'city_name': '鹰潭', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-3/8°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101240701, 'city_name': '赣州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：0/10°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101240801, 'city_name': '景德镇', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-5/8°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101240901, 'city_name': '萍乡', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：2/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101241001, 'city_name': '新余', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：0/8°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101240201, 'city_name': '九江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-3/6°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101240601, 'city_name': '吉安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：1/9°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200101, 'city_name': '武汉', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200501, 'city_name': '黄冈', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-2/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200801, 'city_name': '荆州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：0/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200901, 'city_name': '宜昌', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：0/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101201001, 'city_name': '恩施', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转小雪', 'today_temperature': '今日温度：2/5°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101201101, 'city_name': '十堰', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101201201, 'city_name': '神农架', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/3°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101201301, 'city_name': '随州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-4/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101201401, 'city_name': '荆门', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：0/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101201501, 'city_name': '天门', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-2/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101201601, 'city_name': '仙桃', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-2/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101201701, 'city_name': '潜江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200201, 'city_name': '襄樊', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200301, 'city_name': '鄂州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200401, 'city_name': '孝感', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-3/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200601, 'city_name': '黄石', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101200701, 'city_name': '咸宁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-2/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101270101, 'city_name': '成都', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：1/7°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101270301, 'city_name': '自贡', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：3/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101270401, 'city_name': '绵阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：1/8°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101270501, 'city_name': '南充', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：3/7°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101270601, 'city_name': '达州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/7°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101270701, 'city_name': '遂宁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：2/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101270801, 'city_name': '广安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转小雨', 'today_temperature': '今日温度：2/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101270901, 'city_name': '巴中', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：0/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101271001, 'city_name': '泸州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：3/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101271101, 'city_name': '宜宾', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：2/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101271201, 'city_name': '内江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：2/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101271301, 'city_name': '资阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：1/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101271401, 'city_name': '乐山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：2/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101271501, 'city_name': '眉山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨转阴', 'today_temperature': '今日温度：1/6°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101271601, 'city_name': '凉山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：2/9°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101271701, 'city_name': '雅安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：0/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101271801, 'city_name': '甘孜', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-7/10°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101271901, 'city_name': '阿坝', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-11/0°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101272001, 'city_name': '德阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：1/8°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101272101, 'city_name': '广元', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：0/7°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101270201, 'city_name': '攀枝花', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：7/21°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:舒适  建议穿长袖衬衫单裤等服装。'},
#     {'city_number': 101170101, 'city_name': '银川', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-15/-4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101170501, 'city_name': '中卫', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-16/-3°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101170401, 'city_name': '固原', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-13/-6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101170201, 'city_name': '石嘴山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-16/-4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101170301, 'city_name': '吴忠', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-12/-4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101150101, 'city_name': '西宁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-15/-7°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101150301, 'city_name': '黄南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-14/-8°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101150801, 'city_name': '海北', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-19/-6°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101150501, 'city_name': '果洛', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-15/0°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101150601, 'city_name': '玉树', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-15/5°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101150701, 'city_name': '海西', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转晴', 'today_temperature': '今日温度：-16/-7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101150201, 'city_name': '海东', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-13/-5°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101150401, 'city_name': '海南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转晴', 'today_temperature': '今日温度：-14/-4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120101, 'city_name': '济南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-6/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120601, 'city_name': '潍坊', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-9/0°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120901, 'city_name': '临沂', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/4°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101121001, 'city_name': '菏泽', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-7/4°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101121101, 'city_name': '滨州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-11/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101121201, 'city_name': '东营', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101121301, 'city_name': '威海', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转小雪', 'today_temperature': '今日温度：-7/-1°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:风雨交加特别冷，适当偷懒低强度运动吧。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101121401, 'city_name': '枣庄', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-7/5°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101121501, 'city_name': '日照', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转阴', 'today_temperature': '今日温度：-7/3°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101121601, 'city_name': '莱芜', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101121701, 'city_name': '聊城', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120201, 'city_name': '青岛', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转阴', 'today_temperature': '今日温度：-6/1°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120301, 'city_name': '淄博', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-11/1°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120401, 'city_name': '德州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-11/2°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120501, 'city_name': '烟台', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-10/0°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120701, 'city_name': '济宁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-7/4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101120801, 'city_name': '泰安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-12/3°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101110101, 'city_name': '西安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-5/2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101110300, 'city_name': '延安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-19/-2°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101110401, 'city_name': '榆林', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-16/-2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101111001, 'city_name': '铜川', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-6/1°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101110601, 'city_name': '商洛', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-4/1°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101110701, 'city_name': '安康', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-2/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101110801, 'city_name': '汉中', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-2/5°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101110901, 'city_name': '宝鸡', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-3/1°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101110200, 'city_name': '咸阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-7/1°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101110501, 'city_name': '渭南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-7/2°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100101, 'city_name': '太原', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-15/-1°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100701, 'city_name': '临汾', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-10/1°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100801, 'city_name': '运城', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-10/2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100901, 'city_name': '朔州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转晴', 'today_temperature': '今日温度：-20/-4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101101001, 'city_name': '忻州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-17/-3°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100501, 'city_name': '长治', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-13/-2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100201, 'city_name': '大同', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转阴', 'today_temperature': '今日温度：-23/-5°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100301, 'city_name': '阳泉', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-10/1°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100401, 'city_name': '晋中', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-15/0°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101100601, 'city_name': '晋城', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-9/2°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101101100, 'city_name': '吕梁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-17/-3°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130101, 'city_name': '乌鲁木齐', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-14/-4°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130301, 'city_name': '石河子', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转阴', 'today_temperature': '今日温度：-23/-17°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130401, 'city_name': '昌吉', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-25/-13°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:雨雪相伴湿冷天，坚持室内低强度运动。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130501, 'city_name': '吐鲁番', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-10/-5°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130601, 'city_name': '库尔勒', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-17/-3°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130701, 'city_name': '阿拉尔', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-14/-2°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130801, 'city_name': '阿克苏', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-15/-2°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130901, 'city_name': '喀什', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-13/-5°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101131001, 'city_name': '伊宁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转阴', 'today_temperature': '今日温度：-16/0°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101131101, 'city_name': '塔城', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转阴', 'today_temperature': '今日温度：-22/-4°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101131201, 'city_name': '哈密', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-23/-5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101131301, 'city_name': '和田', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-9/-3°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101131401, 'city_name': '阿勒泰', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转阴', 'today_temperature': '今日温度：-28/-12°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101131501, 'city_name': '阿图什', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-11/-7°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101131601, 'city_name': '博乐', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-26/-15°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101130201, 'city_name': '克拉玛依', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转阴', 'today_temperature': '今日温度：-30/-17°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101140101, 'city_name': '拉萨', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-5/15°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101140301, 'city_name': '山南', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-4/15°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101140701, 'city_name': '阿里', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-17/2°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101140501, 'city_name': '昌都', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-6/15°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101140601, 'city_name': '那曲', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-18/3°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101140201, 'city_name': '日喀则', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-8/12°C',
#      'today_ziwaixian': '紫外线指数:很强  涂擦SPF20以上，PA++护肤品，避强光。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101140401, 'city_name': '林芝', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-1/11°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101340101, 'city_name': '台北县', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：8/14°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101340201, 'city_name': '高雄', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：13/19°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101340401, 'city_name': '台中', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：5/13°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101310101, 'city_name': '海口', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：11/15°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:风雨相伴，坚持室内运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310201, 'city_name': '三亚', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：15/21°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101310202, 'city_name': '东方', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：13/19°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310203, 'city_name': '临高', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：11/15°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310204, 'city_name': '澄迈', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：10/16°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310205, 'city_name': '儋州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：10/15°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310206, 'city_name': '昌江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：11/17°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310207, 'city_name': '白沙', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：9/15°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310208, 'city_name': '琼中', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：9/14°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310209, 'city_name': '定安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：11/16°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310210, 'city_name': '屯昌', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：10/16°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310211, 'city_name': '琼海', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：12/17°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310212, 'city_name': '文昌', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：12/17°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310214, 'city_name': '保亭', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：12/21°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101310215, 'city_name': '万宁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：12/17°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310216, 'city_name': '陵水', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：13/18°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101310217, 'city_name': '西沙', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：小雨', 'today_temperature': '今日温度：20/25°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:风雨相伴，坚持室内运动吧。', 'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101310220, 'city_name': '南沙岛', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：大雨转中雨', 'today_temperature': '今日温度：25/28°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:风雨相伴，坚持室内运动吧。',
#      'today_wear': '穿衣指数:热  适合穿T恤、短薄外套等夏季服装。'},
#     {'city_number': 101310221, 'city_name': '乐东', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：12/21°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101310222, 'city_name': '五指山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：10/19°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天气较舒适，减肥正当时。',
#      'today_wear': '穿衣指数:较舒适  建议穿薄外套或牛仔裤等服装。'},
#     {'city_number': 101310102, 'city_name': '琼山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：11/15°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:风雨相伴，坚持室内运动吧。', 'today_wear': '穿衣指数:较冷  建议着厚外套加毛衣等服装。'},
#     {'city_number': 101250101, 'city_name': '长沙', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：0/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101250301, 'city_name': '株洲', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101250401, 'city_name': '衡阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：2/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101250501, 'city_name': '郴州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：0/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101250601, 'city_name': '常德', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：0/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101250700, 'city_name': '益阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101250801, 'city_name': '娄底', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101250901, 'city_name': '邵阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-1/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101251001, 'city_name': '岳阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：0/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101251101, 'city_name': '张家界', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：1/6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101251201, 'city_name': '怀化', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：1/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101251301, 'city_name': '黔阳', 'today_time': None, 'update_time': None, 'today_wether': None,
#      'today_temperature': None, 'today_ziwaixian': None, 'today_yundong': None, 'today_wear': None},
#     {'city_number': 101251401, 'city_name': '永州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：2/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101251501, 'city_name': '吉首', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：0/5°C', 'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101250201, 'city_name': '湘潭', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：0/7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101190101, 'city_name': '南京', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101190301, 'city_name': '镇江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101190401, 'city_name': '苏州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-5/6°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:风虽有点大，室内可健身。', 'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101190501, 'city_name': '南通', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-5/4°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101190601, 'city_name': '扬州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-6/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101191301, 'city_name': '宿迁', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-6/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101190801, 'city_name': '徐州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-7/4°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101190901, 'city_name': '淮安', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴', 'today_temperature': '今日温度：-6/5°C', 'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101191001, 'city_name': '连云港', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：-9/4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101191101, 'city_name': '常州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-5/5°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101191201, 'city_name': '泰州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：阴转多云', 'today_temperature': '今日温度：-7/5°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101190201, 'city_name': '无锡', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-5/5°C', 'today_ziwaixian': '紫外线指数:强  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101190701, 'city_name': '盐城', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转阴', 'today_temperature': '今日温度：-6/4°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:冷  建议着棉衣加羊毛衫等冬季服装。'},
#     {'city_number': 101050101, 'city_name': '哈尔滨', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-23/-13°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101050301, 'city_name': '牡丹江', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-25/-13°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101050401, 'city_name': '佳木斯', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-26/-14°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101050501, 'city_name': '绥化', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-25/-14°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101050601, 'city_name': '黑河', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-24/-14°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101051301, 'city_name': '双鸭山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-22/-14°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101050801, 'city_name': '伊春', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-30/-16°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101050901, 'city_name': '大庆', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-23/-13°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101051002, 'city_name': '七台河', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-27/-15°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101051101, 'city_name': '鸡西', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-24/-13°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101051201, 'city_name': '鹤岗', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-29/-14°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101050201, 'city_name': '齐齐哈尔', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-21/-11°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101050701, 'city_name': '大兴安岭', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-30/-15°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060101, 'city_name': '长春', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-20/-11°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060301, 'city_name': '延吉', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-20/-8°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060401, 'city_name': '四平', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-23/-11°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060901, 'city_name': '白山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-24/-10°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060601, 'city_name': '白城', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-21/-8°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060701, 'city_name': '辽源', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-24/-10°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060801, 'city_name': '松原', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-24/-13°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060201, 'city_name': '吉林', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-21/-11°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101060501, 'city_name': '通化', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-22/-9°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070101, 'city_name': '沈阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-18/-6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070301, 'city_name': '鞍山', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-12/-5°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070401, 'city_name': '抚顺', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-20/-7°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070501, 'city_name': '本溪', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-18/-6°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070601, 'city_name': '丹东', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-18/-4°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101071401, 'city_name': '葫芦岛', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-14/-2°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070801, 'city_name': '营口', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-14/-4°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070901, 'city_name': '阜新', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-14/-6°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101071001, 'city_name': '辽阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴转多云', 'today_temperature': '今日温度：-17/-6°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101071101, 'city_name': '铁岭', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-18/-8°C',
#      'today_ziwaixian': '紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。', 'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101071201, 'city_name': '朝阳', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-14/-3°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101071301, 'city_name': '盘锦', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云', 'today_temperature': '今日温度：-14/-4°C',
#      'today_ziwaixian': '紫外线指数:最弱  辐射弱，涂擦SPF8-12防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070201, 'city_name': '大连', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：多云转晴', 'today_temperature': '今日温度：-7/-3°C',
#      'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。', 'today_yundong': '减肥指数:天有点冷风较大，不妨室内运动下。',
#      'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'},
#     {'city_number': 101070701, 'city_name': '锦州', 'today_time': '当前日期：01月09日,周六', 'update_time': '更新时间：20:00',
#      'today_wether': '当前天气：晴', 'today_temperature': '今日温度：-12/-4°C', 'today_ziwaixian': '紫外线指数:中等  涂擦SPF大于15、PA+防晒护肤品。',
#      'today_yundong': '减肥指数:天凉室内可健身，户外运动需保暖。', 'today_wear': '穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。'}]


def write_to_js(final,url):
    str1 = 'var data =' + '\n'
    str2 = final + '\n'
    str3 = ';'
    data = str1 + str2 + str3
    print(data)
    fo = open(url, "w+", encoding="utf-8")
    fo.write(data)

#  main_city变量为过滤后的数据,持久不变
main_city = [
    {
        "provinceName": "北京市",
        "provinceShortName": "北京",
        "locationId": 110000,
        "cities": [
            {
                "cityName": "丰台区",
                "locationId": 110106
            },
            {
                "cityName": "大兴区",
                "locationId": 110115
            },
            {
                "cityName": "海淀区",
                "locationId": 110108
            },
            {
                "cityName": "朝阳区",
                "locationId": 110105
            },
            {
                "cityName": "西城区",
                "locationId": 110102
            },
            {
                "cityName": "昌平区",
                "locationId": 110114
            },
            {
                "cityName": "通州区",
                "locationId": 110112
            },
            {
                "cityName": "东城区",
                "locationId": 110101
            },
            {
                "cityName": "房山区",
                "locationId": 110111
            },
            {
                "cityName": "怀柔区",
                "locationId": 110116
            },
            {
                "cityName": "密云区",
                "locationId": 110118
            },
            {
                "cityName": "石景山区",
                "locationId": 110107
            },
            {
                "cityName": "门头沟区",
                "locationId": 110109
            },
            {
                "cityName": "延庆区",
                "locationId": 110119
            },
            {
                "cityName": "顺义区",
                "locationId": 110113
            },
            {
                "cityName": "平谷区",
                "locationId": 110117
            }
        ]
    },
    {
        "provinceName": "香港",
        "provinceShortName": "香港",
        "locationId": 810000,
        "cities": []
    },
    {
        "provinceName": "上海市",
        "provinceShortName": "上海",
        "locationId": 310000,
        "cities": [
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "境外来沪",
                "locationId": 0
            },
            {
                "cityName": "外地来沪",
                "locationId": 0
            },
            {
                "cityName": "浦东新区",
                "locationId": 310115
            },
            {
                "cityName": "宝山区",
                "locationId": 310113
            },
            {
                "cityName": "闵行区",
                "locationId": 310112
            },
            {
                "cityName": "徐汇区",
                "locationId": 310104
            },
            {
                "cityName": "静安区",
                "locationId": 310106
            },
            {
                "cityName": "松江区",
                "locationId": 310117
            },
            {
                "cityName": "长宁区",
                "locationId": 310105
            },
            {
                "cityName": "普陀区",
                "locationId": 310107
            },
            {
                "cityName": "杨浦区",
                "locationId": 310110
            },
            {
                "cityName": "嘉定区",
                "locationId": 310114
            },
            {
                "cityName": "奉贤区",
                "locationId": 310120
            },
            {
                "cityName": "虹口区",
                "locationId": 310109
            },
            {
                "cityName": "黄浦区",
                "locationId": 310101
            },
            {
                "cityName": "青浦区",
                "locationId": 310118
            },
            {
                "cityName": "金山区",
                "locationId": 310116
            },
            {
                "cityName": "崇明区",
                "locationId": 310151
            }
        ]
    },
    {
        "provinceName": "甘肃省",
        "provinceShortName": "甘肃",
        "locationId": 620000,
        "cities": [
            {
                "cityName": "酒泉",
                "locationId": 620900
            },
            {
                "cityName": "兰州",
                "locationId": 620100
            },
            {
                "cityName": "天水",
                "locationId": 620500
            },
            {
                "cityName": "平凉",
                "locationId": 620800
            },
            {
                "cityName": "定西",
                "locationId": 621100
            },
            {
                "cityName": "甘南",
                "locationId": 623000
            },
            {
                "cityName": "白银",
                "locationId": 620400
            },
            {
                "cityName": "陇南",
                "locationId": 621200
            },
            {
                "cityName": "庆阳",
                "locationId": 621000
            },
            {
                "cityName": "临夏",
                "locationId": 622900
            },
            {
                "cityName": "张掖",
                "locationId": 620700
            },
            {
                "cityName": "金昌",
                "locationId": 620300
            },
            {
                "cityName": "武威",
                "locationId": 620600
            },
            {
                "cityName": "临夏回族自治州",
                "locationId": 622900
            },
            {
                "cityName": "甘南藏族自治州",
                "locationId": 623000
            }
        ]
    },
    {
        "provinceName": "四川省",
        "provinceShortName": "四川",
        "locationId": 510000,
        "cities": [
            {
                "cityName": "成都",
                "locationId": 510100
            },
            {
                "cityName": "雅安",
                "locationId": 511800
            },
            {
                "cityName": "甘孜藏族自治州",
                "locationId": 513300
            },
            {
                "cityName": "达州",
                "locationId": 511700
            },
            {
                "cityName": "南充",
                "locationId": 511300
            },
            {
                "cityName": "广安",
                "locationId": 511600
            },
            {
                "cityName": "泸州",
                "locationId": 510500
            },
            {
                "cityName": "巴中",
                "locationId": 511900
            },
            {
                "cityName": "绵阳",
                "locationId": 510700
            },
            {
                "cityName": "内江",
                "locationId": 511000
            },
            {
                "cityName": "德阳",
                "locationId": 510600
            },
            {
                "cityName": "遂宁",
                "locationId": 510900
            },
            {
                "cityName": "攀枝花",
                "locationId": 510400
            },
            {
                "cityName": "凉山彝族自治州",
                "locationId": 513400
            },
            {
                "cityName": "宜宾",
                "locationId": 511500
            },
            {
                "cityName": "自贡",
                "locationId": 510300
            },
            {
                "cityName": "眉山",
                "locationId": 511400
            },
            {
                "cityName": "广元",
                "locationId": 510800
            },
            {
                "cityName": "资阳",
                "locationId": 512000
            },
            {
                "cityName": "乐山",
                "locationId": 511100
            },
            {
                "cityName": "阿坝藏族羌族自治州",
                "locationId": 513200
            }
        ]
    },
    {
        "provinceName": "河北省",
        "provinceShortName": "河北",
        "locationId": 130000,
        "cities": [
            {
                "cityName": "保定",
                "locationId": 130600
            },
            {
                "cityName": "张家口",
                "locationId": 130700
            },
            {
                "cityName": "廊坊",
                "locationId": 131000
            },
            {
                "cityName": "沧州",
                "locationId": 130900
            },
            {
                "cityName": "唐山",
                "locationId": 130200
            },
            {
                "cityName": "邯郸",
                "locationId": 130400
            },
            {
                "cityName": "石家庄",
                "locationId": 130100
            },
            {
                "cityName": "邢台",
                "locationId": 130500
            },
            {
                "cityName": "秦皇岛",
                "locationId": 130300
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "衡水",
                "locationId": 131100
            },
            {
                "cityName": "承德",
                "locationId": 130800
            },
            {
                "cityName": "待明确",
                "locationId": 0
            }
        ]
    },
    {
        "provinceName": "广东省",
        "provinceShortName": "广东",
        "locationId": 440000,
        "cities": [
            {
                "cityName": "广州",
                "locationId": 440100
            },
            {
                "cityName": "深圳",
                "locationId": 440300
            },
            {
                "cityName": "珠海",
                "locationId": 440400
            },
            {
                "cityName": "东莞",
                "locationId": 441900
            },
            {
                "cityName": "佛山",
                "locationId": 440600
            },
            {
                "cityName": "中山",
                "locationId": 442000
            },
            {
                "cityName": "惠州",
                "locationId": 441300
            },
            {
                "cityName": "汕头",
                "locationId": 440500
            },
            {
                "cityName": "江门",
                "locationId": 440700
            },
            {
                "cityName": "湛江",
                "locationId": 440800
            },
            {
                "cityName": "肇庆",
                "locationId": 441200
            },
            {
                "cityName": "梅州",
                "locationId": 441400
            },
            {
                "cityName": "阳江",
                "locationId": 441700
            },
            {
                "cityName": "茂名",
                "locationId": 440900
            },
            {
                "cityName": "清远",
                "locationId": 441800
            },
            {
                "cityName": "揭阳",
                "locationId": 445200
            },
            {
                "cityName": "韶关",
                "locationId": 440200
            },
            {
                "cityName": "潮州",
                "locationId": 445100
            },
            {
                "cityName": "汕尾",
                "locationId": 441500
            },
            {
                "cityName": "河源",
                "locationId": 441600
            },
            {
                "cityName": "云浮",
                "locationId": 445300
            }
        ]
    },
    {
        "provinceName": "陕西省",
        "provinceShortName": "陕西",
        "locationId": 610000,
        "cities": [
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "西安",
                "locationId": 610100
            },
            {
                "cityName": "安康",
                "locationId": 610900
            },
            {
                "cityName": "汉中",
                "locationId": 610700
            },
            {
                "cityName": "咸阳",
                "locationId": 610400
            },
            {
                "cityName": "渭南",
                "locationId": 610500
            },
            {
                "cityName": "宝鸡",
                "locationId": 610300
            },
            {
                "cityName": "延安",
                "locationId": 610600
            },
            {
                "cityName": "铜川",
                "locationId": 610200
            },
            {
                "cityName": "商洛",
                "locationId": 611000
            },
            {
                "cityName": "榆林",
                "locationId": 610800
            },
            {
                "cityName": "韩城",
                "locationId": 610581
            },
            {
                "cityName": "杨凌",
                "locationId": 0
            }
        ]
    },
    {
        "provinceName": "辽宁省",
        "provinceShortName": "辽宁",
        "locationId": 210000,
        "cities": [
            {
                "cityName": "沈阳",
                "locationId": 210100
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "大连",
                "locationId": 210200
            },
            {
                "cityName": "锦州",
                "locationId": 210700
            },
            {
                "cityName": "葫芦岛",
                "locationId": 211400
            },
            {
                "cityName": "丹东",
                "locationId": 210600
            },
            {
                "cityName": "盘锦",
                "locationId": 211100
            },
            {
                "cityName": "阜新",
                "locationId": 210900
            },
            {
                "cityName": "铁岭",
                "locationId": 211200
            },
            {
                "cityName": "朝阳",
                "locationId": 211300
            },
            {
                "cityName": "鞍山",
                "locationId": 210300
            },
            {
                "cityName": "本溪",
                "locationId": 210500
            },
            {
                "cityName": "辽阳",
                "locationId": 211000
            },
            {
                "cityName": "营口",
                "locationId": 210800
            },
            {
                "cityName": "抚顺",
                "locationId": 210400
            }
        ]
    },
    {
        "provinceName": "重庆市",
        "provinceShortName": "重庆",
        "locationId": 500000,
        "cities": [
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "万州区",
                "locationId": 500101
            },
            {
                "cityName": "江北区",
                "locationId": 500105
            },
            {
                "cityName": "云阳县",
                "locationId": 500235
            },
            {
                "cityName": "合川区",
                "locationId": 500117
            },
            {
                "cityName": "綦江区",
                "locationId": 500110
            },
            {
                "cityName": "长寿区",
                "locationId": 500115
            },
            {
                "cityName": "奉节县",
                "locationId": 500236
            },
            {
                "cityName": "九龙坡区",
                "locationId": 500107
            },
            {
                "cityName": "开州区",
                "locationId": 500154
            },
            {
                "cityName": "忠县",
                "locationId": 500233
            },
            {
                "cityName": "渝中区",
                "locationId": 500103
            },
            {
                "cityName": "垫江县",
                "locationId": 500231
            },
            {
                "cityName": "潼南区",
                "locationId": 500152
            },
            {
                "cityName": "渝北区",
                "locationId": 500112
            },
            {
                "cityName": "两江新区",
                "locationId": -1
            },
            {
                "cityName": "南岸区",
                "locationId": 500108
            },
            {
                "cityName": "石柱土家族自治县",
                "locationId": 500240
            },
            {
                "cityName": "大足区",
                "locationId": 500111
            },
            {
                "cityName": "巫溪县",
                "locationId": 500238
            },
            {
                "cityName": "铜梁区",
                "locationId": 500151
            },
            {
                "cityName": "丰都县",
                "locationId": 500230
            },
            {
                "cityName": "巫山县",
                "locationId": 500237
            },
            {
                "cityName": "沙坪坝区",
                "locationId": 500106
            },
            {
                "cityName": "璧山区",
                "locationId": 500120
            },
            {
                "cityName": "荣昌区",
                "locationId": 500153
            },
            {
                "cityName": "大渡口区",
                "locationId": 500104
            },
            {
                "cityName": "巴南区",
                "locationId": 500113
            },
            {
                "cityName": "涪陵区",
                "locationId": 500102
            },
            {
                "cityName": "永川区",
                "locationId": 500118
            },
            {
                "cityName": "江津区",
                "locationId": 500116
            },
            {
                "cityName": "梁平县",
                "locationId": 500155
            },
            {
                "cityName": "高新区",
                "locationId": 0
            },
            {
                "cityName": "黔江区",
                "locationId": 500114
            },
            {
                "cityName": "城口县",
                "locationId": 500229
            },
            {
                "cityName": "彭水苗族土家族自治县",
                "locationId": 500243
            },
            {
                "cityName": "武隆县",
                "locationId": 500156
            },
            {
                "cityName": "南川区",
                "locationId": 500119
            },
            {
                "cityName": "秀山土家族苗族自治县",
                "locationId": 500241
            },
            {
                "cityName": "酉阳土家族苗族自治县",
                "locationId": 0
            },
            {
                "cityName": "万盛经开区",
                "locationId": 0
            }
        ]
    },
    {
        "provinceName": "台湾",
        "provinceShortName": "台湾",
        "locationId": 710000,
        "cities": []
    },
    {
        "provinceName": "福建省",
        "provinceShortName": "福建",
        "locationId": 350000,
        "cities": [
            {
                "cityName": "境外输入人员",
                "locationId": 0
            },
            {
                "cityName": "福州",
                "locationId": 350100
            },
            {
                "cityName": "莆田",
                "locationId": 350300
            },
            {
                "cityName": "泉州",
                "locationId": 350500
            },
            {
                "cityName": "厦门",
                "locationId": 350200
            },
            {
                "cityName": "宁德",
                "locationId": 350900
            },
            {
                "cityName": "漳州",
                "locationId": 350600
            },
            {
                "cityName": "南平",
                "locationId": 350700
            },
            {
                "cityName": "三明",
                "locationId": 350400
            },
            {
                "cityName": "龙岩",
                "locationId": 350800
            }
        ]
    },
    {
        "provinceName": "浙江省",
        "provinceShortName": "浙江",
        "locationId": 330000,
        "cities": [
            {
                "cityName": "台州",
                "locationId": 331000
            },
            {
                "cityName": "温州",
                "locationId": 330300
            },
            {
                "cityName": "杭州",
                "locationId": 330100
            },
            {
                "cityName": "宁波",
                "locationId": 330200
            },
            {
                "cityName": "金华",
                "locationId": 330700
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "嘉兴",
                "locationId": 330400
            },
            {
                "cityName": "绍兴",
                "locationId": 330600
            },
            {
                "cityName": "省十里丰监狱",
                "locationId": 0
            },
            {
                "cityName": "丽水",
                "locationId": 331100
            },
            {
                "cityName": "衢州",
                "locationId": 330800
            },
            {
                "cityName": "湖州",
                "locationId": 330500
            },
            {
                "cityName": "舟山",
                "locationId": 330900
            }
        ]
    },
    {
        "provinceName": "江苏省",
        "provinceShortName": "江苏",
        "locationId": 320000,
        "cities": [
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "南京",
                "locationId": 320100
            },
            {
                "cityName": "苏州",
                "locationId": 320500
            },
            {
                "cityName": "徐州",
                "locationId": 320300
            },
            {
                "cityName": "淮安",
                "locationId": 320800
            },
            {
                "cityName": "无锡",
                "locationId": 320200
            },
            {
                "cityName": "常州",
                "locationId": 320400
            },
            {
                "cityName": "连云港",
                "locationId": 320700
            },
            {
                "cityName": "南通",
                "locationId": 320600
            },
            {
                "cityName": "泰州",
                "locationId": 321200
            },
            {
                "cityName": "盐城",
                "locationId": 320900
            },
            {
                "cityName": "扬州",
                "locationId": 321000
            },
            {
                "cityName": "宿迁",
                "locationId": 321300
            },
            {
                "cityName": "镇江",
                "locationId": 321100
            }
        ]
    },
    {
        "provinceName": "天津市",
        "provinceShortName": "天津",
        "locationId": 120000,
        "cities": [
            {
                "cityName": "北辰区",
                "locationId": 120113
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "宝坻区",
                "locationId": 120115
            },
            {
                "cityName": "河东区",
                "locationId": 120102
            },
            {
                "cityName": "河北区",
                "locationId": 120105
            },
            {
                "cityName": "南开区",
                "locationId": 120104
            },
            {
                "cityName": "和平区",
                "locationId": 120101
            },
            {
                "cityName": "外地来津",
                "locationId": -1
            },
            {
                "cityName": "东丽区",
                "locationId": 120110
            },
            {
                "cityName": "宁河区",
                "locationId": 120117
            },
            {
                "cityName": "河西区",
                "locationId": 120103
            },
            {
                "cityName": "西青区",
                "locationId": 120111
            },
            {
                "cityName": "滨海新区",
                "locationId": 120116
            },
            {
                "cityName": "武清区",
                "locationId": 120114
            },
            {
                "cityName": "红桥区",
                "locationId": 120106
            },
            {
                "cityName": "津南区",
                "locationId": 120112
            },
            {
                "cityName": "静海区",
                "locationId": 120118
            }
        ]
    },
    {
        "provinceName": "澳门",
        "provinceShortName": "澳门",
        "locationId": 820000,
        "cities": []
    },
    {
        "provinceName": "湖北省",
        "provinceShortName": "湖北",
        "locationId": 420000,
        "cities": [
            {
                "cityName": "武汉",
                "locationId": 420100
            },
            {
                "cityName": "孝感",
                "locationId": 420900
            },
            {
                "cityName": "黄冈",
                "locationId": 421100
            },
            {
                "cityName": "荆州",
                "locationId": 421000
            },
            {
                "cityName": "鄂州",
                "locationId": 420700
            },
            {
                "cityName": "随州",
                "locationId": 421300
            },
            {
                "cityName": "襄阳",
                "locationId": 420600
            },
            {
                "cityName": "黄石",
                "locationId": 420200
            },
            {
                "cityName": "宜昌",
                "locationId": 420500
            },
            {
                "cityName": "荆门",
                "locationId": 420800
            },
            {
                "cityName": "咸宁",
                "locationId": 421200
            },
            {
                "cityName": "十堰",
                "locationId": 420300
            },
            {
                "cityName": "仙桃",
                "locationId": 429004
            },
            {
                "cityName": "天门",
                "locationId": 429006
            },
            {
                "cityName": "恩施州",
                "locationId": 422800
            },
            {
                "cityName": "潜江",
                "locationId": 429005
            },
            {
                "cityName": "神农架林区",
                "locationId": 429021
            }
        ]
    },
    {
        "provinceName": "河南省",
        "provinceShortName": "河南",
        "locationId": 410000,
        "cities": [
            {
                "cityName": "信阳",
                "locationId": 411500
            },
            {
                "cityName": "郑州",
                "locationId": 410100
            },
            {
                "cityName": "南阳",
                "locationId": 411300
            },
            {
                "cityName": "驻马店",
                "locationId": 411700
            },
            {
                "cityName": "商丘",
                "locationId": 411400
            },
            {
                "cityName": "周口",
                "locationId": 411600
            },
            {
                "cityName": "平顶山",
                "locationId": 410400
            },
            {
                "cityName": "新乡",
                "locationId": 410700
            },
            {
                "cityName": "安阳",
                "locationId": 410500
            },
            {
                "cityName": "许昌",
                "locationId": 411000
            },
            {
                "cityName": "漯河",
                "locationId": 411100
            },
            {
                "cityName": "焦作",
                "locationId": 410800
            },
            {
                "cityName": "洛阳",
                "locationId": 410300
            },
            {
                "cityName": "开封",
                "locationId": 410200
            },
            {
                "cityName": "鹤壁",
                "locationId": 410600
            },
            {
                "cityName": "濮阳",
                "locationId": 410900
            },
            {
                "cityName": "三门峡",
                "locationId": 411200
            },
            {
                "cityName": "济源",
                "locationId": 419001
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            }
        ]
    },
    {
        "provinceName": "湖南省",
        "provinceShortName": "湖南",
        "locationId": 430000,
        "cities": [
            {
                "cityName": "长沙",
                "locationId": 430100
            },
            {
                "cityName": "岳阳",
                "locationId": 430600
            },
            {
                "cityName": "邵阳",
                "locationId": 430500
            },
            {
                "cityName": "常德",
                "locationId": 430700
            },
            {
                "cityName": "株洲",
                "locationId": 430200
            },
            {
                "cityName": "娄底",
                "locationId": 431300
            },
            {
                "cityName": "益阳",
                "locationId": 430900
            },
            {
                "cityName": "衡阳",
                "locationId": 430400
            },
            {
                "cityName": "永州",
                "locationId": 431100
            },
            {
                "cityName": "怀化",
                "locationId": 431200
            },
            {
                "cityName": "郴州",
                "locationId": 431000
            },
            {
                "cityName": "湘潭",
                "locationId": 430300
            },
            {
                "cityName": "湘西土家族苗族自治州",
                "locationId": 433100
            },
            {
                "cityName": "张家界",
                "locationId": 430800
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            }
        ]
    },
    {
        "provinceName": "安徽省",
        "provinceShortName": "安徽",
        "locationId": 340000,
        "cities": [
            {
                "cityName": "合肥",
                "locationId": 340100
            },
            {
                "cityName": "蚌埠",
                "locationId": 340300
            },
            {
                "cityName": "阜阳",
                "locationId": 341200
            },
            {
                "cityName": "亳州",
                "locationId": 341600
            },
            {
                "cityName": "安庆",
                "locationId": 340800
            },
            {
                "cityName": "六安",
                "locationId": 341500
            },
            {
                "cityName": "宿州",
                "locationId": 341300
            },
            {
                "cityName": "马鞍山",
                "locationId": 340500
            },
            {
                "cityName": "芜湖",
                "locationId": 340200
            },
            {
                "cityName": "铜陵",
                "locationId": 340700
            },
            {
                "cityName": "淮北",
                "locationId": 340600
            },
            {
                "cityName": "淮南",
                "locationId": 340400
            },
            {
                "cityName": "池州",
                "locationId": 341700
            },
            {
                "cityName": "滁州",
                "locationId": 341100
            },
            {
                "cityName": "黄山",
                "locationId": 341000
            },
            {
                "cityName": "宣城",
                "locationId": 341800
            }
        ]
    },
    {
        "provinceName": "黑龙江省",
        "provinceShortName": "黑龙江",
        "locationId": 230000,
        "cities": [
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "哈尔滨",
                "locationId": 230100
            },
            {
                "cityName": "双鸭山",
                "locationId": 230500
            },
            {
                "cityName": "绥化",
                "locationId": 231200
            },
            {
                "cityName": "鸡西",
                "locationId": 230300
            },
            {
                "cityName": "齐齐哈尔",
                "locationId": 230200
            },
            {
                "cityName": "大庆",
                "locationId": 230600
            },
            {
                "cityName": "牡丹江",
                "locationId": 231000
            },
            {
                "cityName": "七台河",
                "locationId": 230900
            },
            {
                "cityName": "佳木斯",
                "locationId": 230800
            },
            {
                "cityName": "黑河",
                "locationId": 231100
            },
            {
                "cityName": "鹤岗",
                "locationId": 230400
            },
            {
                "cityName": "大兴安岭地区",
                "locationId": 232700
            },
            {
                "cityName": "待明确",
                "locationId": 0
            },
            {
                "cityName": "伊春",
                "locationId": 230700
            }
        ]
    },
    {
        "provinceName": "江西省",
        "provinceShortName": "江西",
        "locationId": 360000,
        "cities": [
            {
                "cityName": "南昌",
                "locationId": 360100
            },
            {
                "cityName": "新余",
                "locationId": 360500
            },
            {
                "cityName": "上饶",
                "locationId": 361100
            },
            {
                "cityName": "九江",
                "locationId": 360400
            },
            {
                "cityName": "宜春",
                "locationId": 360900
            },
            {
                "cityName": "赣州",
                "locationId": 360700
            },
            {
                "cityName": "抚州",
                "locationId": 361000
            },
            {
                "cityName": "萍乡",
                "locationId": 360300
            },
            {
                "cityName": "吉安",
                "locationId": 360800
            },
            {
                "cityName": "鹰潭",
                "locationId": 360600
            },
            {
                "cityName": "景德镇",
                "locationId": 360200
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "赣江新区",
                "locationId": 0
            }
        ]
    },
    {
        "provinceName": "山东省",
        "provinceShortName": "山东",
        "locationId": 370000,
        "cities": [
            {
                "cityName": "济宁",
                "locationId": 370800
            },
            {
                "cityName": "青岛",
                "locationId": 370200
            },
            {
                "cityName": "临沂",
                "locationId": 371300
            },
            {
                "cityName": "济南",
                "locationId": 370100
            },
            {
                "cityName": "烟台",
                "locationId": 370600
            },
            {
                "cityName": "潍坊",
                "locationId": 370700
            },
            {
                "cityName": "威海",
                "locationId": 371000
            },
            {
                "cityName": "聊城",
                "locationId": 371500
            },
            {
                "cityName": "德州",
                "locationId": 371400
            },
            {
                "cityName": "泰安",
                "locationId": 370900
            },
            {
                "cityName": "淄博",
                "locationId": 370300
            },
            {
                "cityName": "东营",
                "locationId": 370500
            },
            {
                "cityName": "枣庄",
                "locationId": 370400
            },
            {
                "cityName": "菏泽",
                "locationId": 371700
            },
            {
                "cityName": "日照",
                "locationId": 371100
            },
            {
                "cityName": "滨州",
                "locationId": 371600
            },
            {
                "cityName": "莱芜",
                "locationId": 371200
            }
        ]
    },
    {
        "provinceName": "广西壮族自治区",
        "provinceShortName": "广西",
        "locationId": 450000,
        "cities": [
            {
                "cityName": "南宁",
                "locationId": 450100
            },
            {
                "cityName": "北海",
                "locationId": 450500
            },
            {
                "cityName": "桂林",
                "locationId": 450300
            },
            {
                "cityName": "河池",
                "locationId": 451200
            },
            {
                "cityName": "柳州",
                "locationId": 450200
            },
            {
                "cityName": "防城港",
                "locationId": 450600
            },
            {
                "cityName": "玉林",
                "locationId": 450900
            },
            {
                "cityName": "来宾",
                "locationId": 451300
            },
            {
                "cityName": "钦州",
                "locationId": 450700
            },
            {
                "cityName": "贵港",
                "locationId": 450800
            },
            {
                "cityName": "梧州",
                "locationId": 450400
            },
            {
                "cityName": "贺州",
                "locationId": 451100
            },
            {
                "cityName": "百色",
                "locationId": 451000
            },
            {
                "cityName": "崇左",
                "locationId": 451400
            }
        ]
    },
    {
        "provinceName": "内蒙古自治区",
        "provinceShortName": "内蒙古",
        "locationId": 150000,
        "cities": [
            {
                "cityName": "境外输入人员",
                "locationId": 0
            },
            {
                "cityName": "鄂尔多斯",
                "locationId": 150600
            },
            {
                "cityName": "包头",
                "locationId": 150200
            },
            {
                "cityName": "赤峰",
                "locationId": 150400
            },
            {
                "cityName": "锡林郭勒盟",
                "locationId": 152500
            },
            {
                "cityName": "呼伦贝尔",
                "locationId": 150700
            },
            {
                "cityName": "巴彦淖尔",
                "locationId": 150800
            },
            {
                "cityName": "呼和浩特",
                "locationId": 150100
            },
            {
                "cityName": "通辽",
                "locationId": 150500
            },
            {
                "cityName": "乌兰察布",
                "locationId": 150900
            },
            {
                "cityName": "乌海市",
                "locationId": 150300
            },
            {
                "cityName": "兴安盟",
                "locationId": 152200
            },
            {
                "cityName": "阿拉善盟",
                "locationId": 152900
            },
            {
                "cityName": "乌海市",
                "locationId": 150300
            }
        ]
    },
    {
        "provinceName": "山西省",
        "provinceShortName": "山西",
        "locationId": 140000,
        "cities": [
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "晋中",
                "locationId": 140700
            },
            {
                "cityName": "太原",
                "locationId": 140100
            },
            {
                "cityName": "运城",
                "locationId": 140800
            },
            {
                "cityName": "大同",
                "locationId": 140200
            },
            {
                "cityName": "晋城",
                "locationId": 140500
            },
            {
                "cityName": "长治",
                "locationId": 140400
            },
            {
                "cityName": "朔州",
                "locationId": 140600
            },
            {
                "cityName": "忻州",
                "locationId": 140900
            },
            {
                "cityName": "吕梁",
                "locationId": 141100
            },
            {
                "cityName": "阳泉",
                "locationId": 140300
            },
            {
                "cityName": "临汾",
                "locationId": 141000
            }
        ]
    },
    {
        "provinceName": "云南省",
        "provinceShortName": "云南",
        "locationId": 530000,
        "cities": [
            {
                "cityName": "昆明",
                "locationId": 530100
            },
            {
                "cityName": "昭通",
                "locationId": 530600
            },
            {
                "cityName": "西双版纳傣族自治州",
                "locationId": 532800
            },
            {
                "cityName": "玉溪",
                "locationId": 530400
            },
            {
                "cityName": "曲靖",
                "locationId": 530300
            },
            {
                "cityName": "大理白族自治州",
                "locationId": 532900
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            },
            {
                "cityName": "红河哈尼族彝族自治州",
                "locationId": 532500
            },
            {
                "cityName": "保山",
                "locationId": 530500
            },
            {
                "cityName": "丽江",
                "locationId": 530700
            },
            {
                "cityName": "德宏傣族景颇族自治州",
                "locationId": 533100
            },
            {
                "cityName": "普洱",
                "locationId": 530800
            },
            {
                "cityName": "楚雄彝族自治州",
                "locationId": 532300
            },
            {
                "cityName": "文山壮族苗族自治州",
                "locationId": 532600
            },
            {
                "cityName": "临沧",
                "locationId": 530900
            },
            {
                "cityName": "怒江傈僳族自治州",
                "locationId": 533300
            },
            {
                "cityName": "迪庆藏族自治州",
                "locationId": 533400
            }
        ]
    },
    {
        "provinceName": "海南省",
        "provinceShortName": "海南",
        "locationId": 460000,
        "cities": [
            {
                "cityName": "三亚",
                "locationId": 460200
            },
            {
                "cityName": "海口",
                "locationId": 460100
            },
            {
                "cityName": "三沙",
                "locationId": 460300
            },
            {
                "cityName": "儋州",
                "locationId": 460400
            },
            {
                "cityName": "万宁",
                "locationId": 469006
            },
            {
                "cityName": "澄迈县",
                "locationId": 469023
            },
            {
                "cityName": "昌江黎族自治县",
                "locationId": 469026
            },
            {
                "cityName": "琼海",
                "locationId": 469002
            },
            {
                "cityName": "临高县",
                "locationId": 469024
            },
            {
                "cityName": "陵水黎族自治县",
                "locationId": 469028
            },
            {
                "cityName": "定安县",
                "locationId": 469021
            },
            {
                "cityName": "文昌",
                "locationId": 469005
            },
            {
                "cityName": "东方",
                "locationId": 469007
            },
            {
                "cityName": "保亭黎族苗族自治县",
                "locationId": 469029
            },
            {
                "cityName": "乐东黎族自治县",
                "locationId": 469027
            },
            {
                "cityName": "琼中黎族苗族自治县",
                "locationId": 469030
            },
            {
                "cityName": "白沙黎族自治县",
                "locationId": 469025
            },
            {
                "cityName": "屯昌县",
                "locationId": 469022
            },
            {
                "cityName": "五指山",
                "locationId": 469001
            }
        ]
    },
    {
        "provinceName": "吉林省",
        "provinceShortName": "吉林",
        "locationId": 220000,
        "cities": [
            {
                "cityName": "吉林",
                "locationId": 220200
            },
            {
                "cityName": "长春",
                "locationId": 220100
            },
            {
                "cityName": "四平",
                "locationId": 220300
            },
            {
                "cityName": "辽源",
                "locationId": 220400
            },
            {
                "cityName": "延边",
                "locationId": 222400
            },
            {
                "cityName": "公主岭",
                "locationId": 220381
            },
            {
                "cityName": "通化",
                "locationId": 220500
            },
            {
                "cityName": "松原",
                "locationId": 220700
            },
            {
                "cityName": "梅河口",
                "locationId": 220581
            },
            {
                "cityName": "白城",
                "locationId": 220800
            },
            {
                "cityName": "白山",
                "locationId": 220600
            }
        ]
    },
    {
        "provinceName": "贵州省",
        "provinceShortName": "贵州",
        "locationId": 520000,
        "cities": [
            {
                "cityName": "贵阳",
                "locationId": 520100
            },
            {
                "cityName": "遵义",
                "locationId": 520300
            },
            {
                "cityName": "毕节",
                "locationId": 520500
            },
            {
                "cityName": "黔南布依族苗族自治州",
                "locationId": 522700
            },
            {
                "cityName": "六盘水",
                "locationId": 520200
            },
            {
                "cityName": "铜仁",
                "locationId": 520600
            },
            {
                "cityName": "黔东南苗族侗族自治州",
                "locationId": 522600
            },
            {
                "cityName": "安顺",
                "locationId": 520400
            },
            {
                "cityName": "黔西南布依族苗族自治州",
                "locationId": 522300
            },
            {
                "cityName": "境外输入",
                "locationId": 0
            }
        ]
    },
    {
        "provinceName": "新疆维吾尔自治区",
        "provinceShortName": "新疆",
        "locationId": 650000,
        "cities": [
            {
                "cityName": "乌鲁木齐",
                "locationId": 650100
            },
            {
                "cityName": "伊犁哈萨克自治州",
                "locationId": 654000
            },
            {
                "cityName": "克拉玛依",
                "locationId": 650200
            },
            {
                "cityName": "哈密",
                "locationId": 650500
            },
            {
                "cityName": "昌吉回族自治州",
                "locationId": 652300
            },
            {
                "cityName": "博尔塔拉蒙古自治州",
                "locationId": 652700
            },
            {
                "cityName": "吐鲁番",
                "locationId": 650400
            },
            {
                "cityName": "巴音郭楞蒙古自治州",
                "locationId": 652800
            },
            {
                "cityName": "克孜勒苏柯尔克孜自治州",
                "locationId": 653000
            },
            {
                "cityName": "喀什地区",
                "locationId": 653100
            },
            {
                "cityName": "和田地区",
                "locationId": 653200
            },
            {
                "cityName": "阿克苏地区",
                "locationId": 652900
            },
            {
                "cityName": "塔城地区",
                "locationId": 654200
            },
            {
                "cityName": "阿勒泰地区",
                "locationId": 654300
            },
            {
                "cityName": "直辖县级政区",
                "locationId": 659000
            }
        ]
    },
    {
        "provinceName": "宁夏回族自治区",
        "provinceShortName": "宁夏",
        "locationId": 640000,
        "cities": [
            {
                "cityName": "银川",
                "locationId": 640100
            },
            {
                "cityName": "吴忠",
                "locationId": 640300
            },
            {
                "cityName": "固原",
                "locationId": 640400
            },
            {
                "cityName": "中卫",
                "locationId": 640500
            },
            {
                "cityName": "宁东",
                "locationId": 0
            },
            {
                "cityName": "石嘴山",
                "locationId": 640200
            }
        ]
    },
    {
        "provinceName": "青海省",
        "provinceShortName": "青海",
        "locationId": 630000,
        "cities": [
            {
                "cityName": "西宁",
                "locationId": 630100
            },
            {
                "cityName": "海北藏族自治州",
                "locationId": 632200
            },
            {
                "cityName": "海东",
                "locationId": 630200
            },
            {
                "cityName": "黄南藏族自治州",
                "locationId": 632300
            },
            {
                "cityName": "海南藏族自治州",
                "locationId": 632500
            },
            {
                "cityName": "果洛藏族自治州",
                "locationId": 632600
            },
            {
                "cityName": "玉树藏族自治州",
                "locationId": 632700
            },
            {
                "cityName": "海西蒙古族藏族自治州",
                "locationId": 632800
            }
        ]
    },
    {
        "provinceName": "西藏自治区",
        "provinceShortName": "西藏",
        "locationId": 540000,
        "cities": [
            {
                "cityName": "拉萨",
                "locationId": 540100
            },
            {
                "cityName": "日喀则",
                "locationId": 540200
            },
            {
                "cityName": "昌都",
                "locationId": 540300
            },
            {
                "cityName": "昌都地区",
                "locationId": 54030000
            },
            {
                "cityName": "林芝",
                "locationId": 540400
            },
            {
                "cityName": "山南",
                "locationId": 540500
            },
            {
                "cityName": "那曲地区",
                "locationId": 540600
            },
            {
                "cityName": "阿里地区",
                "locationId": 54250000
            }
        ]
    }
]


def save(append_result):
    main_city = [
        {
            "provinceName": "北京市",
            "provinceShortName": "北京",
            "locationId": 110000,
            "cities": [
                {
                    "cityName": "丰台区",
                    "locationId": 110106
                },
                {
                    "cityName": "大兴区",
                    "locationId": 110115
                },
                {
                    "cityName": "海淀区",
                    "locationId": 110108
                },
                {
                    "cityName": "朝阳区",
                    "locationId": 110105
                },
                {
                    "cityName": "西城区",
                    "locationId": 110102
                },
                {
                    "cityName": "昌平区",
                    "locationId": 110114
                },
                {
                    "cityName": "通州区",
                    "locationId": 110112
                },
                {
                    "cityName": "东城区",
                    "locationId": 110101
                },
                {
                    "cityName": "房山区",
                    "locationId": 110111
                },
                {
                    "cityName": "怀柔区",
                    "locationId": 110116
                },
                {
                    "cityName": "密云区",
                    "locationId": 110118
                },
                {
                    "cityName": "石景山区",
                    "locationId": 110107
                },
                {
                    "cityName": "门头沟区",
                    "locationId": 110109
                },
                {
                    "cityName": "延庆区",
                    "locationId": 110119
                },
                {
                    "cityName": "顺义区",
                    "locationId": 110113
                },
                {
                    "cityName": "平谷区",
                    "locationId": 110117
                }
            ]
        },
        {
            "provinceName": "香港",
            "provinceShortName": "香港",
            "locationId": 810000,
            "cities": []
        },
        {
            "provinceName": "上海市",
            "provinceShortName": "上海",
            "locationId": 310000,
            "cities": [
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "境外来沪",
                    "locationId": 0
                },
                {
                    "cityName": "外地来沪",
                    "locationId": 0
                },
                {
                    "cityName": "浦东新区",
                    "locationId": 310115
                },
                {
                    "cityName": "宝山区",
                    "locationId": 310113
                },
                {
                    "cityName": "闵行区",
                    "locationId": 310112
                },
                {
                    "cityName": "徐汇区",
                    "locationId": 310104
                },
                {
                    "cityName": "静安区",
                    "locationId": 310106
                },
                {
                    "cityName": "松江区",
                    "locationId": 310117
                },
                {
                    "cityName": "长宁区",
                    "locationId": 310105
                },
                {
                    "cityName": "普陀区",
                    "locationId": 310107
                },
                {
                    "cityName": "杨浦区",
                    "locationId": 310110
                },
                {
                    "cityName": "嘉定区",
                    "locationId": 310114
                },
                {
                    "cityName": "奉贤区",
                    "locationId": 310120
                },
                {
                    "cityName": "虹口区",
                    "locationId": 310109
                },
                {
                    "cityName": "黄浦区",
                    "locationId": 310101
                },
                {
                    "cityName": "青浦区",
                    "locationId": 310118
                },
                {
                    "cityName": "金山区",
                    "locationId": 310116
                },
                {
                    "cityName": "崇明区",
                    "locationId": 310151
                }
            ]
        },
        {
            "provinceName": "甘肃省",
            "provinceShortName": "甘肃",
            "locationId": 620000,
            "cities": [
                {
                    "cityName": "酒泉",
                    "locationId": 620900
                },
                {
                    "cityName": "兰州",
                    "locationId": 620100
                },
                {
                    "cityName": "天水",
                    "locationId": 620500
                },
                {
                    "cityName": "平凉",
                    "locationId": 620800
                },
                {
                    "cityName": "定西",
                    "locationId": 621100
                },
                {
                    "cityName": "甘南",
                    "locationId": 623000
                },
                {
                    "cityName": "白银",
                    "locationId": 620400
                },
                {
                    "cityName": "陇南",
                    "locationId": 621200
                },
                {
                    "cityName": "庆阳",
                    "locationId": 621000
                },
                {
                    "cityName": "临夏",
                    "locationId": 622900
                },
                {
                    "cityName": "张掖",
                    "locationId": 620700
                },
                {
                    "cityName": "金昌",
                    "locationId": 620300
                },
                {
                    "cityName": "武威",
                    "locationId": 620600
                },
                {
                    "cityName": "临夏回族自治州",
                    "locationId": 622900
                },
                {
                    "cityName": "甘南藏族自治州",
                    "locationId": 623000
                }
            ]
        },
        {
            "provinceName": "四川省",
            "provinceShortName": "四川",
            "locationId": 510000,
            "cities": [
                {
                    "cityName": "成都",
                    "locationId": 510100
                },
                {
                    "cityName": "雅安",
                    "locationId": 511800
                },
                {
                    "cityName": "甘孜藏族自治州",
                    "locationId": 513300
                },
                {
                    "cityName": "达州",
                    "locationId": 511700
                },
                {
                    "cityName": "南充",
                    "locationId": 511300
                },
                {
                    "cityName": "广安",
                    "locationId": 511600
                },
                {
                    "cityName": "泸州",
                    "locationId": 510500
                },
                {
                    "cityName": "巴中",
                    "locationId": 511900
                },
                {
                    "cityName": "绵阳",
                    "locationId": 510700
                },
                {
                    "cityName": "内江",
                    "locationId": 511000
                },
                {
                    "cityName": "德阳",
                    "locationId": 510600
                },
                {
                    "cityName": "遂宁",
                    "locationId": 510900
                },
                {
                    "cityName": "攀枝花",
                    "locationId": 510400
                },
                {
                    "cityName": "凉山彝族自治州",
                    "locationId": 513400
                },
                {
                    "cityName": "宜宾",
                    "locationId": 511500
                },
                {
                    "cityName": "自贡",
                    "locationId": 510300
                },
                {
                    "cityName": "眉山",
                    "locationId": 511400
                },
                {
                    "cityName": "广元",
                    "locationId": 510800
                },
                {
                    "cityName": "资阳",
                    "locationId": 512000
                },
                {
                    "cityName": "乐山",
                    "locationId": 511100
                },
                {
                    "cityName": "阿坝藏族羌族自治州",
                    "locationId": 513200
                }
            ]
        },
        {
            "provinceName": "河北省",
            "provinceShortName": "河北",
            "locationId": 130000,
            "cities": [
                {
                    "cityName": "保定",
                    "locationId": 130600
                },
                {
                    "cityName": "张家口",
                    "locationId": 130700
                },
                {
                    "cityName": "廊坊",
                    "locationId": 131000
                },
                {
                    "cityName": "沧州",
                    "locationId": 130900
                },
                {
                    "cityName": "唐山",
                    "locationId": 130200
                },
                {
                    "cityName": "邯郸",
                    "locationId": 130400
                },
                {
                    "cityName": "石家庄",
                    "locationId": 130100
                },
                {
                    "cityName": "邢台",
                    "locationId": 130500
                },
                {
                    "cityName": "秦皇岛",
                    "locationId": 130300
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "衡水",
                    "locationId": 131100
                },
                {
                    "cityName": "承德",
                    "locationId": 130800
                },
                {
                    "cityName": "待明确",
                    "locationId": 0
                }
            ]
        },
        {
            "provinceName": "广东省",
            "provinceShortName": "广东",
            "locationId": 440000,
            "cities": [
                {
                    "cityName": "广州",
                    "locationId": 440100
                },
                {
                    "cityName": "深圳",
                    "locationId": 440300
                },
                {
                    "cityName": "珠海",
                    "locationId": 440400
                },
                {
                    "cityName": "东莞",
                    "locationId": 441900
                },
                {
                    "cityName": "佛山",
                    "locationId": 440600
                },
                {
                    "cityName": "中山",
                    "locationId": 442000
                },
                {
                    "cityName": "惠州",
                    "locationId": 441300
                },
                {
                    "cityName": "汕头",
                    "locationId": 440500
                },
                {
                    "cityName": "江门",
                    "locationId": 440700
                },
                {
                    "cityName": "湛江",
                    "locationId": 440800
                },
                {
                    "cityName": "肇庆",
                    "locationId": 441200
                },
                {
                    "cityName": "梅州",
                    "locationId": 441400
                },
                {
                    "cityName": "阳江",
                    "locationId": 441700
                },
                {
                    "cityName": "茂名",
                    "locationId": 440900
                },
                {
                    "cityName": "清远",
                    "locationId": 441800
                },
                {
                    "cityName": "揭阳",
                    "locationId": 445200
                },
                {
                    "cityName": "韶关",
                    "locationId": 440200
                },
                {
                    "cityName": "潮州",
                    "locationId": 445100
                },
                {
                    "cityName": "汕尾",
                    "locationId": 441500
                },
                {
                    "cityName": "河源",
                    "locationId": 441600
                },
                {
                    "cityName": "云浮",
                    "locationId": 445300
                }
            ]
        },
        {
            "provinceName": "陕西省",
            "provinceShortName": "陕西",
            "locationId": 610000,
            "cities": [
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "西安",
                    "locationId": 610100
                },
                {
                    "cityName": "安康",
                    "locationId": 610900
                },
                {
                    "cityName": "汉中",
                    "locationId": 610700
                },
                {
                    "cityName": "咸阳",
                    "locationId": 610400
                },
                {
                    "cityName": "渭南",
                    "locationId": 610500
                },
                {
                    "cityName": "宝鸡",
                    "locationId": 610300
                },
                {
                    "cityName": "延安",
                    "locationId": 610600
                },
                {
                    "cityName": "铜川",
                    "locationId": 610200
                },
                {
                    "cityName": "商洛",
                    "locationId": 611000
                },
                {
                    "cityName": "榆林",
                    "locationId": 610800
                },
                {
                    "cityName": "韩城",
                    "locationId": 610581
                },
                {
                    "cityName": "杨凌",
                    "locationId": 0
                }
            ]
        },
        {
            "provinceName": "辽宁省",
            "provinceShortName": "辽宁",
            "locationId": 210000,
            "cities": [
                {
                    "cityName": "沈阳",
                    "locationId": 210100
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "大连",
                    "locationId": 210200
                },
                {
                    "cityName": "锦州",
                    "locationId": 210700
                },
                {
                    "cityName": "葫芦岛",
                    "locationId": 211400
                },
                {
                    "cityName": "丹东",
                    "locationId": 210600
                },
                {
                    "cityName": "盘锦",
                    "locationId": 211100
                },
                {
                    "cityName": "阜新",
                    "locationId": 210900
                },
                {
                    "cityName": "铁岭",
                    "locationId": 211200
                },
                {
                    "cityName": "朝阳",
                    "locationId": 211300
                },
                {
                    "cityName": "鞍山",
                    "locationId": 210300
                },
                {
                    "cityName": "本溪",
                    "locationId": 210500
                },
                {
                    "cityName": "辽阳",
                    "locationId": 211000
                },
                {
                    "cityName": "营口",
                    "locationId": 210800
                },
                {
                    "cityName": "抚顺",
                    "locationId": 210400
                }
            ]
        },
        {
            "provinceName": "重庆市",
            "provinceShortName": "重庆",
            "locationId": 500000,
            "cities": [
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "万州区",
                    "locationId": 500101
                },
                {
                    "cityName": "江北区",
                    "locationId": 500105
                },
                {
                    "cityName": "云阳县",
                    "locationId": 500235
                },
                {
                    "cityName": "合川区",
                    "locationId": 500117
                },
                {
                    "cityName": "綦江区",
                    "locationId": 500110
                },
                {
                    "cityName": "长寿区",
                    "locationId": 500115
                },
                {
                    "cityName": "奉节县",
                    "locationId": 500236
                },
                {
                    "cityName": "九龙坡区",
                    "locationId": 500107
                },
                {
                    "cityName": "开州区",
                    "locationId": 500154
                },
                {
                    "cityName": "忠县",
                    "locationId": 500233
                },
                {
                    "cityName": "渝中区",
                    "locationId": 500103
                },
                {
                    "cityName": "垫江县",
                    "locationId": 500231
                },
                {
                    "cityName": "潼南区",
                    "locationId": 500152
                },
                {
                    "cityName": "渝北区",
                    "locationId": 500112
                },
                {
                    "cityName": "两江新区",
                    "locationId": -1
                },
                {
                    "cityName": "南岸区",
                    "locationId": 500108
                },
                {
                    "cityName": "石柱土家族自治县",
                    "locationId": 500240
                },
                {
                    "cityName": "大足区",
                    "locationId": 500111
                },
                {
                    "cityName": "巫溪县",
                    "locationId": 500238
                },
                {
                    "cityName": "铜梁区",
                    "locationId": 500151
                },
                {
                    "cityName": "丰都县",
                    "locationId": 500230
                },
                {
                    "cityName": "巫山县",
                    "locationId": 500237
                },
                {
                    "cityName": "沙坪坝区",
                    "locationId": 500106
                },
                {
                    "cityName": "璧山区",
                    "locationId": 500120
                },
                {
                    "cityName": "荣昌区",
                    "locationId": 500153
                },
                {
                    "cityName": "大渡口区",
                    "locationId": 500104
                },
                {
                    "cityName": "巴南区",
                    "locationId": 500113
                },
                {
                    "cityName": "涪陵区",
                    "locationId": 500102
                },
                {
                    "cityName": "永川区",
                    "locationId": 500118
                },
                {
                    "cityName": "江津区",
                    "locationId": 500116
                },
                {
                    "cityName": "梁平县",
                    "locationId": 500155
                },
                {
                    "cityName": "高新区",
                    "locationId": 0
                },
                {
                    "cityName": "黔江区",
                    "locationId": 500114
                },
                {
                    "cityName": "城口县",
                    "locationId": 500229
                },
                {
                    "cityName": "彭水苗族土家族自治县",
                    "locationId": 500243
                },
                {
                    "cityName": "武隆县",
                    "locationId": 500156
                },
                {
                    "cityName": "南川区",
                    "locationId": 500119
                },
                {
                    "cityName": "秀山土家族苗族自治县",
                    "locationId": 500241
                },
                {
                    "cityName": "酉阳土家族苗族自治县",
                    "locationId": 0
                },
                {
                    "cityName": "万盛经开区",
                    "locationId": 0
                }
            ]
        },
        {
            "provinceName": "台湾",
            "provinceShortName": "台湾",
            "locationId": 710000,
            "cities": []
        },
        {
            "provinceName": "福建省",
            "provinceShortName": "福建",
            "locationId": 350000,
            "cities": [
                {
                    "cityName": "境外输入人员",
                    "locationId": 0
                },
                {
                    "cityName": "福州",
                    "locationId": 350100
                },
                {
                    "cityName": "莆田",
                    "locationId": 350300
                },
                {
                    "cityName": "泉州",
                    "locationId": 350500
                },
                {
                    "cityName": "厦门",
                    "locationId": 350200
                },
                {
                    "cityName": "宁德",
                    "locationId": 350900
                },
                {
                    "cityName": "漳州",
                    "locationId": 350600
                },
                {
                    "cityName": "南平",
                    "locationId": 350700
                },
                {
                    "cityName": "三明",
                    "locationId": 350400
                },
                {
                    "cityName": "龙岩",
                    "locationId": 350800
                }
            ]
        },
        {
            "provinceName": "浙江省",
            "provinceShortName": "浙江",
            "locationId": 330000,
            "cities": [
                {
                    "cityName": "台州",
                    "locationId": 331000
                },
                {
                    "cityName": "温州",
                    "locationId": 330300
                },
                {
                    "cityName": "杭州",
                    "locationId": 330100
                },
                {
                    "cityName": "宁波",
                    "locationId": 330200
                },
                {
                    "cityName": "金华",
                    "locationId": 330700
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "嘉兴",
                    "locationId": 330400
                },
                {
                    "cityName": "绍兴",
                    "locationId": 330600
                },
                {
                    "cityName": "省十里丰监狱",
                    "locationId": 0
                },
                {
                    "cityName": "丽水",
                    "locationId": 331100
                },
                {
                    "cityName": "衢州",
                    "locationId": 330800
                },
                {
                    "cityName": "湖州",
                    "locationId": 330500
                },
                {
                    "cityName": "舟山",
                    "locationId": 330900
                }
            ]
        },
        {
            "provinceName": "江苏省",
            "provinceShortName": "江苏",
            "locationId": 320000,
            "cities": [
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "南京",
                    "locationId": 320100
                },
                {
                    "cityName": "苏州",
                    "locationId": 320500
                },
                {
                    "cityName": "徐州",
                    "locationId": 320300
                },
                {
                    "cityName": "淮安",
                    "locationId": 320800
                },
                {
                    "cityName": "无锡",
                    "locationId": 320200
                },
                {
                    "cityName": "常州",
                    "locationId": 320400
                },
                {
                    "cityName": "连云港",
                    "locationId": 320700
                },
                {
                    "cityName": "南通",
                    "locationId": 320600
                },
                {
                    "cityName": "泰州",
                    "locationId": 321200
                },
                {
                    "cityName": "盐城",
                    "locationId": 320900
                },
                {
                    "cityName": "扬州",
                    "locationId": 321000
                },
                {
                    "cityName": "宿迁",
                    "locationId": 321300
                },
                {
                    "cityName": "镇江",
                    "locationId": 321100
                }
            ]
        },
        {
            "provinceName": "天津市",
            "provinceShortName": "天津",
            "locationId": 120000,
            "cities": [
                {
                    "cityName": "北辰区",
                    "locationId": 120113
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "宝坻区",
                    "locationId": 120115
                },
                {
                    "cityName": "河东区",
                    "locationId": 120102
                },
                {
                    "cityName": "河北区",
                    "locationId": 120105
                },
                {
                    "cityName": "南开区",
                    "locationId": 120104
                },
                {
                    "cityName": "和平区",
                    "locationId": 120101
                },
                {
                    "cityName": "外地来津",
                    "locationId": -1
                },
                {
                    "cityName": "东丽区",
                    "locationId": 120110
                },
                {
                    "cityName": "宁河区",
                    "locationId": 120117
                },
                {
                    "cityName": "河西区",
                    "locationId": 120103
                },
                {
                    "cityName": "西青区",
                    "locationId": 120111
                },
                {
                    "cityName": "滨海新区",
                    "locationId": 120116
                },
                {
                    "cityName": "武清区",
                    "locationId": 120114
                },
                {
                    "cityName": "红桥区",
                    "locationId": 120106
                },
                {
                    "cityName": "津南区",
                    "locationId": 120112
                },
                {
                    "cityName": "静海区",
                    "locationId": 120118
                }
            ]
        },
        {
            "provinceName": "澳门",
            "provinceShortName": "澳门",
            "locationId": 820000,
            "cities": []
        },
        {
            "provinceName": "湖北省",
            "provinceShortName": "湖北",
            "locationId": 420000,
            "cities": [
                {
                    "cityName": "武汉",
                    "locationId": 420100
                },
                {
                    "cityName": "孝感",
                    "locationId": 420900
                },
                {
                    "cityName": "黄冈",
                    "locationId": 421100
                },
                {
                    "cityName": "荆州",
                    "locationId": 421000
                },
                {
                    "cityName": "鄂州",
                    "locationId": 420700
                },
                {
                    "cityName": "随州",
                    "locationId": 421300
                },
                {
                    "cityName": "襄阳",
                    "locationId": 420600
                },
                {
                    "cityName": "黄石",
                    "locationId": 420200
                },
                {
                    "cityName": "宜昌",
                    "locationId": 420500
                },
                {
                    "cityName": "荆门",
                    "locationId": 420800
                },
                {
                    "cityName": "咸宁",
                    "locationId": 421200
                },
                {
                    "cityName": "十堰",
                    "locationId": 420300
                },
                {
                    "cityName": "仙桃",
                    "locationId": 429004
                },
                {
                    "cityName": "天门",
                    "locationId": 429006
                },
                {
                    "cityName": "恩施州",
                    "locationId": 422800
                },
                {
                    "cityName": "潜江",
                    "locationId": 429005
                },
                {
                    "cityName": "神农架林区",
                    "locationId": 429021
                }
            ]
        },
        {
            "provinceName": "河南省",
            "provinceShortName": "河南",
            "locationId": 410000,
            "cities": [
                {
                    "cityName": "信阳",
                    "locationId": 411500
                },
                {
                    "cityName": "郑州",
                    "locationId": 410100
                },
                {
                    "cityName": "南阳",
                    "locationId": 411300
                },
                {
                    "cityName": "驻马店",
                    "locationId": 411700
                },
                {
                    "cityName": "商丘",
                    "locationId": 411400
                },
                {
                    "cityName": "周口",
                    "locationId": 411600
                },
                {
                    "cityName": "平顶山",
                    "locationId": 410400
                },
                {
                    "cityName": "新乡",
                    "locationId": 410700
                },
                {
                    "cityName": "安阳",
                    "locationId": 410500
                },
                {
                    "cityName": "许昌",
                    "locationId": 411000
                },
                {
                    "cityName": "漯河",
                    "locationId": 411100
                },
                {
                    "cityName": "焦作",
                    "locationId": 410800
                },
                {
                    "cityName": "洛阳",
                    "locationId": 410300
                },
                {
                    "cityName": "开封",
                    "locationId": 410200
                },
                {
                    "cityName": "鹤壁",
                    "locationId": 410600
                },
                {
                    "cityName": "濮阳",
                    "locationId": 410900
                },
                {
                    "cityName": "三门峡",
                    "locationId": 411200
                },
                {
                    "cityName": "济源",
                    "locationId": 419001
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                }
            ]
        },
        {
            "provinceName": "湖南省",
            "provinceShortName": "湖南",
            "locationId": 430000,
            "cities": [
                {
                    "cityName": "长沙",
                    "locationId": 430100
                },
                {
                    "cityName": "岳阳",
                    "locationId": 430600
                },
                {
                    "cityName": "邵阳",
                    "locationId": 430500
                },
                {
                    "cityName": "常德",
                    "locationId": 430700
                },
                {
                    "cityName": "株洲",
                    "locationId": 430200
                },
                {
                    "cityName": "娄底",
                    "locationId": 431300
                },
                {
                    "cityName": "益阳",
                    "locationId": 430900
                },
                {
                    "cityName": "衡阳",
                    "locationId": 430400
                },
                {
                    "cityName": "永州",
                    "locationId": 431100
                },
                {
                    "cityName": "怀化",
                    "locationId": 431200
                },
                {
                    "cityName": "郴州",
                    "locationId": 431000
                },
                {
                    "cityName": "湘潭",
                    "locationId": 430300
                },
                {
                    "cityName": "湘西土家族苗族自治州",
                    "locationId": 433100
                },
                {
                    "cityName": "张家界",
                    "locationId": 430800
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                }
            ]
        },
        {
            "provinceName": "安徽省",
            "provinceShortName": "安徽",
            "locationId": 340000,
            "cities": [
                {
                    "cityName": "合肥",
                    "locationId": 340100
                },
                {
                    "cityName": "蚌埠",
                    "locationId": 340300
                },
                {
                    "cityName": "阜阳",
                    "locationId": 341200
                },
                {
                    "cityName": "亳州",
                    "locationId": 341600
                },
                {
                    "cityName": "安庆",
                    "locationId": 340800
                },
                {
                    "cityName": "六安",
                    "locationId": 341500
                },
                {
                    "cityName": "宿州",
                    "locationId": 341300
                },
                {
                    "cityName": "马鞍山",
                    "locationId": 340500
                },
                {
                    "cityName": "芜湖",
                    "locationId": 340200
                },
                {
                    "cityName": "铜陵",
                    "locationId": 340700
                },
                {
                    "cityName": "淮北",
                    "locationId": 340600
                },
                {
                    "cityName": "淮南",
                    "locationId": 340400
                },
                {
                    "cityName": "池州",
                    "locationId": 341700
                },
                {
                    "cityName": "滁州",
                    "locationId": 341100
                },
                {
                    "cityName": "黄山",
                    "locationId": 341000
                },
                {
                    "cityName": "宣城",
                    "locationId": 341800
                }
            ]
        },
        {
            "provinceName": "黑龙江省",
            "provinceShortName": "黑龙江",
            "locationId": 230000,
            "cities": [
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "哈尔滨",
                    "locationId": 230100
                },
                {
                    "cityName": "双鸭山",
                    "locationId": 230500
                },
                {
                    "cityName": "绥化",
                    "locationId": 231200
                },
                {
                    "cityName": "鸡西",
                    "locationId": 230300
                },
                {
                    "cityName": "齐齐哈尔",
                    "locationId": 230200
                },
                {
                    "cityName": "大庆",
                    "locationId": 230600
                },
                {
                    "cityName": "牡丹江",
                    "locationId": 231000
                },
                {
                    "cityName": "七台河",
                    "locationId": 230900
                },
                {
                    "cityName": "佳木斯",
                    "locationId": 230800
                },
                {
                    "cityName": "黑河",
                    "locationId": 231100
                },
                {
                    "cityName": "鹤岗",
                    "locationId": 230400
                },
                {
                    "cityName": "大兴安岭地区",
                    "locationId": 232700
                },
                {
                    "cityName": "待明确",
                    "locationId": 0
                },
                {
                    "cityName": "伊春",
                    "locationId": 230700
                }
            ]
        },
        {
            "provinceName": "江西省",
            "provinceShortName": "江西",
            "locationId": 360000,
            "cities": [
                {
                    "cityName": "南昌",
                    "locationId": 360100
                },
                {
                    "cityName": "新余",
                    "locationId": 360500
                },
                {
                    "cityName": "上饶",
                    "locationId": 361100
                },
                {
                    "cityName": "九江",
                    "locationId": 360400
                },
                {
                    "cityName": "宜春",
                    "locationId": 360900
                },
                {
                    "cityName": "赣州",
                    "locationId": 360700
                },
                {
                    "cityName": "抚州",
                    "locationId": 361000
                },
                {
                    "cityName": "萍乡",
                    "locationId": 360300
                },
                {
                    "cityName": "吉安",
                    "locationId": 360800
                },
                {
                    "cityName": "鹰潭",
                    "locationId": 360600
                },
                {
                    "cityName": "景德镇",
                    "locationId": 360200
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "赣江新区",
                    "locationId": 0
                }
            ]
        },
        {
            "provinceName": "山东省",
            "provinceShortName": "山东",
            "locationId": 370000,
            "cities": [
                {
                    "cityName": "济宁",
                    "locationId": 370800
                },
                {
                    "cityName": "青岛",
                    "locationId": 370200
                },
                {
                    "cityName": "临沂",
                    "locationId": 371300
                },
                {
                    "cityName": "济南",
                    "locationId": 370100
                },
                {
                    "cityName": "烟台",
                    "locationId": 370600
                },
                {
                    "cityName": "潍坊",
                    "locationId": 370700
                },
                {
                    "cityName": "威海",
                    "locationId": 371000
                },
                {
                    "cityName": "聊城",
                    "locationId": 371500
                },
                {
                    "cityName": "德州",
                    "locationId": 371400
                },
                {
                    "cityName": "泰安",
                    "locationId": 370900
                },
                {
                    "cityName": "淄博",
                    "locationId": 370300
                },
                {
                    "cityName": "东营",
                    "locationId": 370500
                },
                {
                    "cityName": "枣庄",
                    "locationId": 370400
                },
                {
                    "cityName": "菏泽",
                    "locationId": 371700
                },
                {
                    "cityName": "日照",
                    "locationId": 371100
                },
                {
                    "cityName": "滨州",
                    "locationId": 371600
                },
                {
                    "cityName": "莱芜",
                    "locationId": 371200
                }
            ]
        },
        {
            "provinceName": "广西壮族自治区",
            "provinceShortName": "广西",
            "locationId": 450000,
            "cities": [
                {
                    "cityName": "南宁",
                    "locationId": 450100
                },
                {
                    "cityName": "北海",
                    "locationId": 450500
                },
                {
                    "cityName": "桂林",
                    "locationId": 450300
                },
                {
                    "cityName": "河池",
                    "locationId": 451200
                },
                {
                    "cityName": "柳州",
                    "locationId": 450200
                },
                {
                    "cityName": "防城港",
                    "locationId": 450600
                },
                {
                    "cityName": "玉林",
                    "locationId": 450900
                },
                {
                    "cityName": "来宾",
                    "locationId": 451300
                },
                {
                    "cityName": "钦州",
                    "locationId": 450700
                },
                {
                    "cityName": "贵港",
                    "locationId": 450800
                },
                {
                    "cityName": "梧州",
                    "locationId": 450400
                },
                {
                    "cityName": "贺州",
                    "locationId": 451100
                },
                {
                    "cityName": "百色",
                    "locationId": 451000
                },
                {
                    "cityName": "崇左",
                    "locationId": 451400
                }
            ]
        },
        {
            "provinceName": "内蒙古自治区",
            "provinceShortName": "内蒙古",
            "locationId": 150000,
            "cities": [
                {
                    "cityName": "境外输入人员",
                    "locationId": 0
                },
                {
                    "cityName": "鄂尔多斯",
                    "locationId": 150600
                },
                {
                    "cityName": "包头",
                    "locationId": 150200
                },
                {
                    "cityName": "赤峰",
                    "locationId": 150400
                },
                {
                    "cityName": "锡林郭勒盟",
                    "locationId": 152500
                },
                {
                    "cityName": "呼伦贝尔",
                    "locationId": 150700
                },
                {
                    "cityName": "巴彦淖尔",
                    "locationId": 150800
                },
                {
                    "cityName": "呼和浩特",
                    "locationId": 150100
                },
                {
                    "cityName": "通辽",
                    "locationId": 150500
                },
                {
                    "cityName": "乌兰察布",
                    "locationId": 150900
                },
                {
                    "cityName": "乌海市",
                    "locationId": 150300
                },
                {
                    "cityName": "兴安盟",
                    "locationId": 152200
                },
                {
                    "cityName": "阿拉善盟",
                    "locationId": 152900
                },
                {
                    "cityName": "乌海市",
                    "locationId": 150300
                }
            ]
        },
        {
            "provinceName": "山西省",
            "provinceShortName": "山西",
            "locationId": 140000,
            "cities": [
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "晋中",
                    "locationId": 140700
                },
                {
                    "cityName": "太原",
                    "locationId": 140100
                },
                {
                    "cityName": "运城",
                    "locationId": 140800
                },
                {
                    "cityName": "大同",
                    "locationId": 140200
                },
                {
                    "cityName": "晋城",
                    "locationId": 140500
                },
                {
                    "cityName": "长治",
                    "locationId": 140400
                },
                {
                    "cityName": "朔州",
                    "locationId": 140600
                },
                {
                    "cityName": "忻州",
                    "locationId": 140900
                },
                {
                    "cityName": "吕梁",
                    "locationId": 141100
                },
                {
                    "cityName": "阳泉",
                    "locationId": 140300
                },
                {
                    "cityName": "临汾",
                    "locationId": 141000
                }
            ]
        },
        {
            "provinceName": "云南省",
            "provinceShortName": "云南",
            "locationId": 530000,
            "cities": [
                {
                    "cityName": "昆明",
                    "locationId": 530100
                },
                {
                    "cityName": "昭通",
                    "locationId": 530600
                },
                {
                    "cityName": "西双版纳傣族自治州",
                    "locationId": 532800
                },
                {
                    "cityName": "玉溪",
                    "locationId": 530400
                },
                {
                    "cityName": "曲靖",
                    "locationId": 530300
                },
                {
                    "cityName": "大理白族自治州",
                    "locationId": 532900
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                },
                {
                    "cityName": "红河哈尼族彝族自治州",
                    "locationId": 532500
                },
                {
                    "cityName": "保山",
                    "locationId": 530500
                },
                {
                    "cityName": "丽江",
                    "locationId": 530700
                },
                {
                    "cityName": "德宏傣族景颇族自治州",
                    "locationId": 533100
                },
                {
                    "cityName": "普洱",
                    "locationId": 530800
                },
                {
                    "cityName": "楚雄彝族自治州",
                    "locationId": 532300
                },
                {
                    "cityName": "文山壮族苗族自治州",
                    "locationId": 532600
                },
                {
                    "cityName": "临沧",
                    "locationId": 530900
                },
                {
                    "cityName": "怒江傈僳族自治州",
                    "locationId": 533300
                },
                {
                    "cityName": "迪庆藏族自治州",
                    "locationId": 533400
                }
            ]
        },
        {
            "provinceName": "海南省",
            "provinceShortName": "海南",
            "locationId": 460000,
            "cities": [
                {
                    "cityName": "三亚",
                    "locationId": 460200
                },
                {
                    "cityName": "海口",
                    "locationId": 460100
                },
                {
                    "cityName": "三沙",
                    "locationId": 460300
                },
                {
                    "cityName": "儋州",
                    "locationId": 460400
                },
                {
                    "cityName": "万宁",
                    "locationId": 469006
                },
                {
                    "cityName": "澄迈县",
                    "locationId": 469023
                },
                {
                    "cityName": "昌江黎族自治县",
                    "locationId": 469026
                },
                {
                    "cityName": "琼海",
                    "locationId": 469002
                },
                {
                    "cityName": "临高县",
                    "locationId": 469024
                },
                {
                    "cityName": "陵水黎族自治县",
                    "locationId": 469028
                },
                {
                    "cityName": "定安县",
                    "locationId": 469021
                },
                {
                    "cityName": "文昌",
                    "locationId": 469005
                },
                {
                    "cityName": "东方",
                    "locationId": 469007
                },
                {
                    "cityName": "保亭黎族苗族自治县",
                    "locationId": 469029
                },
                {
                    "cityName": "乐东黎族自治县",
                    "locationId": 469027
                },
                {
                    "cityName": "琼中黎族苗族自治县",
                    "locationId": 469030
                },
                {
                    "cityName": "白沙黎族自治县",
                    "locationId": 469025
                },
                {
                    "cityName": "屯昌县",
                    "locationId": 469022
                },
                {
                    "cityName": "五指山",
                    "locationId": 469001
                }
            ]
        },
        {
            "provinceName": "吉林省",
            "provinceShortName": "吉林",
            "locationId": 220000,
            "cities": [
                {
                    "cityName": "吉林",
                    "locationId": 220200
                },
                {
                    "cityName": "长春",
                    "locationId": 220100
                },
                {
                    "cityName": "四平",
                    "locationId": 220300
                },
                {
                    "cityName": "辽源",
                    "locationId": 220400
                },
                {
                    "cityName": "延边",
                    "locationId": 222400
                },
                {
                    "cityName": "公主岭",
                    "locationId": 220381
                },
                {
                    "cityName": "通化",
                    "locationId": 220500
                },
                {
                    "cityName": "松原",
                    "locationId": 220700
                },
                {
                    "cityName": "梅河口",
                    "locationId": 220581
                },
                {
                    "cityName": "白城",
                    "locationId": 220800
                },
                {
                    "cityName": "白山",
                    "locationId": 220600
                }
            ]
        },
        {
            "provinceName": "贵州省",
            "provinceShortName": "贵州",
            "locationId": 520000,
            "cities": [
                {
                    "cityName": "贵阳",
                    "locationId": 520100
                },
                {
                    "cityName": "遵义",
                    "locationId": 520300
                },
                {
                    "cityName": "毕节",
                    "locationId": 520500
                },
                {
                    "cityName": "黔南布依族苗族自治州",
                    "locationId": 522700
                },
                {
                    "cityName": "六盘水",
                    "locationId": 520200
                },
                {
                    "cityName": "铜仁",
                    "locationId": 520600
                },
                {
                    "cityName": "黔东南苗族侗族自治州",
                    "locationId": 522600
                },
                {
                    "cityName": "安顺",
                    "locationId": 520400
                },
                {
                    "cityName": "黔西南布依族苗族自治州",
                    "locationId": 522300
                },
                {
                    "cityName": "境外输入",
                    "locationId": 0
                }
            ]
        },
        {
            "provinceName": "新疆维吾尔自治区",
            "provinceShortName": "新疆",
            "locationId": 650000,
            "cities": [
                {
                    "cityName": "乌鲁木齐",
                    "locationId": 650100
                },
                {
                    "cityName": "伊犁哈萨克自治州",
                    "locationId": 654000
                },
                {
                    "cityName": "克拉玛依",
                    "locationId": 650200
                },
                {
                    "cityName": "哈密",
                    "locationId": 650500
                },
                {
                    "cityName": "昌吉回族自治州",
                    "locationId": 652300
                },
                {
                    "cityName": "博尔塔拉蒙古自治州",
                    "locationId": 652700
                },
                {
                    "cityName": "吐鲁番",
                    "locationId": 650400
                },
                {
                    "cityName": "巴音郭楞蒙古自治州",
                    "locationId": 652800
                },
                {
                    "cityName": "克孜勒苏柯尔克孜自治州",
                    "locationId": 653000
                },
                {
                    "cityName": "喀什地区",
                    "locationId": 653100
                },
                {
                    "cityName": "和田地区",
                    "locationId": 653200
                },
                {
                    "cityName": "阿克苏地区",
                    "locationId": 652900
                },
                {
                    "cityName": "塔城地区",
                    "locationId": 654200
                },
                {
                    "cityName": "阿勒泰地区",
                    "locationId": 654300
                },
                {
                    "cityName": "直辖县级政区",
                    "locationId": 659000
                }
            ]
        },
        {
            "provinceName": "宁夏回族自治区",
            "provinceShortName": "宁夏",
            "locationId": 640000,
            "cities": [
                {
                    "cityName": "银川",
                    "locationId": 640100
                },
                {
                    "cityName": "吴忠",
                    "locationId": 640300
                },
                {
                    "cityName": "固原",
                    "locationId": 640400
                },
                {
                    "cityName": "中卫",
                    "locationId": 640500
                },
                {
                    "cityName": "宁东",
                    "locationId": 0
                },
                {
                    "cityName": "石嘴山",
                    "locationId": 640200
                }
            ]
        },
        {
            "provinceName": "青海省",
            "provinceShortName": "青海",
            "locationId": 630000,
            "cities": [
                {
                    "cityName": "西宁",
                    "locationId": 630100
                },
                {
                    "cityName": "海北藏族自治州",
                    "locationId": 632200
                },
                {
                    "cityName": "海东",
                    "locationId": 630200
                },
                {
                    "cityName": "黄南藏族自治州",
                    "locationId": 632300
                },
                {
                    "cityName": "海南藏族自治州",
                    "locationId": 632500
                },
                {
                    "cityName": "果洛藏族自治州",
                    "locationId": 632600
                },
                {
                    "cityName": "玉树藏族自治州",
                    "locationId": 632700
                },
                {
                    "cityName": "海西蒙古族藏族自治州",
                    "locationId": 632800
                }
            ]
        },
        {
            "provinceName": "西藏自治区",
            "provinceShortName": "西藏",
            "locationId": 540000,
            "cities": [
                {
                    "cityName": "拉萨",
                    "locationId": 540100
                },
                {
                    "cityName": "日喀则",
                    "locationId": 540200
                },
                {
                    "cityName": "昌都",
                    "locationId": 540300
                },
                {
                    "cityName": "昌都地区",
                    "locationId": 54030000
                },
                {
                    "cityName": "林芝",
                    "locationId": 540400
                },
                {
                    "cityName": "山南",
                    "locationId": 540500
                },
                {
                    "cityName": "那曲地区",
                    "locationId": 540600
                },
                {
                    "cityName": "阿里地区",
                    "locationId": 54250000
                }
            ]
        }
    ]
    # 循环判断存入字典
    for index, i in enumerate(main_city):
        for idx, j in enumerate(i["cities"]):
            if len([x['city_number'] for x in append_result if j["cityName"].replace("区", "") == x["city_name"]]):
                data = [x for x in append_result if
                        j["cityName"].replace("区", "") == x["city_name"]]
                main_city[index]["cities"][idx].update(
                    {"city_number": data[0]["city_number"], "today_time": data[0]["today_time"],
                     "update_time": data[0]["update_time"], "today_wether": data[0]["today_wether"],
                     "today_temperature": data[0]["today_temperature"], "today_ziwaixian": data[0]["today_ziwaixian"],
                     "today_yundong": data[0]["today_yundong"], "today_wear": data[0]["today_wear"]})

            else:
                main_city[index]["cities"][idx].update({"city_number": 0, "today_time": "当前日期：01月09日,周六",
                                                        "update_time": "更新时间：20:00", "today_wether": "当前天气：多云",
                                                        "today_temperature": "今日温度：-7/4°C",
                                                        "today_ziwaixian": "紫外线指数:弱  辐射较弱，涂擦SPF12-15、PA+护肤品。",
                                                        "today_yundong": "减肥指数:天凉室内可健身，户外运动需保暖。",
                                                        "today_wear": "穿衣指数:寒冷  建议着厚羽绒服等隆冬服装。"})

    # 打印
    # print(json.dumps(main_city, indent=1, ensure_ascii=False))
    return json.dumps(main_city, indent=1, ensure_ascii=False)

#
# if __name__ == '__main__':
#     append_result = get_append()
#     save(append_result)
# print(main_city)
#     print(append_result)
