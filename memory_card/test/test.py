import re
import time

from common.libs.helper import getCurrentDate, str_date_to_datetime
from controllers.web.CardWebController import time_judge

now = getCurrentDate()
# 2019-05-20 17:12
print(now)
print(type(now))

# 2019-05-20 19:32:00
print(str_date_to_datetime(now))
print(type(str_date_to_datetime(now)))

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(type(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))

print(time_judge('2019-05-20 19:33:00'))

# 2019-05-24 00:00:00
time_info = '2019-05-24 00:00:00'
time_info_list = re.findall("\\d+", time_info)
print(time_info_list)

print(int('00'))
