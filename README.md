# Web Scraping from IG
<br>
Credit to InstaLoader IG Scraper Python Tool
<br>
### Create an Instaloader() object
`loader = Instaloader()`

Functions we can use to scrape:
<br><br>
BY LOCATION
<br>*Note: need IG location ID (see database of IDs in LA)
<br>
`loader.download_location(362629379, max_count=30, post_filter=None, fast_update=True)`

BY HASHTAG
<br>
`loader.download_hashtag('food', max_count=30), post_filter=None, fast_update=True)`
<br>
<br>
fast_update set to True so we don't donwload duplicates
<br>We can modify post_filter argument with lambda functions, so we can filter hashtags by location (and other filters when needed)

<br>
### LINKS
<br>
See here https://instaloader.github.io/as-module.html#posts
For info on all properties/methods of the Post object
