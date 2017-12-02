from urllib2 import urlopen 
from config_secret import*
from urllib import pathname2url 
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    # token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)

client = Client(auth)

params = {
    'lang': 'en'
}


#search for and print businesses
def fetch_resturants(state, city, search_term):
    #go to yelp api and fetch business
    params['term'] = search_term;
    response= client.search(state + " " + city, **params)
    return response.businesses
   