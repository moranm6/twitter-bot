# Importing the module
from twython import Twython, TwythonError

#Setting these as variables will make them easier for future edits
app_key = ""
app_secret = ""
oauth_token = ""
oauth_token_secret = ""

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

naughty_words = ["follows", "RT", "SEX", "followers"]
good_words = ['"retweet to win"', '"RT to win"', '"RT for chance"', 
'"retweet for chance"', '"RT to #win"', '"retweet to #win"', '#giveaway', ]

filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

def add(tweet, screen_names):
	for id in screen_names:
		twitter.create_friendship(user_id = id)

def destroy(tweet, num):
	# else destroy the oldest friend(s)
	last_screen_names = bot_friends["ids"][-num]
	for id in last_screen_names:
		twitter.friendships_destroy(user_id = id)


def follow(tweet):
	print(tweet["text"])
	bot_friends = twitter.get_friends_ids(screen_name = "n1mbusKid", count=2000)

	print("bot friends: ")
	print(len(bot_friends["ids"]))

	screen_names = [tweet["user"]["id_str"]]

	if "entities" in tweet:	
		if "user_mentions" in tweet["entities"]:
			user_mentions = tweet["entities"]["user_mentions"]

	for mention in user_mentions:
		screen_names.append(mention["id_str"])

	if len(bot_friends["ids"]) > 2000 - len(screen_names):
		destroy(tweet, len(screen_names))
	
	add(tweet, screen_names)
		
			
search_results = twitter.search(q=keywords, lang="en")
try:
	for tweet in search_results["statuses"]:
		try:
			if "retweeted_status" not in tweet and "quoted_status" not in tweet:	
				#tweet is candidate tweet and is not a quoted tweet
				twitter.retweet(id = tweet["id_str"])			

				if "follow" or "Follow" or "#follow" or "FOLLOW" in tweet["text"]:
					follow(tweet)
							
		except TwythonError as e:
			print(e)
except TwythonError as e:
	print(e)


