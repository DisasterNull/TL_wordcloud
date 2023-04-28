from pyknp import Jumanpp
from wordcloud import WordCloud
import api
import config
import datetime

font_pass = "/System/Library/Fonts/ヒラギノ角ゴシック W1.ttc"

f = open("/Users/nene/TL/stop_words.txt", "r")
word = f.read()
f.close()
stop_words = word.split()
dt_now = datetime.datetime.now()
print(dt_now)
tweet = ""
try:
    for i in range(24):
        num = str(i).zfill(2)
        print(dt_now.strftime('%Y%m%d')+"_"+num)
        f = open(f"/Users/nene/TL/tweets/"+dt_now.strftime('%Y%m%d')+"_"+num+"tweet.txt", "r")
        tweet += f.readline()
        f.close()
except:
    print("終わり")

wc = WordCloud(font_path=font_pass, width=1200, height=675, background_color="white", stopwords=set(stop_words), max_words=500, collocations=False,).generate(tweet)
wc.to_file('/Users/nene/TL/pictures/'+dt_now.strftime('%Y年%m月%d日')+'result.png')

api.API.update_status_with_media(status="""
#今日のTLWordCloud
改善点があればこのツイートのリプライか@disaster_kasu5にメンションしてください。
""",
                             filename='/Users/nene/TL/pictures/'+dt_now.strftime('%Y年%m月%d日')+'result.png')

ts = api.API.list_timeline(owner_screen_name=config.screen_name, slug=config.list_ID, count=1)
f = open("/Users/nene/TL/tweet_id.txt", "w")
f.write(str(ts[0].id))
f.close()


