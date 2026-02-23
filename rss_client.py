import feedparser
class RSSClient:
    #this class is responsible for fetching and parsing RSS feed
    def __init__(self, rss_url):
        #store RSS feed URL
        self.rss_url = rss_url

    def fetch_feed(self):
        #fetch and return parsed RSS feed
        return feedparser.parse(self.rss_url)

    def get_latest_entry(self):
        #get latest entry from RSS feed
        feed = self.fetch_feed()
        if feed.entries:
            return feed.entries[0]
        return None