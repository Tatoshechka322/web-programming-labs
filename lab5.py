from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2

lab5 = Blueprint('lab5',__name__)


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_bokov",
        user="bokov_knowledge_base",
        password="bokov_user")
    return conn


def dbClose(cursor,connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():
    username=session.get("username")
    if username =='':
        visibleUser='Anon'
    else:
        visibleUser=username
    return render_template('main.html',username=visibleUser)