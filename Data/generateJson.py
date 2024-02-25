import json,random
from faker import Faker
from tqdm import tqdm

def generateHashtag():
    mainstr = ""
    hashtags = [
        "#love",
        "#instagood",
        "#fashion",
        "#photooftheday",
        "#photography",
        "#art",
        "#beautiful",
        "#nature",
        "#picoftheday",
        "#happy",
        "#follow",
        "#travel",
        "#cute",
        "#style",
        "#instadaily",
        "#tbt",
        "#followme",
        "#summer",
        "#beauty",
        "#fitness",
        "#like4like",
        "#food",
        "#instalike",
        "#photo",
        "#selfie",
        "#friends",
        "#music",
        "#smile",
        "#family",
        "#life",
        "#fun",
        "#girl",
        "#likeforlikes",
        "#motivation",
        "#lifestyle",
        "#likeforlike",
        "#sunset",
        "#amazing",
        "#nofilter",
        "#instamood",
        "#sun",
        "#follow4follow",
        "#inspiration",
        "#followforfollow",
        "#instapic",
        "#bestoftheday",
        "#cool",
        "#swag",
        "#night",
        "#happybirthday",
        "#smallbusiness",
        "#business",
        "#entrepreneur",
        "#socialmedia",
        "#digitalmarketing",
        "#sales",
        "#tech",
        "#leadership",
        "#innovation",
        "#networking",
        "#seo",
        "#contentmarketing",
        "#marketingstrategy",
        "#businesstips",
        "#startups",
        "#productivity",
        "#strategy",
        "#b2b",
        "#consulting",
        "#workplace",
        "#professionaldevelopment",
        "#leadgeneration",
        "#b2bmarketing",
        "#saas",
        "#thoughtleadership",
        "#artist",
        "#drawing",
        "#artwork",
        "#digitalart",
        "#artistsoninstagram",
        "#draw",
        "#instaart",
        "#artoftheday",
        "#contemporaryart",
        "#paint",
        "#abstractart",
        "#artgallery",
        "#artistic",
        "#artofinstagram",
        "#artcollector",
        "#modernart",
        "#tattooart",
        "#urbanart",
        "#picsart",
        "#artists",
        "#artlover",
        "#artdaily",
        "#artjournal"
    ]
    
    hashtags = list(set(hashtags))
    
    tags = random.sample(hashtags,random.randint(1,10))
    for i in tags:
        mainstr+=" "+i
    return mainstr
    
def getOutput():

    datas = []
    usernames = []
    names = []
    regions = ["en","tr","de","fr","pl"]
    languages = ["english","turkish","german","french","polish"]
    

    faker = Faker()

    username = ""
    name = ""
    followers_count = 0
    following_count = 0
    language = ""
    region = ""
    tweets = []
    tweet_count = 0


    for i in tqdm(range(35000),desc="Değer Atama"):
        tweets.clear()
        newDict = {}
    
        username = faker.unique.user_name()
    
        usernames.append(username)
        name = faker.name()
        names.append(name)
        
        region = random.choice(regions)
        language = random.choice(languages)
        
        followers_count = random.randint(1,20)
        tweet_count = random.randint(10,30)
        
        newDict["username"] = username
        newDict["name"] = name
        newDict["followers_count"] = followers_count
        newDict["following_count"] = 0
        newDict["language"] = language
        newDict["region"] = region
        newDict["tweet_count"] = tweet_count
        newDict["tweets"] = []
        newDict["followers"] = []
        newDict["following"] = []

        datas.append(newDict)
        
        
    for data in tqdm(datas,desc="Tweet-Takipçi-Takip Edilen ataması"):
        
        for i in range(data["tweet_count"]):
            data["tweets"].append(faker.sentence() + generateHashtag())
            
        
        data["followers"] = random.sample(usernames,data["followers_count"])      
        
        
        try:
            data["followers"].remove(data["username"]) 
        except:
            pass

    for user in tqdm(datas,desc="Takipçiler Atanıyor"):
        counter = 0
        for followers in user["followers"]:
            datas[usernames.index(followers)]["following"].append(user["username"])
            counter+=1
            
        try:
            data["following"].remove(data["username"]) 
        except:
            pass
        
    for user in tqdm(datas,desc="Takipçi Sayısı Ataması"):
        user["following_count"] = len(user["following"])
        
    try:
        data["following"].remove(data["username"]) 
    except:
        pass
        
    return datas
        
   
if __name__=="__main__": 
    
    datas = getOutput()
    
    with open("output.json", "w") as json_file:
        json.dump(datas, json_file, indent=3) 