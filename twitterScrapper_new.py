from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# paste your credentials

ACCESS_TOKEN = "gGbTf3ngGjFS1LKNyTDk9TRJVoYbuv"
ACCESS_TOKEN_SECRET = "gIfCnKDEgF71AVIaasJrBAg"
CONSUMER_KEY = "2Z05K2pb2j"
CONSUMER_SECRET = "tpKhuMXpuoZXjdhzF78Bb" 


"""
CONSUMER_KEY ="Jm6WDdSpcg"
CONSUMER_SECRET ="Wp4Gbf74R6MZwWbchhn53Mv8L7VMLbIUi6Wnd"
ACCESS_TOKEN ="919434545yB2VwSoj4VwGb7tBYCyr"
ACCESS_TOKEN_SECRET ="RaPfxU0rSMjkS3MSI9N0ztu4I2iLMecXg79OerNHw4Ly"
"""


# twitter authenticator #
class TwitterAuthenticator():
	def AuthenticateTwitterApp(self):
				
		auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
		return auth 

class TweetAnalyzer():
	"""
	Functionalites for analyzinz and categorizing twets

	"""
	def CleanTweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\s+)"," ",tweet).split())

	def AnalyzeSentiment(self, tweet):
		
		analysis = TextBlob(self.CleanTweet(tweet))

		if analysis.sentiment.polarity > 0:
			
			return 1
		elif analysis.sentiment.polarity == 0:
			return 0
		else:
			return -1

	def getTweets(self, tweets):
	     #tweets = api.search(q=p,count=count)
	     pc = 0
	     nc = 0
	     netc = 0
	     for t in tweets:
		tweetlist =  self.CleanTweet(t.text)
		#print(tweetlist)
		data = self.AnalyzeSentiment(tweetlist)
		tweetdata = []
		tweetdata.append(data)
		
		
		for  t in tweetdata:
		     if t == 1:
		            pc =pc+1
		     elif t == -1:
		          nc = nc+1
		     else:
		          netc = netc+1
	     sent=[]
	     sent.append(pc)
	     sent.append(nc)
	     sent.append(netc)
	     return sent 
		
	def TweetsToDataFrame(self, tweets):
		df = pd.DataFrame(data = [tweet.text for tweet in tweets], columns=['tweets'])
		df['id'] = np.array([tweet.id for tweet in tweets])
		df['len'] = np.array([len(tweet.text) for tweet in tweets])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['source'] = np.array([tweet.source for tweet in tweets])
		df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
		df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

		return df

	def GetMaximumRetweetCount(self,df):
		# Get the number of Retweets for the maximum time retweeted tweet
		print("Retweet "+str(np.max(df['retweets'])))
		
	
	
	def GetMaximumLikesCount(self,df):
		# Get the number of Retweets for the maximum time retweeted tweet
		print("Likes "+str(np.max(df['likes'])))

	def GetAverageTweetLength(self,df):
		# Get average length over all tweets	
		print("Average Length of tweets "+ str(np.mean(df['len'])))	
	
	def GetLikesTimeSeries(self,df):
		# Time Series for Likes
		time_likes = pd.Series(data = df['likes'].values, index=df['date'])
		time_likes.plot(figsize=(16, 4), color='r', title='Likes')
		plt.show()
		
	def GetRetweetsTimeSeries(self,df):
		# Time Series for Retweets
		time_retweets = pd.Series(data = df['retweets'].values, index=df['date'])
		time_retweets.plot(figsize=(16, 4), color='r', title='Retweets')
		plt.show()

	def GetTimeSeries(self,df):
		# Time Series for Likes and Retweets

		time_retweets = pd.Series(data = df['retweets'].values, index=df['date'])
		time_retweets.plot(figsize=(16, 4), label='Retweets', legend=True)
		
		time_likes = pd.Series(data = df['likes'].values, index=df['date'])
		time_likes.plot(figsize=(16, 4), label='Likes', legend=True)
		
		plt.show()

