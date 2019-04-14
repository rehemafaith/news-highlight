from app import app 
import urllib.request,json
from .models import newsource

Newsource = newsource.Newsource

#Getting the api key 
api_key = app.config['NEWS_API_KEY']

# Getting the news base url 
base_url = app.config["NEWS_API_BASE_URL"]


def get_newsource(source):
    '''
    