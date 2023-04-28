import tweepy
from janome.tokenizer import Tokenizer
import api
import config

try:
    f = open(config.tweet_path, "x", encoding='utf-8')
    f.write("")
    f.close()
except FileExistsError as e:
    print(e)

f = open("/Users/nene/TL/tweet_id.txt", "r")
tweet_id = f.readline()
f.close()

tts = tweepy.Cursor(api.API.list_timeline, owner_screen_name=config.screen_name, slug=config.list_ID, since_id=tweet_id).items()
t_lists = []
text = ""
for tt in tts:
    twbe = tt.text
    tw = twbe.strip().replace(' ', '')
    k = 0
    while "@" in tw:
        for i, t in enumerate(tw):
            if t == "@":
                k = i
            elif t == " ":
                tw = tw.replace(tw[k:i + 1], "")
                break
            elif i == len(tw)-1:
                tw = tw.replace(tw[k:], "")
                break
    while "#" in tw:
        for i, t in enumerate(tw):
            if t == "#":
                tw = tw.replace(tw[i], "")
                break
    if "RT" in tw:
        tw = tw.replace(tw[:2], "")
    while "https" in tw:
        for i, t in enumerate(tw):
            try:
                if t == "h" and tw[i + 1] == "t":
                    tw = tw.replace(tw[i:i + 23], "")
            except IndexError:
                if t == "h":
                    tw = tw.replace(tw[i:i + 23], "")
    t_lists.append(tw)
t = Tokenizer("/Users/nene/TL/user_dictionary.csv", udic_enc="utf8")
for tw in t_lists:
    tts = [token.surface for token in t.tokenize(tw) if token.part_of_speech.startswith('名詞')]
    for ts in tts:
        text += " " + ts

f = open(config.tweet_path, "a", encoding='utf-8')
f.write(text)
f.close()

t = api.API.list_timeline(owner_screen_name=config.screen_name, slug=config.list_ID, count=1, since_id=tweet_id)
if len(t) != 0:
    f = open("/Users/nene/TL/tweet_id.txt", "w")
    f.write(str(t[0].id))
    f.close()
