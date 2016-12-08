from flask import Flask 
from flask import render_template
from flask import request, url_for, redirect, session, g, flash
import resturant_recommender

app = Flask(__name__)

@app.route('/recomendations', methods=['GET'])
def list_recomendations():
	state = request.args.get("state")
	city = request.args.get("city")

	resturants = resturant_recommender.recommend_based_on_weather(state, city)
	return render_template('recomendations/list.html', resturants=resturants, state=state, city=city)


@app.route('/', methods=['GET'])
def default():
	return render_template('recomendations/index.html')

if __name__ == '__main__':
	# init_db()
	app.run(debug=True)