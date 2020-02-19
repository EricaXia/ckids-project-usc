import instaloader
import itertools

L = instaloader.Instaloader()
L.login('musketeers1128@gmail.com', 'EvOu7CR7Iq2V')

hashtags = ["lafoodie", "laeats", "dinela",
            "eaterla", "lafood"]


for h in hashtags:
    L.download_hashtag(h, max_count=15)
