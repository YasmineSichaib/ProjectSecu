import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
tweets = api.mentions_timeline()

#Vérifier l'état de la connexion
try:
    api.verify_credentials()
    print('Vous êtes connecté!')
except: 
    print("Erreur de connexion.")

#Afficher mes tweets
print("Vos tweets : ")
for tweet in tweets:
    print('Nom du user : ' + tweet.user.name)
    print('Le tweet ID --> ' + str(tweet.id) + ' - Le tweet : ' + tweet.text)

#Afficher les abonnés
for follower in tweepy.Cursor(api.get_followers).items():
    print("Followers : " + follower.name)

print("Home tweets :")
for tweet in tweepy.Cursor(api.home_timeline).items(10):
    print(f"{tweet.user.name} tweet: {tweet.text}") 

print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

print('\nTweets avec hashtag : ')
for tweet in tweepy.Cursor(api.search_tweets, q = QUERY).items():
	try:
        
		print('\nTweet by: @' + tweet.user.screen_name)
		tweet.retweet()
		print('J''ai Retweet le tweet')

		# Favorite the tweet
		if LIKE:
			tweet.favorite()
			print('J''ai fav le tweet')

		# Follow the user who tweeted
		# check that bot is not already following the user
		if FOLLOW:
			if not tweet.user.following:
				tweet.user.follow()
				print('j''ai follow le compte ;)')

		sleep(SLEEP_TIME)

	except AttributeError  as e:
		print(e.reason)

	except StopIteration:
		break


