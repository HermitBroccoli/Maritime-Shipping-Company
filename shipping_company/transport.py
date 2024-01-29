class Transport:
    def __init__(
            self, name: str,
            capacity: int,
            year_built: int,
            speed: float
    ) -> None:

        self.__name = name
        self.__capacity = capacity
        self.__year_built = year_built
        self.__speed = speed

    def change_location(self, new_location: str) -> None:
        raise NotImplementedError(
            "This method should be implemented in a subclass")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def year_built(self) -> int:
        return self.__year_built

    @property
    def speed(self) -> float:
        return self.__speed
