class Location():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Trip():
    def __init__(self):
        self.stops = []

    def add_location(self, stop):
        self.stops.append(stop)

    def make_trip(self):
        print("Began trip.")
        for i in range(len(self.stops)-1):
            print(f'Travelled from {self.stops[i]} to {self.stops[i+1]}')
        print("Ended trip.")


road_trip = Trip()
toronto = Location('Toronto')
ottawa = Location('Ottawa')
montreal = Location('Montreal')
quebec_city = Location('Quebec City')
halifax = Location('Halifax')
st_johns = Location("St. John's")

road_trip.add_location(toronto)
road_trip.add_location(ottawa)
road_trip.add_location(montreal)
road_trip.add_location(quebec_city)
road_trip.add_location(halifax)
road_trip.add_location(st_johns)

print(road_trip.stops[0])
road_trip.make_trip()