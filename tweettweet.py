#Generous bot
import tweepy
import time

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
user=api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

# public_tweets=api.home_timeline()
# for tweet in public_tweets:
# 	print(tweet.text)


def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	#if follower.name=='abcd':
	if follower.followers_count>=18:
		follower.follow()
		break

# public_tweets=api.home_timeline()
# for tweet in public_tweets:
# 	print(tweet.text)





