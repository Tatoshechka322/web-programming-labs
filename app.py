from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
     return redirect('/menu', code=302)


@app.route("/lab1")
def two():
    return'''
<!doctype html>
<html>
    <head> 
        <link rel='stylesheet' type='text/css' href="''' + url_for('static',filename='lab1.css') + '''"
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

        <h3><a href='/menu'>Меню</a></h3>

        <h2>Реализованные роуты</h2>
        <h3><a href='/lab1/oak'>Дуб</a></h3>
        <h3><a href='/lab1/student'>Судент</a></h3>
        <h3><a href='/lab1/python'>Python</a></h3>
        <h3><a href='/lab1/bi'>Бизнес-Информатика</a></h3>

        <footer>
            &copy; Антон Боков, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@app.route('/menu')
def menu():
    return'''
<!doctype html>
<html>
    <head>
        <link rel='stylesheet' type='text/css' href="''' + url_for('static',filename='lab1.css') + '''"
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
'''


@app.route('/lab1/oak')
def oak():
    return'''
<!doctype html>
<html
    <head> 
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static' , filename='oak.jpg') + '''">
    </body>
</html>
'''


@app.route('/lab1/student')
def logo():
     return '''
<!doctype html>
<html
    <head> 
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Боков Антон Константинович</h1>
        <img src="''' + url_for('static' , filename='logo.png') + '''">
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
     return '''
<!doctype html>
<html
    <head> 
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div>Большая часть работы программистов связана с написанием исходного кода, тестированием и отладкой программ 
        на одном из языков программирования. Исходные тексты и исполняемые файлы программ являются объектами авторского 
        права и являются интеллектуальной собственностью их авторов и правообладателей</div>
        <br>
        <div>Различные языки программирования поддерживают различные стили программирования (парадигмы программирования). 
        Выбор нужного языка программирования для некоторых частей алгоритма позволяет сократить время написания программы и решить задачу
        описания алгоритма наиболее эффективно. Разные языки требуют от программиста различного уровня внимания к деталям при реализации
        алгоритма, результатом чего часто бывает компромисс между простотой и производительностью (или между «временем программиста»
        и «временем пользователя»).</div>
        <br>
        <div>Единственный язык, напрямую выполняемый ЭВМ — это машинный язык (также называемый машинным кодом и языком машинных команд).
        Изначально все программы писались в машинном коде, но сейчас этого практически уже не делается. Вместо этого программисты пишут
        исходный код на том или ином языке программирования, затем, используя компилятор, транслируют его в один или несколько этапов
        в машинный код, готовый к исполнению на целевом процессоре, или в промежуточное представление, которое может быть исполнено
        специальным интерпретатором — виртуальной машиной. Но это справедливо только для языков высокого уровня. Если требуется 
        полный низкоуровневый контроль над системой на уровне машинных команд и отдельных ячеек памяти, программы пишут на языке 
        ассемблера, мнемонические инструкции которого преобразуются один к одному в соответствующие инструкции машинного языка 
        целевого процессора ЭВМ (по этой причине трансляторы с языков ассемблера получаются алгоритмически простейшими трансляторами).</div>
        <img src="''' + url_for('static' , filename='python.jpg') + '''">
    </body>
</html>
'''


@app.route('/lab1/bi')
def bi():
     return '''
<!doctype html>
<html
    <head> 
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Бизнес-Информатика</h1>
        <div>Бизнес-информатика (BI) - дисциплина, объединяющая экономику, экономику оцифровки, бизнес-администрирование, 
        информационные технологии (IT) и концепции информатики.</div>
        <div>Бизнес-информатика сосредоточена вокруг создания программных и аппаратных фреймворков, которые в конечном итоге
         обеспечивают эффективную работу организации на основе применения информационных технологий. 
         Акцент на программировании и оборудовании повышает ценность анализа экономики и информационных технологий.</div>
        <img src="''' + url_for('static' , filename='bi.png') + '''">
    </body>
</html>
'''
@app.route('/lab2/example')
def example():
    name = 'Боков Антон'
    group = 'ФБИ-12'
    cours = '3 курс'
    number = 'Лабораторная работа 2'
    return render_template('example.html', name=name, group=group, cours=cours,number=number)