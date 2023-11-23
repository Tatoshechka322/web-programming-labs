from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route('/lab2/example')
def example():
    name, number, group, cours = 'Боков Антон','Лабораторная работа 2', 'ФБИ-12', '3 курс'
    fruits =[
         {'name':'яблоки','price':88},
         {'name':'груши','price':74},
         {'name':'апельсины','price':94},
         {'name':'мандарины','price':90},
         {'name':'манго','price':400}
         ]

    books =[
         {'name': 'Ася','author': 'Тургенев Иван','style': 'повесть','page':128},
         {'name': 'Яд бессмертия','author': 'Робертс Нора','style': 'детектив','page':416},
         {'name': 'Триумфальная арка','author': 'Ремарк Эрих Мария','style': 'роман','page':540},
         {'name': 'Долина ужаса','author': 'Дойл Артур Конан','style': 'детектив','page':199},
         {'name': 'Знак четырех','author': 'Дойл Артур Конан','style': 'детектив','page':136},
         {'name': 'Ревизор','author': 'Гоголь Николай','style': 'комедия','page':192},
         {'name': 'Три товарища','author': 'Ремарк Эрих Мария','style': 'роман','page':484},
         {'name': 'Иллюзия греха','author': 'Маринина Александра','style': 'детектива','page':448},
         {'name': 'Преступление и наказания','author': 'Иоганн Вольфганг Гете','style': 'роман','page':592},
         {'name': 'Процесс','author': 'Франц Кафка','style': 'роман','page':416}
    ]   

    return render_template('example.html', name=name, group=group, cours=cours,number=number,fruits=fruits, books=books)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/pictures')
def pictures():
    return render_template('pictures.html')