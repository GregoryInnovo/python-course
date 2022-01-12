from datetime import datetime
import pytz

# Select a code from: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
bogota_date = datetime.now(mexico_timezone)
print("Ciudad de México: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("Ciudad de México: ", caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))