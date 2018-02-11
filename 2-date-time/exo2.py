from datetime import datetime

now = datetime.now()
date = '%s/%s/%s' % (now.day, now.month, now.year)
time = '%s:%s:%s' % (now.hour, now.minute, now.second)

print date + " " + time