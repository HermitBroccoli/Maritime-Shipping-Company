from typing import List
from shipping_company.ship import Ship
from shipping_company.route import Route
from shipping_company.captain import Captain


class ShippingCompany:

    """
    Представляет собой морскую транспортную компанию с названием, флотом,
    маршрутами и капитанами. Управляет добавлением кораблей, маршрутов и
    наймом капитанов. Предоставляет списки кораблей, маршрутов и капитанов.
    """

    def __init__(self, name_company: str) -> None:
        """
        Инициализирует экземпляр класса ShippingCompany. Принимает название
        компании и инициализирует списки для управления флотом кораблей,
        маршрутами и капитанами.
        """

        self.__name_company: str = name_company  # название компании
        self.__fleet: List[Ship] = []  # спикок кораблей
        self.__routers: List[Route] = []  # список путей
        self.__captains: List[Captain] = []  # список капитанов

    @property
    def name_company(self) -> str:
        """
        Возвращает название транспортной компании.
        """

        return self.__name_company

    @property
    def fleets(self) -> List[Ship]:
        """
        Возвращает список кораблей, принадлежащих компании.
        """

        return self.__fleet

    def add_ship(self, value: Ship) -> None:
        """
        Добавляет корабль в флот компании. Принимает экземпляр класса Ship.
        """

        self.__fleet.append(value)

    @property
    def routers(self) -> List[Route]:
        """
        Возвращает список маршрутов, доступных для компании.
        """

        return self.__routers

    def add_route(self, value: Route) -> None:
        """
        Добавляет маршрут в список маршрутов компании. Принимает экземпляр
        класса Route.
        """

        self.__routers.append(value)

    @property
    def captains(self) -> List[Captain]:
        """
        Возвращает список капитанов, работающих в компании.
        """

        return self.__captains

    def hire_captain(self, value: Captain) -> None:
        """
        фНанимает капитана для работы в компании. Принимает экземпляр класса
        Captain.
        """

        self.__captains.append(value)

    def list_ship(self) -> List[str]:
        """
        Возвращает список названий всех кораблей в флоте компании.
        """

        return [ship.name for ship in self.fleets]

    def list_route(self) -> List[str]:
        """
        Возвращает список всех маршрутов, доступных для компании, в формате
        'отправление - назначение'.
        """

        return [f"'{route.departure_point}' to '{route.destination}'"
                for route in self.routers]

    def list_captain(self) -> List[str]:

        """
        Возвращает список всех капитанов, работающих в компании, в формате
        'имя фамилия'.
        """

        return [f"{captains.name} {captains.surname}"
                for captains in self.captains]
