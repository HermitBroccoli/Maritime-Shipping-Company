
from .transport import Transport
from .route import Route


class Ship(Transport):
    def __init__(self,
                 name: str,
                 capacity: int,
                 year_built: int,
                 current_location: str,
                 speed: float
                 ) -> None:

        super().__init__(name, capacity, year_built, speed)
        self.__current_location: str = current_location  # местонахождение
        self.__cargo: float = 0  # груз отсутвует

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, value: float) -> float:
        self.__speed = value

    # полученние текующего места нахождения
    @property
    def current_location(self) -> str:
        return self.__current_location

    # сеетор для сохранения нового значения местанахождения
    @current_location.setter
    def current_location(self, value: str) -> None:
        self.__current_location = value

    # получение количества загруженоссти
    @property
    def cargo(self) -> float:
        return self.__cargo

    #  сеттор для сохренения нового значения загруженности
    @cargo.setter
    def cargo(self, cargo: float) -> None:
        self.__cargo = cargo

    def change_location(self, new_location: str) -> None:
        self.current_location = new_location

    def load_cargo(self, cargo: float) -> None:

        if cargo < 0:
            raise ValueError("Cargo weight cannot be negative.")

        if self.cargo + cargo > self.capacity:
            raise OverflowError(
                f"Cannot load cargo: Exceeds capacity of {self.capacity} tons."
            )

        self.cargo = self.cargo + cargo

    def unload_cargo(self, cargo: float):

        if cargo < 0:
            raise ValueError("Cargo weight cannot be negative.")

        if cargo > self.cargo:
            raise OverflowError(
                f"Cannot load cargo: Exceeds capacity of {self.capacity} tons."
            )

        new_cargo = self.cargo - cargo

        self.cargo = new_cargo

    def get_travel_time(self, route: Route) -> float:
        return route.calculate_travel_time(self.speed)
