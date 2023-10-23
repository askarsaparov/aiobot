from datetime import datetime

import pytz


def timestamp_to_datetime(timestamp):
    timestamp = timestamp / 1000
    return datetime.fromtimestamp(timestamp, tz=pytz.timezone('Asia/Tashkent'))


print(timestamp_to_datetime(1694649600000))
