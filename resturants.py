from flask import Flask 
from flask import render_template
from flask import request, url_for, redirect, session, g, flash
import resturant_recommender

app = Flask(__name__)

@app.route('/recomendations', methods=['GET'])
def list_recomendations():
	resturants = resturant_recommender.recommend_based_on_weather("MO", "Kansas City")
	return render_template('recomendations/list.html', resturants=resturants)

if __name__ == '__main__':
	# init_db()
	app.run(debug=True)