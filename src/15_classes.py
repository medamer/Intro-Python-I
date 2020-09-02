# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(LatLon):
    def __init__(name, difficulty, size, lat, lon):
        self.name = name
        self.difficulty = difficulty
        self.size = size
        self.lat = lat
        self.lon = lon

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
class Waypoint:
    def __init__(self,name, lat, lon):
        self.name = "Catacombs"
        self.lat = 41.70505
        self.lon = -121.51521
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint(name = "Catacombs",lat = 41.70505, lon = -121.51521)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
class Geocache:
    def __init__(self, name, difficulty, size, lat, lon):
        self.name = "Newberry Views"
        self.difficulty = "diff 1.5"
        self.size = "size 2"
        self.lat = 44.052137
        self.lon = -121.41556
# Print it--also make this print more nicely
geocache = Geocache(name = "Newberry Views", difficulty="diff 1.5", size="size 2", lat=44.052137, lon=-121.41556)
print(geocache)
