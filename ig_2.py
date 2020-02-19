import instaloader
import itertools

L = instaloader.Instaloader()
L.login('musketeers1128@gmail.com', 'EvOu7CR7Iq2V')        # (login)

# TODO: look into itertools techniques

f = L.get_hashtag_posts('dinela')

for post in itertools.islice(f, 10):
    L.download_post(post, target='#dinela')
