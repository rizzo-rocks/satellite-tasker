from skyfield.api import load

"""
Skyfield barebones tutorial
"""

TLE_FILENAME = 'space_stations.tle'
TLE_URL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle'

stations_url = TLE_URL
satellites = load.tle_file(stations_url) # load & parse at TLE file, returning a list of Earth satellites
by_name = {sat.name: sat for sat in satellites} # Earth satellite > Indexing satellites by name or number

for name in by_name: print(name)
print()

iss = by_name['ISS (ZARYA)'] 
ts = load.timescale() # create a Timescale to use for all date and time conversions
t = ts.now() # return current date/time as Time 

geocentric = iss.at(t) # simplest form to generate a satellite position using at() -- returns (x,y,z) relative to Earth's center
print(geocentric.position.km)
