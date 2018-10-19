import tweepy
from tweepy import OAuthHandler
from tweepy import Cursor 
import re # regular expression
from textblob import TextBlob #text/tweet parse


ck="Jm6WDXZuiwlwUnT9mFbPdSpcg"
cs="Wp4Gbf74R6MZWjXvj0ifKrCobwWbchhn53Mv8L7VMLbIUi6Wnd"
at="919434545924935681-wFjVVTbs0pmyB2VwSoj4VwGb7tBYCyr"
ats ="RaPfxU0rSMjkS3MSI9N0ztXu4I2iLMecXg79OerNHw4Ly"


auth = OAuthHandler(ck, cs)
# set access token and secret
auth.set_access_token(at, ats)

# create tweepy API object to fetch tweets
api = tweepy.API(auth)

#print(api,' login success ')

def getSentiment(tweet):
     
        analysis = TextBlob(tweet)
        #print(analysis)
        #print(analysis.sentiment.polarity)
        
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'    
        

def cleanData(tweet):
     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())     

def getTweets(p,coun):
     tweets = api.search(q=p,count=coun)
     pc = 0
     nc = 0
     netc = 0
     for t in tweets:
        tweetlist=  cleanData(t.text)
        #print(tweetlist)
        data = getSentiment(tweetlist)
        tweetdata = []
        tweetdata.append(data)
        
        
        for  t in tweetdata:
             if t == 'positive':
                    pc =pc+1
             elif t == 'negative':
                  nc = nc+1
             else:
                  netc = netc+1
     #print('user name :',p)
     #print ('positive count ',pc)
     #print ('negative count ',nc)
     #print ('neutral count ',netc)
     sent=[]
     sent.append(pc)
     sent.append(nc)
     sent.append(netc)
     return sent             

user=api.get_user('shreya73767208')
#print user.screen_name
def frndz1(n):

    user=api.get_user(n)
    ct=0
    person=[]
    list2=[]
    
    for friend in user.friends(count=200):
        
        #print friend.screen_name
        ct=ct+1
        
    
        #list2=[]	

        list2.append(friend.screen_name)
        
    list1=list(list2)
    list2=[]
    for l in list1:
        list3=[]
        data1=getTweets(l,40) 
        #print data1
        user = api.get_user(id = l)
        sc = user.screen_name
        
        user_profile = api.get_user(screen_name=sc)
        data = []
        data.append(['ID         ',user_profile.id]);
        data.append(['Screen Name',user_profile.screen_name]);
        data.append(['Name       ',user_profile.name]);
        data.append(['Followers  ',user_profile.followers_count]);
        data.append(['Location   ',user_profile.location])
        data.append(['Description',user_profile.description])
        data.append(['FriendCount',user_profile.friends_count])
        data.append(['Joined At  ',user_profile.created_at])
     
        #print(str(data[0]) + ' : ' + str(data[1]) + ' : ' + str(data[6]))
        l3=str(data[6]).split(',')
        list3.append(l)
        list3.append((l3[1].replace(']','')).replace(' ',''))
        list2.append(list3)
    return(list2)
       
#frndz1('shreya73767208')
        
       
        

        







            
