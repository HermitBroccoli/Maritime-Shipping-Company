

class Ship:
    def __init__(self,
                 name: str,
                 capacity: int,
                 year_built: int,
                 current_location: str
                 ) -> None:

        self.name = name  # наименования судна
        self.capacity = capacity  # вместимость
        self.year_built = year_built  # год постройки
        self.current_location = current_location  # местонахождение
        self.carfo = None  # груз отсутвует

    def change_location(self, new_location: str) -> None:
        self.current_location = new_location

    def load_cargo(self, cargo):
        pass

    def unload_cargo(self, cargo):
        pass
