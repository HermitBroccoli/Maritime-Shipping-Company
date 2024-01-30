
class Route:

    """
    Определяет маршрут с точками отправления и назначения, а также дистанцией.
    Позволяет рассчитывать время путешествия на основе заданной скорости.
    """

    def __init__(self,
                 departure_point: str,  # начальный пункт
                 destination: str,  # конечный пункт
                 distance: float  # дистанция
                 ) -> None:
        """
        Инициализирует экземпляр класса Route. Принимает точку отправления,
        точку назначения и дистанцию маршрута.
        """

        self.__departure_point = departure_point
        self.__destination = destination
        self.__distance = distance

    @property
    def departure_point(self) -> str:
        """
        Возвращает точку отправления маршрута.
        """
        return self.__departure_point

    @departure_point.setter
    def departure_point(self, value: str) -> None:
        """
        Устанавливает новую точку отправления маршрута. Принимает строку
        с названием новой точки отправления.
        """
        self.__departure_point = value

    @property
    def destination(self) -> str:
        """
        Возвращает точку назначения маршрута.
        """
        return self.__destination

    @destination.setter
    def destination(self, value: str) -> None:
        """
        Устанавливает новую точку назначения маршрута. Принимает строку
        с названием новой точки назначения.
        """
        self.__destination = value

    @property
    def distance(self) -> float:
        """
        Возвращает дистанцию маршрута.
        """
        return self.__distance

    @distance.setter
    def distance(self, value: float) -> None:
        """
        Устанавливает новую дистанцию маршрута. Принимает значение
        дистанции в качестве параметра.
        """
        self.__distance = value

    def calculate_travel_time(self, speed: float) -> float:
        """
        Рассчитывает время путешествия по маршруту на основе заданной скорости.
        Вызывает исключение, если скорость не является положительной.
        Принимает скорость в качестве параметра.
        """
        if speed <= 0:
            raise ValueError("speed must be positive")

        return self.distance / speed
