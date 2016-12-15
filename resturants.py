from flask import Flask 
from flask import render_template
from flask import request, url_for, redirect, session, g, flash
import resturant_recommender

app = Flask(__name__, static_url_path='')

@app.route('/recomendations', methods=['GET'])
def list_recomendations():
	state = request.args.get("state")
	city = request.args.get("city")

	recommendation_info = resturant_recommender.recommend_based_on_weather(state, city)
	resturants = recommendation_info["resturants"]
	temp = recommendation_info["temp"]
	headline = recommendation_info["headline"]

	return render_template('recomendations/list.html', headline=headline, temp=temp, resturants=resturants, state=state, city=city)


@app.route('/', methods=['GET'])
def default():
	return render_template('recomendations/index.html')

if __name__ == '__main__':
	# init_db()
	app.run(debug=True)