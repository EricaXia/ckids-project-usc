import instaloader

# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
L.login('musketeers1128@gmail.com', 'EvOu7CR7Iq2V')        # (login)
# L.interactive_login(USER)      # (ask password on terminal)
# L.load_session_from_file(USER)  # (load session created w/
# #  `instaloader -l USERNAME`)

L.download_hashtag('eatla', max_count=10)
