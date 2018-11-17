import tweepy

auth = tweepy.OAuthHandler( "5GfAOVFbva56SfFRrxPwu6S7K", "FSrHlgAKFTRR3I7JTBeFCouweQpoqrPCHCZBAdKKYFUCrthbdy")
auth.set_access_token( "912719203689422854-4GmOCIIINULb4Dpwsefr8IciUKpSk4b",  "44bTrObNAjML1FAGLJDjUOQkYQYgvzjUaDeaZNF5jtn39")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)