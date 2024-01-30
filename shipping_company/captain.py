class Captain:

    """
    Представляет капитана корабля.
    Хранит информацию о имени, фамилии, опыте и квалификации капитана.
    """

    def __init__(self,
                 name: str,
                 surname: str,
                 experience: int,
                 qualification: str
                 ) -> None:
        """
        Инициализирует экземпляр класса Captain с заданными параметрами.
        Принимает имя, фамилию, опыт и квалификацию капитана.
        """

        self.__name = name  # имя капитана
        self.__surname = surname  # фамилия капитана
        self.__experience = experience  # опыт капитана
        self.__qualification = qualification  # квалификация капитана

    @property
    def name(self) -> str:
        """
        Возвращает имя капитана.
        """

        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает новое имя капитана. Принимает строку с именем.
        """

        self.__name = value

    @property
    def surname(self) -> str:
        """
        Возвращает фамилию капитана.
        """
        return self.__surname

    @surname.setter
    def surname(self, value: str) -> None:
        """
        Устанавливает новую фамилию капитана. Принимает строку с фамилией.
        """
        self.__surname = value

    @property
    def qualifier(self) -> str:
        """
        Возвращает квалификацию капитана.
        """
        return self.__qualification

    @qualifier.setter
    def qualifier(self, value: str) -> None:
        """
        Устанавливает новую квалификацию капитана. Принимает строку с
        квалификацией.
        """
        self.__qualification = value

    @property
    def experience(self) -> int:
        """
        Возвращает опыт капитана в годах.
        """
        return self.__experience

    @experience.setter
    def experience(self, value: int) -> None:
        """
        Устанавливает новый опыт капитана. Принимает целое число лет опыта.
        """

        self.__experience = value
