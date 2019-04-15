from flask import render_template
from app import app 
from .request import get_news

#Views 
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its date 
    '''
      # Getting news news 
    sources = get_news('sources')
  

    print(sources)
    title = 'Home - Welcome to News Highlight'
    return render_template('index.html',title = title , sources = sources)

@app.route('/news/<news_id>')
def news(news_id):

  '''
  View news page function that returns the news details page and its data
  '''
  return render_template('news.html',id = news_id)