import datetime

from wordcloud import WordCloud

import api

date = datetime.datetime.now()
dt2 = date + datetime.timedelta(minutes=-1)

now = dt2.strftime('%Y-%m-%d_%H:%M:%S')
qer = "#TLwordcloud since:" + now + "_JST filter:follows"
print(qer)
for t in api.API.search_tweets(q=qer):

    text = t.text
    if "@disaster_kasu5" in text:
        print(text)
        text1 = text.replace("#TLwordcloud", "")
        text2 = text1.replace("@disaster_kasu5", "")
        text3 = text2.replace(" ", "")
        text4 = text3.replace("　", "").replace("\n", "")
        font_pass = "/System/Library/Fonts/ヒラギノ角ゴシック W1.ttc"
        f = open("/Users/nene/TL/stop_words.txt", "r")
        word = f.read()
        f.close()
        stop_words = word.split()
        try:
            if text4[11] == "~":
                text4 = text4[:14]
                num = text4[9:14].replace("~", " ").split()
                tweet = ""
                i = int(num[0])
                while i <= int(num[1]):
                    f = open(f"/Users/nene/TL/tweets/{text4[:9] + str(i).zfill(2)}tweet.txt", "r")
                    tweet += f.readline()
                    f.close()
                    i += 1
            else:
                text4 = text4[:11]
                f = open(f"/Users/nene/TL/tweets/{text4}tweet.txt", "r")
                tweet = f.readline()
                f.close()
        except:
            text4 = text4[:11]
            f = open(f"/Users/nene/TL/tweets/{text4}tweet.txt", "r")
            tweet = f.readline()
            f.close()

        wc = WordCloud(font_path=font_pass, width=1200, height=675, background_color="white", stopwords=set(stop_words),
                       max_words=500, collocations=False, ).generate(tweet)
        wc.to_file('/Users/nene/TL/pictures/' + text4 + 'result.png')
        mes = "@"+str(t.user.screen_name)
        print(mes)
        api.API.update_status_with_media(status=mes, filename='/Users/nene/TL/pictures/' + text4 + 'result.png',
                                         in_reply_to_status_id=t.id)
