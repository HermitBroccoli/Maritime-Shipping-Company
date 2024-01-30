class Transport:

    """
    Базовый класс для транспортных средств. Включает общие характеристики
    транспорта, такие как название, вместимость, год постройки и скорость.
    Требует реализации метода изменения местоположения в подклассах.
    """

    def __init__(
            self, name: str,
            capacity: int,
            year_built: int,
            speed: float
    ) -> None:
        """
        Инициализирует экземпляр класса Transport. Принимает название
        транспорта, его вместимость, год постройки и скорость.
        """

        self._name = name
        self._capacity = capacity
        self._year_built = year_built
        self._speed = speed

    def change_location(self, new_location: str) -> None:
        """
        Абстрактный метод для изменения местоположения транспорта.
        Должен быть реализован в подклассах. Принимает новое местоположение.
        """

        raise NotImplementedError(
            "This method should be implemented in a subclass")

    @property
    def name(self) -> str:
        """
        Возвращает название транспортного средства.
        """
        return self._name

    @property
    def capacity(self) -> int:
        """
        Возвращает вместимость транспортного средства.
        """
        return self._capacity

    @property
    def year_built(self) -> int:
        """
        Возвращает год постройки транспортного средства.
        """
        return self._year_built

    @property
    def speed(self) -> float:
        """
        Возвращает скорость транспортного средства.
        """
        return self._speed
