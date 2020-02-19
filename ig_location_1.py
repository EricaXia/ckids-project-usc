""" 
(Can find Loc ID in web URL on Instagram location page,
or check the database file link in README)

Popular Location IDS in LA:
212999109 - Los Angeles
1865514327051885 - DTLA
495901727445891 - DTLA

 """

import instaloader

L = instaloader.Instaloader()

L.login('musketeers1128@gmail.com', 'EvOu7CR7Iq2V')

L.download_location("1865514327051885",
                    max_count=15,
                    # filter by specific hashtag in post's caption
                    post_filter=lambda post: "food" in post.caption_hashtags,
                    fast_update=True)


""" 
To improve on:
1. Get only one photo per post, not all of them?
2. Better way to filter out non-food posts
3. Get other relevant data
 """
