from flask import Blueprint, render_template, request

zach=Blueprint('zach',__name__)


def calculate_expression(N):  
    result = 0  
    sign = 1

    for i in range(1, N + 1):  
        result += sign * (i / 10)  
        sign *= -1  # Смена знака  
  
    return result  
  
@zach.route('/zach', methods=['GET', 'POST'])  
def zach1():  
    sign = 1  
    N = 5
    result = calculate_expression(N)  
    return render_template('zach.html', result=result)  
