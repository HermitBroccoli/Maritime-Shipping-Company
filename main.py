from shipping_company import Route, Ship, Captain, ShippingCompany  # noqa
from typing import List, Dict, TypedDict
from sys import platform
from subprocess import run as r


class Flights(TypedDict):
    on: str
    where: str
    ship: str
    point: str
    cap: str


def clear_cols():
    if platform.startswith("win"):
        r("cls", shell=True)
    else:
        r("cls", shell=True)


class Table:
    def __init__(self, width: int, line: int) -> None:
        self.__width = width
        self.__line = line

    @property
    def width(self):
        return self.__width

    @property
    def line(self):
        return self.__line

    @width.setter
    def set_width(self, value: int) -> None:
        self.__width = value


class TableFlight(Table):
    def __init__():
        super().__init__()

    def __width_line(self, value: Flights) -> str:
        return (
            f"| {value['on']} в {value['where']} | Судно: {value['ship']} | "
            f"Местонахождение: {value['point']} | Капитан: {value['cap']}"
            )

    def __lines(self, value: List):
        lines = []

        for line in value:
            lines.append(
                self.__width_line(line)
            )

        return lines

    def __find_max_width(self, value: List[str]) -> int:
        if not value:
            return None

        max_lengt = 0

        for len_string in value:
            if len(len_string) > max_lengt:
                max_lengt = len(len_string)

        return max_lengt

    def __create_table(self, value):
        result = self.__lines(value)
        self.set_width = self.__find_max_width(result)

        print(self.width)


class Menu:

    def __init__(self) -> None:
        self.__companes: List[Dict[int, ShippingCompany]] = []
        self.__ships: List[Ship] = []  # noqa
        self.__routers: List[Route] = []  # noqa
        self.__captains: List[Captain] = []  # noqa
        self.__flights: List[Dict[Flights]] = []

    @property
    def companes(self):
        return self.__companes

    @property
    def ships(self):
        return self.__ships

    @property
    def captains(self):
        return self.__captains

    @property
    def routes(self):
        return self.__routers

    @property
    def flights(self):
        return self.__flights

    def __hiring_caption(self, value: Captain) -> None:

        if not (value.name and value.surname
                and value.qualification and value.experience):
            raise ValueError("You must provide")

        self.captains.append(Captain(
            name=value.name,
            surname=value.surname,
            experience=value.experience,
            qualification=value.qualification
        ))

    def __dismissal_caption(self, value: int) -> None:
        if value < 0 or len(self.captains) < value:
            raise ValueError("value must be a string")

        self.captains.pop(value)

    def __create_company(self, value: str) -> None:
        if not value:
            raise ValueError("value must be a string")

        self.companes.append({
            len(self.__companes): ShippingCompany(value)
        })

    def __ifOs(self) -> None:
        clear_cols()

    def clear_col(self, func):
        def wrapper():
            self.__ifOs()
            func()
            self.__ifOs()
        return wrapper

    def __add_ship(self) -> None:

        name = input("Название коробля: ")
        capacity = int(input("Грузовместимость: ").replace(',', ''))
        year_built = int(input("Год постройки: "))
        current_location = input("Текущее местонахождение: ")
        speed = float(input("Скорость передвежения: ").replace(',', '.'))

        if not (name and capacity and current_location):
            print("Отсутвуют обязательные компоненты")
            return

        if speed <= 0:
            print(
                "Скорость передвежения не может быть равна нулю ",
                "или быть меньше"
            )
            return

        if year_built <= 0:
            print("Не может быть равен или быть меньше нуля")
            return

        self.ships.append(
            Ship(
                name=name,
                capacity=capacity,
                year_built=year_built,
                current_location=current_location,
                speed=speed
            )
        )

    def __list_capitan(self):
        for i, item in enumerate(self.captains):
            print(
                f"{i+1}. {item.name} {item.surname}"
            )

    def run(self):
        clear_cols()
        line: str = '-' * 59

        menu = [
            ["1", "Создать/добавить судоходную компанию"],
            ["2", "Создать/добавить судно"],
            ["3", "Создать маршрут"],
            ["4", "Создать рейс"],
            ["5", "Нанять капитана"],
            ["6", "Удалить судно"],
            ["7", "Уволить капитана"],
            ["8", "Удалить маршрут"],
            ["9", "Удалить рейс"],
            ["10", "Вывести список судн"],
            ["11", "Вывести список капитанов"],
            ["12", "Вывести список маршрутов"],
            ["13", "Вывести список компаний"],
            ["14", "Вывести список рейсов"]
            ["15", "Выход"]
        ]

        def print_menu():
            print(
                f"{line}\n"
                f"|{" "*8}Система управления судоходными компаниями{" "*8}|\n"
                f"{line}"
            )

            for row in menu:
                print(
                    f"|  {row[0]}. {row[1]} {' ' * (57-(len(row[0]) + len(row[1]) + 5))}|\n"  # noqa,
                    f"{line}",
                )

        @self.clear_col
        def create_company():
            name_company = input("Введите название компание: ")
            self.__create_company(name_company)

        @self.clear_col
        def create_chip():
            self.__add_ship()

        @self.clear_col
        def create_capitan():
            name = input("Введите имя капитана: ")
            surname = input("Введите фамилию капитана: ")
            experience = int(input("Введите опыт капитана: "))
            qualification = input("Введите клалификацию капитана: ")

            self.__hiring_caption(Captain(
                name=name,
                surname=surname,
                experience=experience,
                qualification=qualification
            ))

        @self.clear_col
        def delete_capitan():
            value = int(input("> "))
            self.__dismissal_caption(value=value-1)

        print_menu()

        while True:

            res = int(input("> "))  # noqa

            if res == 1:
                create_company()
                print_menu()

            if res == 2:
                create_chip()
                print_menu()

            if res == 4:
                create_capitan()
                print_menu()

            if res == 6:
                delete_capitan()
                print_menu()

            if res == 9:
                self.__list_capitan()
                print_menu()

            if res == 13:
                for i, item in enumerate(self.companes):
                    print(
                        f"{i+1}. {item[i].name_company}"
                    )

            if res == 15:
                exit()


def main() -> None:
    menu = Menu()

    menu.run()


if __name__ == '__main__':
    main()
