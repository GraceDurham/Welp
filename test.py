import resturant_recommender

resturants = resturant_recommender.recommend_based_on_weather("MO", "Kansas City")

for resturant in resturants:
	print resturant.name
	print resturant.image_url
	print 

