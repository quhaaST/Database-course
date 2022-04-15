import psycopg2
from geopy.geocoders import Nominatim

conn = psycopg2.connect(database="dvdrental", user="postgres",
                       password="", host="127.0.0.1", port="5432")
                       
cur = conn.cursor()

pattern = '11'
lower_id_bound = 400
upper_id_bound = 600

geolocator = Nominatim(user_agent="dvdrental")

cur.callproc('get_addresses', (pattern, lower_id_bound, upper_id_bound, ))
# process the result set
row = cur.fetchone()
while row is not None:
	current_address = row[1]
	try:
		location = geolocator.geocode(current_address)
		print((location.latitude, location.longitude))
	except Exception:
		print(0, 0)
	row = cur.fetchone()

# close the communication with the PostgreSQL database server
cur.close()
