from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2
from Db import db
from Db.models import users,articles
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('lab6',__name__)

@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"

@lab6.route("/lab6/check_articles")
def check_articles():
    
    my_articles = articles.query.all()
    print(my_articles)
    return "result in console!"

@lab6.route("/lab6/register",methods=["GET","POST"])
def register():
    if request.method=='GET':
        return render_template('register.html')

    errors = ''
    username_form=request.form.get('username')
    password_form=request.form.get('password')

    if username_form =='' or password_form == '':
        errors='Пожалуйста, заполните все поля'
        return render_template('register.html',errors=errors)

    isUserExist = users.query.filter_by(username=username_form).first()
    if isUserExist is not None:
        errors='Пользователь с данным именем уже существует'
        return render_template('register.html',errors=errors)

    if len(password_form) < 5:
        errors='Придумайте более сложный пароль'
        return render_template('register.html',errors=errors)
   
    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form,password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()

    return redirect('/lab6/login')

@lab6.route("/lab6/login",methods=["GET","POST"])
def login():
    if request.method=='GET':
        return render_template('login_5.html')

    errors=''
    username_form=request.form.get('username')
    password_form=request.form.get('password')

    if username_form =='' or password_form == '':
        errors='Пожалуйста, заполните все поля'
        return render_template('login_5.html',errors=errors)

    my_user = users.query.filter_by(username=username_form).first()
    
    if my_user is None:
        errors='Такой пользователь отсутствует'
        return render_template('login_5.html',errors=errors)

    if not check_password_hash(my_user.password, password_form):
        errors = 'Введен неправильный пароль'
        return render_template('login_5.html', errors=errors)

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user,remember=False)
            return redirect('/lab6')
    return render_template('login_5.html',username=current_user.username)

@lab6.route("/lab6/articles")
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template('spisok_article.html',articles=my_articles)

@lab6.route('/lab6/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab6')

@lab6.route("/lab6/new_article", methods=['GET','POST'])
@login_required
def createArticle():
    errors = ''
    if request.method == "GET":
        return render_template("new_article.html")
    if request.method == "POST":
        is_public = False
        text_article = request.form.get("text_article")
        title = request.form.get("title_article")
        if len(text_article) == 0:
            errors = 'Заполните текст'
            return render_template("new_article.html", errors=errors)
        if 'is_public' in request.form:
            is_public = True
    new_article = articles(user_id=current_user.id, title=title, article_text=text_article, is_public=is_public)
    db.session.add(new_article)
    db.session.commit()

    return redirect(f"/lab6/articles/{new_article.id}")

@lab6.route('/lab6')
def all():
    if current_user.is_authenticated:
        visibleUser = current_user.username
    else:
        visibleUser = 'Anon'
    public_articles = articles.query.filter_by(is_public=True).all()
    return render_template('main_6.html', username=visibleUser,public_articles=public_articles)

@lab6.route("/lab6/articles/<int:article_id>")
@login_required
def like_article(article_id):
    article = articles.query.filter_by(id=article_id,user_id=current_user.id).first()
    if not article:
        return "Not found!"

    text = article.article_text.splitlines()
    return render_template('articleN.html',article_text=text,article_title=article.title,username=current_user.username)