from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news
from ..models import News

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    highlight = get_news()
    print(highlight)
    title = 'Home - News'
    return render_template('index.html' , title=title,highlights=highlight)


@main.route('/article/<int:id>')
def article(id):
    '''
    view news and returns the news details
    '''
    article = article_source(id)
    return render_template('article.html' , articles = articles , id=id)