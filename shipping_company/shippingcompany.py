from typing import List
from .ship import Ship
from .route import Route
from .captain import Captain


class ShippingCompany:

    def __init__(self, name_company: str) -> None:
        self.name_company = name_company  # название компании
        self.fleet: List[Ship] = []  # спикок кораблей
        self.routers: List[Route] = []  # список путей
        self.captains: List[Captain] = []  # список капитанов

    def add_ship(self, ship: Ship) -> None:
        self.fleet.append(ship)

    def add_route(self, route: Route) -> None:
        self.routers.append(route)

    def hire_capitan(self, captain: Captain) -> None:
        self.captains.append(captain)

    def list_ship(self) -> List[str]:
        return [ship.name for ship in self.fleet]

    def list_route(self) -> List[str]:
        return [f"{route.departure_point} to {route.destination}"
                for route in self.routers]

    def list_captain(self) -> List[str]:
        return [f"{capacitan.name} {capacitan.surname}"
                for capacitan in self.captains]
