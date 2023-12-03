import time
import datetime

seconds = time.time()

ecriture_scientifique = "{:.2e}".format(seconds)

date_actuelle = datetime.datetime.now()
format_date = date_actuelle.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {seconds} or {ecriture_scientifique} in scientific notation")
print(f"{format_date}")