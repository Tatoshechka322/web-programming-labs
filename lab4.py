from flask import Blueprint, redirect, url_for, render_template, request
lab4 = Blueprint('lab4',__name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'bokov' and password == '123':
        return render_template('success_login.html',username=username)
    
    error = ''
    if username != 'bokov' or password != '123':
        error = 'Неверный логин и/или пароль'
    if username == '':
        error = 'Не введен логин!'
    if password == '':
        error = 'Не введен пароль!'
    
    return render_template('login.html', error=error,username=username,password=password)


@lab4.route('/lab4/fridge', methods=['GET','POST'])
def fridge():
    if request.method == 'GET':
        return render_template('fridge.html')
   
    temp = request.form.get('temp')
    error=''

    if temp == '':
        error = 'Ошибка: не задана температура'
    else:
        if temp:
            temp=int(temp)
            if (temp>-13) and 0>temp:
                if (temp>-13) and (-8>temp):
                    snow = '❄️❄️❄️'
                elif (temp>-9) and (-4>temp):
                    snow = '❄️❄️'
                elif (temp>-5) and (0>temp):
                    snow = '❄️'
                return render_template('success_fridge.html',temp=temp,snow=snow)

            if temp <-12:
                error = 'Не удалось установить температуру: слишком низкое значение'
            if temp >-1:
                error = 'Не удалось установить температуру: слишком высокое значение'

    return render_template('fridge.html',temp=temp,error=error)