from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form():
    errors={}
    errorss={}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errorss['age'] = 'Заполните поле!'
    sex = request.args.get('sex')

    return render_template('form1.html', user=user, age=age, sex=sex,errors=errors,errorss=errorss) 


@lab3.route('/lab3/order')
def order():
    drink=request.args.get('drink')
    milk=request.args.get('milk')
    sugar=request.args.get('sugar')
    return render_template('order.html', drink=drink, milk=milk, sugar=sugar)


@lab3.route('/lab3/pay')
def pay():
    price=0
    drink=request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    card=request.args.get('card')
    name=request.args.get('name')
    cvv=request.args.get('cvv')

    return render_template('pay.html',price=price,card=card,name=name,cvv=cvv)


@lab3.route('/lab3/succes')
def succes():
    return render_template('succes.html')


@lab3.route('/lab3/bilet')
def bilet():
    errors={}
    FIO=request.args.get('FIO')
    if FIO == '':
        errors['FIO'] = 'Заполните поле!'

    age=request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    
    wherefrom=request.args.get('wherefrom')
    if wherefrom == '':
        errors['wherefrom'] = 'Заполните поле!'
    
    whereto=request.args.get('whereto')
    if whereto == '':
        errors['whereto'] = 'Заполните поле!'
    
    date=request.args.get('date')
    if date == '':
        errors['date'] = 'Заполните поле!'
    
    type=request.args.get('type')
    place=request.args.get('place')
    things=request.args.get('things')
    return render_template('bilet.html',FIO=FIO,age=age,wherefrom=wherefrom,whereto=whereto,date=date,type=type,place=place,things=things,errors=errors)
