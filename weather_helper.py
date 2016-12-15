
from config_secret import*
from urllib import pathname2url 
from urllib2 import urlopen 
from json import load 

#takes a city and state and returns the wether
def fetch_weather(city, state):
	url_base = 'http://api.wunderground.com/api/' + weather_underground_key
	apiUrl = url_base+"/conditions/q/"+pathname2url(state)+"/"+pathname2url(city)+".json"

	response=urlopen(apiUrl)

	json_obj=load(response)

	if json_obj.get("current_observation"):
		return int(json_obj["current_observation"]["feelslike_f"])

	return 0   
