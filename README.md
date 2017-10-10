
Welp 

Welp is a restaurant recommender based on the weather
It uses two apis yelp and weather underground 


Getting Started 

1. clone to local 
2. cd welp



Create and run virtual environment on command line
3. pip install virtualenv
4. virtualenv ENV
5. source env/bin/activate

System dependancies are in requirements.txt
6. pip install -r requirements.txt


Runs flask app and starts server
7. python resturants.py 

8. open http://127.0.0.1:5000/

9. Type city and choose state from drop down then hit submit button 
 
Ex. San Francisco choose CA hit submit button 

It will grab the temperature from weather underground api 

    if temperature is greater than 65
        it will grab all resturants from yelp with outdoor seating
    else if temperature is less than 40
        it will grab all resturants from yelp that have soup
        






