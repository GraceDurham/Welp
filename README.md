# Welp 

Welp is a restaurant recommender that makes recommendations based on today's weather.
It uses two apis yelp and weather underground.


![alt text](https://raw.githubusercontent.com/GraceDurham/Welp/master/preview.gif)


## Getting Started 

```
git clone https://github.com/GraceDurham/Welp.git
cd welp
```
#### Create and run virtual environment on command line

```
pip install virtualenv
virtualenv ENV
source env/bin/activate
```

#### Install system dependancies 

```
pip install -r requirements.txt
```

#### Get Authentication from Yelp by obtaining Client ID and Secret

```
Go to https://www.yelp.com/developers/documentation/v3/authentication and log into Yelp.
Follow steps 1-3 in screen shot below to get client id, secret, and access token.
```

![alt text](https://raw.githubusercontent.com/GraceDurham/Welp/master/Yelp_Auth.png)

![alt text](https://raw.githubusercontent.com/GraceDurham/Welp/master/get_access_token.png)

![alt text](https://raw.githubusercontent.com/GraceDurham/Welp/master/response_body.png)


#### Runs flask app (start server)

```
python resturants.py 
```

#### Profit

open http://127.0.0.1:5000/


## Using welp

Type city and choose state from drop down then hit submit button 
 
Ex. San Francisco choose CA hit submit button 
