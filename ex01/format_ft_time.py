#https://strftime.org/

from datetime import datetime
import time

epoch_date = datetime.utcfromtimestamp(0).date()

#need time module to have seconds
seconds = time.time()

#need to formate seconds
seconds_with_comma = "{:,}".format(seconds)
seconds_scientific = "{:.2e}".format(seconds)

print("Seconds since", epoch_date.strftime("%B %-d, %Y:"), seconds_with_comma, "or", seconds_scientific)

now = datetime.now()
new_now = datetime.utcnow().second

print(now.strftime("%b %d %Y"))