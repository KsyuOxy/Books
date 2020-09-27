"""
Разработайте ĸласс Book (Книга) и реализуйте в нем ĸонструĸтор объеĸтов,
набор атрибутов, набор аĸсессоров и метод __str__().
"""


# -> создание класса Book
class Book:
    # -> определяет атрибуты (защищённые от случайного изменения)
    def __init__(self, author: str, title: str, genre: str, price: float, cover: str):
        self.__author = author  # -> автор
        self.__title = title  # -> название книги
        self.__genre = genre  # -> жанр
        self.__price = price  # -> цена
        self.__cover = cover  # -> тип обложки

    def __str__(self) -> str:    # -> переопределение строкового отображения
        return f'{self.__author} "{self.__title}" - цена: {self.__price} грн.\nжанр: {self.__genre}; ' \
               f'обложка {self.__cover}\n'

    def get_cover(self) -> str:  # -> метод получения значения cover
        return self.__cover

    def set_cover(self, new_cover) -> None:  # -> метод для переопределения значения cover
        self.__cover = new_cover

    def get_price(self) -> float:  # -> метод получения значения price
        return self.__price

    def set_price(self, new_price) -> None:  # -> метод для переопределения значения price
        self.__price = new_price
