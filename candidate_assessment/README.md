# Tweety

Tweety is a REST API which returns a word cloud for the last 24h for the hashtag #covid from Twitter

## Installation Instructions

Project was developed using ***Python 3.8.5***

Install the requirements to your environment from the candidate_assessment directory via the command:

```bash
pip install -r requirements.txt
```

The API can be run locally, using Django's own development server.  
Once the requirements have been installed to your environment run the following
commands in order to start the server:
```bash
python manage.py migrate
python manage.py runserver
```

````
(venv) path\to\candidate-assessment\candidate_assessment>python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
February 02, 2021 - 03:19:27
Django version 3.1.5, using settings 'my_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

````
## API Endpoints

Below you will find the api endpoints.  
The default admin endpoint from Django is included.  

#### Welcome endpoint.  
Requires a token for authorization.

##### Request
````http request
GET /tweety-api/
Authorization: Token {token}
Accept: : */*
````
##### Response
````http request
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
body: 
{
    "message": "Hello my name is Tweety!"
}
````

#### Register endpoint.  
Requires a username and a password.

##### Request
````http request
POST /tweety-api/register/
Accept: : */*
body:
{
    "username": "username_value",
    "password": "password_value"
}
````
##### Response
````http request
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
body: 
{
    "success": "True",
    "status code": 200,
    "message": "User: username_value registered successfully."
}
````

#### Token generation endpoint.  
Requires a username and a password for authorization.

##### Request
````http request
POST /tweety-api/token-auth/
Accept: : */*
body:
{
    "username": "username_value",
    "password": "password_value"
}
````
##### Response
````http request
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
body: 
{
    "token": "token_value"
}

````

#### Daily world cloud endpoint.  
Requires token for authorization.

##### Request
````http request
POST /tweety-api/tweet-word-cloud/
Authorization: Token {token}
Accept: : */*
body:
{
    "words": "any integer greater than 0",
    "response_format": "json or csv"
}
````
##### Response
````http request
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
body: 
{
    "words": ["a list of words in descending order"],
    "topic": "chosen topic is covid (surprisingly)",
    "first_tweet_timestamp": "timestamp_value",
    "last_tweet_timestamp": "timestamp_value",
}

````
OR
````http request
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Type: text/csv; charset=utf-8
body: 
words,topic,first_tweet_timestamp,last_tweet_timestamp
"comma separated string with all the words found","chosen topic is covid (surprisingly)","timestamp_value","timestamp_value"
````

### Request path in order to generate the tweet word cloud
```
/tweety-api/register/          # register
/tweety-api/token-auth/        # get the api token
/tweety-api/tweet-word-cloud/  # generate the word cloud
```
### Comments

A lot of comments reside within the code.  
Therefore, the documentation is really short. I am happy to delve into it in more detail, following our discussion.  
The code is pylinted and unittested.
