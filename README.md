# Introduction
This api provides data about tweets. Get tweets searching by user or hashtag.  
You can read documentation [here...](https://documenter.getpostman.com/view/1700393/RWgjZ2DU)  
The project is deployed on Heroku and can be accessed through this link: https://twittermicro.herokuapp.com/users/twitter

# Installation

1. Clone repository
```bash
$ git clone https://github.com/zshanabek/zhunisali-project
$ cd zhunisali-project
```
2. Install dependencies
```bash
$ pip install -r requirements.txt
```
3. Run server
```bash
$ python start.py
```
4. Get tweets
```bash
$ curl localhost:5000/users/zshanabek
```
Expect json response:
```json
{
  "tweets": [
    {
      "account": {
        "fullname": "Zhunisali Shanabek", 
        "href": "/zshanabek", 
        "id": "760766794940416000"
      }, 
      "date": "Fri, 28 Sep 2018 15:26:04 GMT", 
      "hashtags": [
        "#postmanclient"
      ], 
      "likes": 213, 
      "replies": 54, 
      "retweets": 42, 
      "text": "If you need to document your API, use @postmanclient. Excellent software.\n#postmanclient"
    }
  ]
}
```
# Unit tests
```bash
$ python3 unit_tests.py 
```
# Overview
You can set the limit of tweets in response by typing argument: `limit`.  
For example. `localhost:5000/users/zshanabek?limit=10`.  
Default is 30.

Only Python 3.6+ is supported
