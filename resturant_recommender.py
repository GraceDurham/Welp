import weather_helper
import yelp_helper

def recommend_based_on_weather(state, city):
	#get the temp
	weather = weather_helper.fetch_weather(state, city);
	
	#based on the temp we are going to populate a search term for yelp
	search_term = 'indoor seating'    
	
	if(weather > 65):
		search_term = 'outdoor seating'
	elif(weather < 40):
		search_term = 'soup'

	#hit the yelp API for resturants in our area using the search term
	resturants = yelp_helper.fetch_resturants(state, city, search_term);

	return resturants