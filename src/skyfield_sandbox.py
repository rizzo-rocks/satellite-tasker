"""
==================================
Skyfield barebones tutorial
==================================
"""
from skyfield.api import load, wgs84

TLE_URL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle'

satellites = load.tle_file(TLE_URL) # load & parse at TLE file, returning a list of Earth satellites
by_name = {sat.name: sat for sat in satellites} # Earth satellite > Indexing satellites by name or number

iss = by_name["ISS (ZARYA)"] 
ts = load.timescale() # create a Timescale to use for all date and time conversions
t = ts.now() # return current date/time as Time 

# geocentric = iss.at(t) # simplest form to generate a satellite position using at() -- returns (x,y,z) relative to Earth's center


"""
==================================
Get ISS coordinates

Fun fact: the linspace() method here is Skyfield's (uses Numpy under the hood)
==================================
"""
from datetime import timedelta

t_0 = ts.now()
t_1 = ts.utc(t_0.utc_datetime() + timedelta(days=1))
times = ts.linspace(t_0, t_1, 500) # Returns a Time object that supports vectorized operations over the time range...

geocentric = iss.at(times) # ... which is great and very helpful 

subpoint = wgs84.subpoint(geocentric)
latitudes = subpoint.latitude.degrees
longitudes = subpoint.longitude.degrees


"""
==================================
Plot ground track
==================================
"""
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.title("ISS Ground Track (Next 24 Hours)")
plt.plot(longitudes, latitudes, label="ISS Orbit", linewidth=1)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.xlim([-180, 180])
plt.ylim([-90, 90])
plt.legend()
plt.show()
