import weather_helper
import yelp_helper

def recommend_based_on_weather(state, city):
	#get the temp
	temp = weather_helper.fetch_weather(state, city);
	str_temp = str(temp)
	#based on the temp we are going to populate a search term for yelp
	search_term = 'indoor seating'    
	headline = "It feels like " + str_temp + " outside. How about eating somewhere inside. Pick one below."

	if(temp > 65):
		search_term = 'outdoor seating'
		headline = "It feels like " + str_temp + " outside. What a great day to go to an outdoor resturant. Pick one below."

	elif(temp < 40):
		search_term = 'soup'   
		headline = "It feels like " + str_temp + " outside. Better grub somewhere warm with soup. Pick one below."

	#hit the yelp API for resturants in our area using the search term
	resturants = yelp_helper.fetch_resturants(state, city, search_term);

	return {"resturants": resturants, "temp": temp, "headline": headline}