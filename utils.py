import math

# Constants
R = 6371  # Radius of the Earth in kilometers

# Function to calculate distance using Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # Result in kilometers
    return distance

# Test Haversine function
print(haversine(51.5074, -0.1278, 48.8566, 2.3522))  # London to Paris
