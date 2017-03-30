import tweepy

class Twitter:
    def __init__(self):
        self.key="XXXXXXXXX"
        self.secretKey="XXXXXXXXXXXXXXXX"
        self.access = "XXXXXXXXXXXX"
        self.secretAccess = "XXXXXXXXXXXXXXXXXXXX"
        self.auth=""
        self.api =""
    def connect(self):
        self.auth = tweepy.OAuthHandler(self.key, self.secretKey)
        self.auth.set_access_token(self.access, self.secretAccess)
        self.api = tweepy.API(self.auth)
    def tweet(self,message):
        self.api.update_status(message)