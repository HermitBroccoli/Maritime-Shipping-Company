from .route import Route


class Ship:
    def __init__(self,
                 name: str,
                 capacity: int,
                 year_built: int,
                 current_location: str,
                 speed: float
                 ) -> None:

        self.name = name  # наименования судна
        self.capacity = capacity  # вместимость
        self.year_built = year_built  # год постройки
        self.current_location: str = current_location  # местонахождение
        self.cargo: float = 0  # груз отсутвует
        self.speed: float = speed  # скорость

    def change_location(self, new_location: str) -> None:
        self.current_location = new_location

    def load_cargo(self, cargo: float) -> None:

        if cargo < 0:
            raise ValueError("Cargo weight cannot be negative.")

        if self.cargo + cargo > self.capacity:
            raise OverflowError(
                f"Cannot load cargo: Exceeds capacity of {self.capacity} tons."
            )

        self.cargo += cargo

    def unload_cargo(self, cargo):

        if cargo < 0:
            raise ValueError("Cargo weight cannot be negative.")

        if cargo > self.cargo:
            raise OverflowError(
                f"Cannot load cargo: Exceeds capacity of {self.capacity} tons."
            )

        self.cargo -= cargo

    def get_travel_time(self, route: Route) -> float:
        return route.calculate_travel_time(self.speed)
