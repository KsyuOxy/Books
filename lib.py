from models import Book
from tkinter import *

"""
    Для тестирования ĸласса создайте списоĸ из 5 ĸниг различных авторов, выведите
    на эĸран ĸонсоли ** или Tkinter все хараĸтеристиĸи этих ĸниг и найдите их
    среднюю цену
"""

# -> создание объектов класса Book
book1 = Book('Юрий Никитин', 'Трое из леса', 'фэнтези', 215, 'твёрдая')
book2 = Book('Стивен Кинг', 'Кладбище домашних животных', 'мистика, ужасы', 185, 'мягкая')
book3 = Book('Александр Романович Беляев', 'Голова профессора Доуэля', 'фантастика', 129, 'мягкая')
book4 = Book('Артур Конан Дойль', 'Маракотова бездна', 'фантастика', 234, 'твёрдая')
book5 = Book('Джон Уиндем', 'День триффидов', 'фантастика', 189, 'мягкая')

# -> расчёт средней стоимости книг с округлением до 2 знаков
average_cost = round(((book1.get_price() + book2.get_price() + book3.get_price() + book4.get_price() +
                       book5.get_price())/5), 2)

# -> создание и параметры окна
root = Tk()
root.geometry('600x400+200+200')
root.title('Книги')
root.config(bg='Wheat')

Label(root, width=10, bg='Wheat', text='Мир книг', font=('Comic Sans Ms', 22), fg='SaddleBrown').place(x=45, y=10)
Label(root, width=19, bg='Wheat', text='Средняя стоимость книг:', font=('Comic Sans Ms', 11), fg='SaddleBrown')\
    .place(x=30, y=340)

# -> отображает книги и их характеристики
shows_books = Label(root)
shows_books.config(width=60, height=15, text=f'{book1}\n{book2}\n{book3}\n{book4}\n{book5}', justify=LEFT,
                   font=('Comic Sans Ms', 10), bg='Wheat', fg='SaddleBrown')
shows_books.place(x=30, y=60)

# -> отображает среднюю стоимость
result_label = Label(root)
result_label.config(width=10, bg='Tan', font=('Comic Sans Ms', 10), fg='SaddleBrown', bd=2, relief=RIDGE,
                    text=f'{average_cost} грн')
result_label.place(x=220, y=340)


# -> изменяет значения цен, обложек и среднюю стоимость книг, обновляет текст в Labels
def update_prices():
    # -> изменения цен и типа обложек книг
    book1.set_price(200)
    book1.set_cover('мягкая')

    book2.set_price(200)
    book2.set_cover('твёрдая')

    book3.set_price(300)
    book3.set_cover('твёрдая')

    book4.set_price(200)
    book4.set_cover('мягкая')

    book5.set_price(300)
    book5.set_cover('твёрдая')

    # -> расчёт средней стоимости книг с учётом новых значений
    average_cost_update = round(((book1.get_price() + book2.get_price() + book3.get_price() + book4.get_price() +
                                  book5.get_price()) / 5), 2)

    result_label.config(text=f'{average_cost_update} грн')  # -> переопределение параметра текста
    shows_books.config(text=f'{book1}\n{book2}\n{book3}\n{book4}\n{book5}')  # -> замена текста с учётом новых значений


# -> кнопка вызова функции update_prices()
button_update = Button(root)
button_update.config(width=12, font=('Comic Sans Ms', 9), fg='SaddleBrown', text='Обновить', bg='Tan',
                     command=update_prices)
button_update.place(x=480, y=340)
