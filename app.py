from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
     return redirect('/menu', code=302)

@app.route("/lab1")
def two():
    return"""
<!doctype html>
<html>
    <head>
        <title>Боков Антон Константинович, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <h2>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые ба-
        зовые возможности.</h2>

        <footer>
            &copy; Антон Боков, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
""" 

@app.route('/menu')
def menu():
    return"""
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h3>
            <a href='/lab1'>Лабораторная работа 1</a>
        </h3>

        <footer>
            &copy; Антон Боков, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""