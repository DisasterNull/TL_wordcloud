import tweepy
import api
import config

ls = tweepy.Cursor(api.API.get_list_members, list_id=config.list_ID).items()
fs = tweepy.Cursor(api.API.get_friends).items()
add_list = []

lists = [l.screen_name for l in ls]
friends = [f.screen_name for f in fs]

for f in friends:
    result = f not in lists
    if result:
        add_list.append(f)

for a in add_list:
    api.API.add_list_member(list_id=config.list_ID, screen_name=a)