class TwitterClient():
	tweet_analyzer = TweetAnalyzer()
	def __init__(self,twitter_user=None):
		self.auth = TwitterAuthenticator().AuthenticateTwitterApp()
		self.twitter_client = API(self.auth)
		self.twitter_user = twitter_user

    	def GetClientAPI(self):
		return self.twitter_client
		
	def GetScreenName(self,api,user_id):
		user = api.get_user(id = user_id)
		screen_name = user.screen_name;
		return screen_name

	def GetFollowerList(self,api,screen_name):
		
		for follower_id in Cursor(api.followers_ids, screen_name = screen_name).items():
			sc = self.GetScreenName(api,follower_id)	
			data = self.GetUserProfileDetails(api,sc)
			print(str(data[0]) + ' : ' + str(data[1]))

	def GetFriendList(self,api,screen_name):
		filename="followers.csv"
		f=open(filename,"w+")
		headers="Name,friends,Positive,Negative,Neutral"
		f.write(headers+"\n")
		print('\t:\t Screen_name\t:\tName\t:\tFriends\t:\tPositiveCount\t:\tNegativeCount\t:\tNeutralCount')

		for friend_id in Cursor(api.friends_ids, screen_name = screen_name).items():
			sc = self.GetScreenName(api,friend_id)
			friend = self.GetUserProfileDetails(api,sc)
			c1 = friend[1][1].encode("utf-8") # get screen_name of each friend
			c2 = friend[2][1].encode("utf-8") # get name of the friend
			c3 = friend[6][1] # get friend count
			tweets = api.search(q = c1, count = 40)
			counts = tweet_analyzer.getTweets(tweets)

			print('\t:\t '+c1+'\t:\t'+c2+'\t:\t'+str(c3)+'\t:\t' + str(counts[0])+'\t:\t'+str(counts[1])+'\t:\t'+str(counts[2])+"\n")
			
			f.write(c1 +","+ c2 +","+str(counts[0])+","+str(counts[1])+","+str(counts[2])+"\n")
		
		f.close()
		
	

			

		
	def GetUserProfileDetails(self,api,screen_name):
		user_profile = api.get_user(screen_name=screen_name)
		data = []
		data.append(['ID          	',user_profile.id]);
		data.append(['Screen Name	',user_profile.screen_name]);
		data.append(['Name       	',user_profile.name]);
		data.append(['FollowerCount	',user_profile.followers_count]);
		data.append(['Location   	',user_profile.location])
		data.append(['Description	',user_profile.description])
		data.append(['FriendCount	',user_profile.friends_count])
		data.append(['Joined At  	',user_profile.created_at])
		return data		

	

	

		
if __name__ == '__main__':
	twitter_client = TwitterClient()
	tweet_analyzer = TweetAnalyzer()
	api = twitter_client.GetClientAPI()

	user_id = ACCESS_TOKEN[0:19]; #fetch user_id from ACCESS_TOKEN
	#print(user_id)

	sn = twitter_client.GetScreenName(api,user_id); # get screen_name 
	#sn = 'shreya73767208'

	#print(sn)
	
	print("\nBasic Profile Details")
	data = twitter_client.GetUserProfileDetails(api,sn)
	for i in data:
		print(str(i[0]) + ' : ' + str(i[1]))

	
	
	
	print("Followed By " + data[2][1] )	
	twitter_client.GetFriendList(api,sn)

	
	
	
	#print("\nFollowers of " + data[2][1]  )	
	#data = followers = twitter_client.GetFollowerList(api,sn)

	
	# analyze tweets


	#df = pd.DataFrame
	#tweets = api.user_timeline(screen_name=sn, count=30)
	#df = tweet_analyzer.TweetsToDataFrame(tweets) # df = pd.DataFrame 
	
	# Sentiment Analysis
	#df['sentiment'] = np.array([tweet_analyzer.AnalyzeSentiment(tweet) for tweet in df['tweets']])
	#print(df.head(10))
		
		
	# Get Maximum retweet count
	#print(tweet_analyzer.GetMaximumRetweetCount(df))

	# Get maximum likes count
	#print(tweet_analyzer.GetMaximumLikesCount(df))	

	# Display Likes and retweets time series
	# tweet_analyzer.GetTimeSeries(df)
