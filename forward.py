import praw
import urllib.request
from telethon.tl.functions.messages import UploadMediaRequest
from telethon.tl.types import MessageMediaPhoto
from telethon.sync import TelegramClient
from telethon import functions, types
import time
import os
reddit = praw.Reddit(client_id='',
                     client_secret='', 
                     password='',
                     user_agent='', 
                     username='')
name =""
api_id = ""
api_hash =""

def get_hot():
    return list(reddit.subreddit('').hot(limit=100))
ref_hot = get_hot()
count = 0
while True:
    time.sleep(300)
    now_hot = get_hot()
    for post in now_hot:
        if post not in ref_hot:
            print("New post in hot listings")
            url = str(post.url)
            if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
                urllib.request.urlretrieve(url, f"image{count}.jpeg")
                with TelegramClient(name, api_id, api_hash) as client:
                    client.send_file("CHANNEL_USERNAME", f"image{count}.jpeg", caption=post.title)
                os.remove(f"image{count}.jpeg")
                count += 1
    ref_hot = now_hot