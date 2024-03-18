
from .transport import Transport
from .route import Route


class Ship(Transport):

    """
    Описывает корабль, наследуя свойства от Transport. Включает в себя
    название, вместимость, год постройки, текущее местоположение и скорость.
    Управляет загрузкой/разгрузкой груза и расчетом времени путешествия.
    """

    def __init__(self,
                 name: str,
                 capacity: int,
                 year_built: int,
                 current_location: str,
                 speed: float
                 ) -> None:
        """
        Инициализирует экземпляр класса Ship с заданными параметрами.
        Принимает название, вместимость, год постройки, текущее местоположение
        и скорость корабля.
        """

        super().__init__(name, capacity, year_built, speed)
        self.__current_location: str = current_location  # местонахождение
        self.__cargo: float = 0  # груз отсутвует

    @property
    def speed(self) -> float:
        """
        Возвращает текущую скорость корабля.
        """
        return self.__speed

    @speed.setter
    def speed_edit(self, value: float) -> None:
        """
        Устанавливает новую скорость корабля. Принимает значение скорости.
        """
        self.__speed = value

    @property
    def current_location(self) -> str:
        """
        Возвращает текущее местоположение корабля.
        """
        return self.__current_location

    @current_location.setter
    def current_location(self, value: str) -> None:
        """
        Устанавливает новое местоположение корабля. Принимает строку с
        названием местоположения.
        """
        self.__current_location = value

    @property
    def cargo(self) -> float:
        """
        Возвращает текущий вес груза на корабле.
        """
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: float) -> None:
        """
        Устанавливает новый вес груза на корабле. Принимает вес груза.
        """
        self.__cargo = cargo

    def change_location(self, new_location: str) -> None:
        """
        Изменяет текущее местоположение корабля. Принимает строку с новым
        местоположением.
        """
        self.current_location = new_location

    def load_cargo(self, cargo: float) -> None:

        """
        Загружает груз на корабль. Принимает вес груза для загрузки.
        Вызывает исключение, если загрузка превышает вместимость или вес
        груза отрицателен.
        """

        if cargo < 0:
            raise ValueError("Cargo weight cannot be negative.")

        if self.cargo + cargo > self.capacity:
            raise OverflowError(
                f"Cannot load cargo: Exceeds capacity of {self.capacity} tons."
            )

        self.cargo += cargo

    def unload_cargo(self, cargo: float):

        """
        Разгружает груз с корабля. Принимает вес груза для разгрузки.
        Вызывает исключение, если разгружаемый вес превышает текущий вес
        груза или вес отрицателен.
        """

        if cargo < 0:
            raise ValueError("Cargo weight cannot be negative.")

        if cargo > self.cargo:
            raise OverflowError(
                f"Cannot load cargo: Exceeds capacity of {self.capacity} tons."
            )

        self.cargo -= cargo

    def get_travel_time(self, route: Route) -> float:

        """
        Рассчитывает время путешествия по заданному маршруту. Принимает
        объект маршрута и использует его дистанцию и скорость корабля для
        расчета времени.
        """

        return route.calculate_travel_time(self.speed)
