from flask import render_template
from app import app 
from .request import get_news,get_headlines

#Views 
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its date 
    '''
      # Getting news news 
    sources = get_news() 
  

    print(sources)
    title = 'Home - Welcome to News Highlight'
    return render_template('index.html',title = title , sources = sources)

@app.route('/news/<sources_id>')
def news(sources):

  '''
  View news page function that returns the news details page and its data
  '''

  news = get_headlines(sources)
  print(news)
  
  
  return render_template('news.html',news = news)