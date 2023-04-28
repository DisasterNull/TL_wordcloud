import os
from dotenv import load_dotenv
import datetime
load_dotenv()
dt_now = datetime.datetime.now()

# 環境変数を参照
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
screen_name = os.environ.get("SCREEN_NAME")
list_ID = os.environ.get("LIST_ID")

tweet_path = f"/Users/nene/TL/tweets/{dt_now.strftime('%Y%m%d_%H')}tweet.txt"
