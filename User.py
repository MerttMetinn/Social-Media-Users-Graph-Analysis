class User():
    def __init__(self,username:str,name:str,followers_count:int,following_count:int,language:str,region:str,tweets:list,followers:list,following:list):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = tweets
        self.followers = followers
        self.following = following
    
    def __str__(self) -> str:
        return f"Username: {self.username}\nName: {self.name}\nFollowersCount: {self.followers_count}\nFollowingCount: {self.following_count}\nLanguage: {self.language}\nRegion: {self.region}\nTweets: {self.tweets}\nFollowers: {self.followers}\nFollowing: {self.following}"

    
