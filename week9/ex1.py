import psycopg2
from geopy.geocoders import Nominatim


def get_query(address_id, latitude, longitude):
	query = f"UPDATE address SET latitude = {latitude}, longitude = {longitude} WHERE address_id = {address_id};"
	return query

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
arr = []
while row is not None:
	current_address = row[1]
	latitude = 0.0
	longitude = 0.0
	try:
		location = geolocator.geocode(current_address)
		latitude = location.latitude
		longitude = location.longitude
	except Exception:
		print('Location not found')
	arr.append((row[0], latitude, longitude))
	print((latitude, longitude))
	row = cur.fetchone()
# close the communication with the PostgreSQL database server
cur.close()

cur = conn.cursor()
for address_id, latitude, longitude in arr:
	query = get_query(address_id, latitude, longitude)
	cur.execute(query)
cur.close()
conn.commit()
	
	
