import json,time,os,random
from User import User
from Dictionary import OptimizedDictionary
from faker import Faker
import networkx as nx
from tqdm import tqdm
import sys
import matplotlib.pyplot as plt
from UserHashData import UserHashData
from DirectedGraph import OptimizedDirectedGraph
from ArrayList import ArrayList
       

class App():
    def __init__(self) -> None:
        self.data = None
        self.hashtable = None
        self.all_users_graph = None
        self.max_common_words_without_hashtag = None
        self.max_common_words_with_hashtag = None
        self.users_with_topics = None
        
        self.hashtags = [
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
        
        
    def bind_values(self):
        self.load_data()
        self.set_hash_table()
        #self.init_all_users_graph()
        
    def are_all_items_unique(self,my_list):
        return len(my_list) == len(set(my_list))


    def load_data(self):
        with open("output.json","r",encoding="utf-8") as f:
            data = json.loads(f.read())
            
        self.data = data
            
            
    def set_hash_table(self):
        
        myDict = OptimizedDictionary(35000)
        
        for i in tqdm(self.data,desc="Veri Setine Atama"):
        
            myUser = User(i["username"],i["name"],i["followers_count"],i["following_count"],i["language"],i["region"],i["tweets"],i["followers"],i["following"])

            myDict.put(i["username"],myUser)
            
        self.hashtable = myDict
            
    def init_all_users_graph(self):

        all_users_graph = OptimizedDirectedGraph()

        for user in tqdm(self.hashtable.keys,desc="Tüm Kullanıcılar Bir Vertex Olarak Ekleniyor"):
            all_users_graph.add_vertex(user)

        for user in tqdm(self.hashtable.keys,desc="Tüm Kullanıcıların Takipçileri Birbirlerine Bağlanıyor"):
            for i in self.hashtable.get(user).followers:
                all_users_graph.add_edge(user,i)
                
        for user in tqdm(self.hashtable.keys,desc="Kullanıcının Takip Ettikleri İlgili Kullanıcıya Bağlanıyor"):
            for i in self.hashtable.get(user).following:
                all_users_graph.add_edge(i,user)
            
        self.all_users_graph = all_users_graph


    def set_max_common_words(self,count:int,with_hashtag=False):
        
        
        if(with_hashtag):
            if (self.max_common_words_with_hashtag is not None):
                top = self.max_common_words_with_hashtag[:count]

                labels, values = zip(*top)
                
                labels = list(labels)
                values = list(values)
                
                for i in range(len(labels)):
                    labels[i] = labels[i] + f"({values[i]})"

                plt.figure(figsize=(20, 10))

                plt.bar(labels, values)

                plt.xticks(rotation=45)

                plt.xlabel('Datalar')
                plt.ylabel('Sayılar')
                plt.title(f'En Çok Geçen {count} Etiket')
                plt.show()
            else:
                
                with open("stopwords.txt","r",encoding="utf-8") as f:
                    stops = f.read().strip().split("\n")
                    
                words = {}
                    
                for user in tqdm(self.data,desc="Kullanıcılarda Dolaşılıyor"):
                    for tweet in user["tweets"]:
                        
                        temp = str(tweet)
                        temp = temp.replace(".","").replace(",","").lower().strip().split(" ")
                                      

                        for word in temp:
                            if word in words and word not in stops:
                                words[word] += 1
                            else:
                                words[word] = 1

                                
                                    
                words = {key: value for key, value in words.items() if key and value}

                sorted_data = list(sorted(words.items(), key=lambda x: x[1], reverse=True))        
                      
                self.max_common_words_with_hashtag = sorted_data
                
                print(self.max_common_words_with_hashtag)

                top = sorted_data[:count]

                labels, values = zip(*top)
                
                labels = list(labels)
                values = list(values)

                for i in range(len(labels)):
                    labels[i] = labels[i] + f"({values[i]})"

                plt.figure(figsize=(20, 10))

                plt.bar(labels, values)

                plt.xticks(rotation=45)

                plt.xlabel('Datalar')
                plt.ylabel('Sayılar')
                plt.title(f'En Çok Geçen {count} Etiket')
                plt.show()
        else:
            if (self.max_common_words_without_hashtag is not None):
                top = self.max_common_words_without_hashtag[:count]

                labels, values = zip(*top)
                
                labels = list(labels)
                values = list(values)

                for i in range(len(labels)):
                    labels[i] = labels[i] + f"({values[i]})"

                plt.figure(figsize=(20, 10))

                plt.bar(labels, values)

                plt.xticks(rotation=45)

                plt.xlabel('Datalar')
                plt.ylabel('Sayılar')
                plt.title(f'En Çok Geçen {count} Etiket')
                plt.show()
            else:
                
                with open("stopwords.txt","r",encoding="utf-8") as f:
                    stops = f.read().strip().split("\n")
                    
                self.hashtags.extend(stops)
                    
                words = {}
                    
                for user in tqdm(self.data,desc="Kullanıcılarda Dolaşılıyor"):
                    for tweet in user["tweets"]:
                        
                        temp = str(tweet)
                        temp = temp.replace(".","").replace(",","").lower().strip().split(" ")
                        
                        for hashtag in self.hashtags:
                            if hashtag in temp:
                                temp.remove(hashtag)
                               
                        for word in temp:
                            if word in words:
                                words[word] += 1
                            else:
                                words[word] = 1
                                    
                words = {key: value for key, value in words.items() if key and value}

                sorted_data = list(sorted(words.items(), key=lambda x: x[1], reverse=True))
                
                self.max_common_words_without_hashtag = sorted_data
                
                print(self.max_common_words_without_hashtag)

                top = sorted_data[:count]

                labels, values = zip(*top)
                
                labels = list(labels)
                values = list(values)

                for i in range(len(labels)):
                    labels[i] = labels[i] + f"({values[i]})"

                plt.figure(figsize=(20, 10))

                plt.bar(labels, values)

                plt.xticks(rotation=45)

                plt.xlabel('Datalar')
                plt.ylabel('Sayılar')
                plt.title(f'En Çok Geçen {count} Etiket')
                plt.show()
    
    def findTopics(self):
        users_with_topics = OptimizedDictionary(30)
        
        _max30 = list(self.max_common_words_without_hashtag[:30])
        max30 = ArrayList()
        
        for topic,count in _max30:
            max30.add(topic)
        
        for topic in tqdm(max30,desc="findTopics"):
            print("Topic : " + topic)
                        
            for username in tqdm(self.hashtable.keys,desc="35k"):               
                        
                user = self.hashtable.get(username)
                
                for _tweet in user.tweets:
                    tweet = _tweet.split(" ")
                    if(topic in tweet):
                        varMi = users_with_topics.get(topic)
                        
                        if varMi is not None:
                            users = users_with_topics.get(topic)
                            if not users.contains(username):
                                users.add(username)
                                users_with_topics.put(topic,users)
                        else:
                            arr = ArrayList()
                            arr.add(username)
                            users_with_topics.put(topic,arr)

        mainstr = ""
                    
        for key in users_with_topics.keys:
            if(key is not None):
                mainstr+=key + ":" + str(users_with_topics.get(key)) + "\n\n\n"
                
        with open("report_without_hastag.txt","w",encoding="utf-8") as f:
            f.write(mainstr)
            
            
    def findTopicsByRegion(self):
        regions = ArrayList()
        regions.add("en")
        regions.add("tr")
        regions.add("de")
        regions.add("fr")
        regions.add("pl")
        
        topics_by_region = OptimizedDictionary(5)

        for username in tqdm(self.hashtable.keys,desc="findTopicsByRegionWorking"):
            user = self.hashtable.get(username)
            for tweet in user.tweets:
                temp = str(tweet)
                temp = temp.replace(".","").replace(",","").lower().strip().split(" ")
                
                for hashtag in self.hashtags:
                    if hashtag in temp:
                        temp.remove(hashtag)
                for word in temp:
                    varMi = topics_by_region.get(user.region)
                    if varMi is not None:
                        varMi.add(word)
                    else:
                        arr = ArrayList()
                        arr.add(word)
                        topics_by_region.put(user.region,arr)
                        
        
        for region in regions:
            print(region + " : ")
            print(topics_by_region.get(region).get_top_frequencies(10))
            
  
    def userGraph(self,username):
        graph = OptimizedDirectedGraph()
        
        graph.add_vertex(username)
        
        for follower in self.hashtable.get(username).followers:
            graph.add_vertex(follower)
            graph.add_edge(follower,username)
            
        for following in self.hashtable.get(username).following:
            graph.add_vertex(following)
            graph.add_edge(username,following)
        
            
        print(graph.display_graph())
        
        
        print("DFS")
        graph.dfs_iterative(username)

            
        graph2 = nx.DiGraph()

        for follower in self.hashtable.get(username).followers:
            graph2.add_node(follower)
            graph2.add_edge(follower, username)

        for following in self.hashtable.get(username).following:
            graph2.add_node(following)
            graph2.add_edge(username, following)

        pos = nx.spring_layout(graph2)  
        nx.draw(graph2, pos, with_labels=True, arrows=True)
        plt.show()
                          
    
    def findTopicsByLanguage(self):
        languages = ArrayList()
        languages.add("english")
        languages.add("turkish")
        languages.add("german")
        languages.add("french")
        languages.add("polish")
        
        topics_by_language = OptimizedDictionary(5)

        for username in tqdm(self.hashtable.keys,desc="findTopicsByLanguageWorking"):
            user = self.hashtable.get(username)
            for tweet in user.tweets:
                temp = str(tweet)
                temp = temp.replace(".","").replace(",","").lower().strip().split(" ")
                
                for hashtag in self.hashtags:
                    if hashtag in temp:
                        temp.remove(hashtag)
                for word in temp:
                    varMi = topics_by_language.get(user.language)
                    if varMi is not None:
                        varMi.add(word)
                    else:
                        arr = ArrayList()
                        arr.add(word)
                        topics_by_language.put(user.language,arr)
                        
        
        for language in languages:
            print(language + " : ")
            print(topics_by_language.get(language).get_top_frequencies(10))
            
    def show_all_users(self):
        for user in self.hashtable.keys:
            print(user)
            
    def find_same_following_count_users(self,username):
        
        print(username + " kullanıcısının takip edilen sayısı " + str(self.hashtable.get(username).following_count))

        for _username in self.hashtable.keys:
            if(self.hashtable.get(_username).following_count == self.hashtable.get(username).following_count):
                print(_username + " : " + str(self.hashtable.get(_username).following_count))
                
    def find_same_followers_count_users(self,username):
        
        print(username + " kullanıcısının takipçi sayısı " + str(self.hashtable.get(username).followers_count))

        for _username in self.hashtable.keys:
            if(self.hashtable.get(_username).followers_count == self.hashtable.get(username).followers_count):
                print(_username + " : " + str(self.hashtable.get(_username).followers_count))
                
                
    def dfs_with_keyword(self,username,keyword):
        graph = OptimizedDirectedGraph()
        graph.add_vertex(username)
        
        for tweet in self.hashtable.get(username).tweets:
            words = tweet.replace(".","").replace(",","").lower().strip().split(" ")
            for word in words:
                if word == keyword:
                    graph.add_vertex(tweet)
                    graph.add_edge(username,tweet)
                    break
                
        graph.dfs_iterative(username)

if __name__=="__main__":
    app = App()
    app.bind_values()
    
    while(True):
        a = input("1) En yaygın konular (hashtagsiz)\n2) En yaygın konular (hashtagli)\n3) Bütün kişileri dfs ile göster\n4) En yaygın 30 konuyu yazdır\n5) kişi bazlı konuları raporla\n6) Bölgeye göre konuları bul\n7) Dile göre konuları bul\n8) kişiye özgü graph oluştur ve DFS ile gez\n9) Tüm kullanıcıları yazdır\n10) kişiyle aynı takip edilen sayısı olan kullanıcıları yazdır\n11) kişiyle aynı takipçi sayısı olan kullanıcıları yazdır\n12) Belirli bir keyword'e göre tweetlerde DFS\n")
        if (a=="1"):
            ans = int(input("En yaygın kaç konuyu görmek istiyorsunuz (Önerilen 20):"))
            app.set_max_common_words(with_hashtag=False,count=ans)
        elif (a=="2"):
            ans = int(input("En yaygın kaç konuyu görmek istiyorsunuz (Önerilen 20):"))
            app.set_max_common_words(with_hashtag=True,count=ans)
            
        elif (a=="3"):
            ans = input("Hangi kullanıcıdan başlayayım : ")
            if (app.all_users_graph is None):
                auth = input("Graph oluşturulmamış. Oluşturmak istiyor musunuz (e/h):")
                if (auth=="e"):
                    app.init_all_users_graph()
                else:
                    continue
            else:
                if app.hashtable.get(ans) is None:
                    print("Kullanıcı bulunamadı")
                    continue
                app.all_users_graph.dfs_iterative(ans)
            
        elif (a=="4"):
            print("En yaygın 30 konu : ")
            if(app.max_common_words_with_hashtag is None or app.max_common_words_without_hashtag is None):
                print("Veri ataması için ilk başta 1. ve 2. komutu çalıştırın")
                continue
                
            print(app.max_common_words_with_hashtag[:30])
            print(app.max_common_words_without_hashtag[:30])
            
        elif (a=="5"):
            if (app.max_common_words_without_hashtag is None):
                print("İlk başta 1. komutu çalıştırın")
                continue
            app.findTopics()
            
        elif (a=="6"): 
            app.findTopicsByRegion()
        
        elif (a=="7"): 
            app.findTopicsByLanguage()
        
        elif(a=="8"):
            
            uname = input("Kullanici adi giriniz : ")
            
            if app.hashtable.get(uname) is None:
                print("Kullanici bulunamadi")
                continue
            app.userGraph(uname)
            
        elif(a=="9"):
            app.show_all_users()
            
        elif (a=="10"):
            uname = input("Kullanici adi giriniz:")
            if app.hashtable.get(uname) is None:
                print("Kullanici bulunamadi")
                continue
            app.find_same_following_count_users(uname)
        elif (a=="11"):
            uname = input("Kullanici adi giriniz:")
            if app.hashtable.get(uname) is None:
                print("Kullanici bulunamadi")
                continue
            app.find_same_followers_count_users(uname)
        elif (a=="12"):
            uname = input("Kullanici adi giriniz:")
            if app.hashtable.get(uname) is None:
                print("Kullanici bulunamadi")
                continue
            keyword = input("Keyword giriniz:")
            app.dfs_with_keyword(uname,keyword)
            
            
        

