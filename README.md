# Web Scraping from IG (using Instaloader Scraper Tool)

### Create an Instaloader() object
`loader = Instaloader()`

Functions we can use to scrape:
<br><br>
BY LOCATION
<br>*Note: need IG location ID
<br>
[see database of IDs in LA](https://uploads-ssl.webflow.com/5bf6aaab4fac80dbdf6a9b13/5d309a17b0d13061efe289d5_A%20Complete%20List%20of%20Instagram%20Location%20IDs%20in%20Los%20Angeles%2C%20California%2C%20USA.pdf)
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
