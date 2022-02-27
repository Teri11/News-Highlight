from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,search_news, sources_news
from ..models import Sources

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    Trending_news = get_news()
    print(Trending_news)
    title = 'Home - News'
    return render_template('index.html' , title=title,Trending = Trending_news)


@main.route('/article/<int:id>')
def article(id):
    '''
    view news and returns the news details
    '''
    article = article_source(id)
    return render_template('article.html' , articles = articles , id=id)