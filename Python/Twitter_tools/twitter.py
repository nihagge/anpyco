#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

# argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '1sfCEr19Px0VMBRJrbEr3FaY1'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'vKen6YaghHZms7KvsEY0rON9ZaVE6HNrE58Z19o8BPughsoFEm'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3415136763-eJauHqdkJUDip2Bu0jaifoPZDk6bM8TcvnsaCYq'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'FWACspFFpDFubPzeiA9b59shqbvlfBkzrDJom5rVszV0z'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('test.txt','r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
