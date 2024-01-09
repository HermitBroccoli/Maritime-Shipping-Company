

class Route:

    def __init__(self,
                 departure_point: str,
                 destination: str,
                 distance: float
                 ) -> None:

        self.departure_point = departure_point
        self.destination = destination
        self.distance = distance

    def calculate_travel_time(self):
        pass
