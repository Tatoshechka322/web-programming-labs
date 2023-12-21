from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2

lab5 = Blueprint('lab5',__name__)


def dbConnect():
    # Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_ersh_trub",
        user="ersh_trub_knowledge_base",
        password="ershtrub123")
    return conn


def dbClose(cursor,connection):
    # Закрываем курсор и соединение 
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_bokov",
        user="bokov_knowledge_base",
        password="bokov_user")
    
    cur=conn.cursor()

    cur.execute ("SELECT * FROM users;")

    result = cur.fetchall()


    cursor.close()
    connection.close()

    print(result)
    return 'go to console'


    username=session.get("username")
    if username =='':
        visibleUser='Anon'
    else:
        visibleUser=username
    return render_template('5_main.html',username=visibleUser)