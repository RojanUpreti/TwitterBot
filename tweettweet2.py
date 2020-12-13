
##Narcissit bot
import tweepy
import time

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
user=api.me()


def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)


search_string='Rojan'
numberOfTweets=2


for tweet in tweepy.Cursor(api.search,search_string).items(numberOfTweets):
	try:
		#tweet.retweet()
		tweet.favorite()
		print('I liked this tweet')

	except tweepy.TweepError as e:
		print(e.reason)

	except StopIteration:
		break

