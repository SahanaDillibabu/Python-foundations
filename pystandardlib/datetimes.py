from datetime import datetime
import time

dt = datetime(2018,1,1)
dt1 = datetime.now()
dt2 = datetime.strptime("2024/04/08", "%Y/%d/%m")
dt3 = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")