#mvp of the entire project
'''
1. collect news and areas of interest
2. process - filter
3. Build email content
4. Send the email
all wrapped under 1 container
get it to run and work
'''
import feedparser

def collect_news():
    #general news - political, local, economy, public safety, environment, social issues, and major interational events. Using RSS
    RSS_LINKS = {
        'BBC News' : 'http://feeds.bbci.co.uk/news/rss.xml',
        'NY Times' : 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
        'Washington Post' : 'http://feeds.washingtonpost.com/rss/world',
        'CNN' : 'http://rss.cnn.com/rss/cnn_topstories.rss',
        'NPR': 'https://feeds.npr.org/1001/rss.xml',
        'The Guardian' : 'https://www.theguardian.com/us-news/us-politics/rss'
    }

    #parse the news feeds
    #for the articles - filter out to get information that falls under 'general' news categories
    for source,link in RSS_LINKS.items():
        newsfeed = feedparser.parse(link)
        
    

def process_news(news):
    pass

def compose_email(processed):
    pass

def send_email(email):
    pass

if __name__ == "__main__":
    news = collect_news()
    # processed = process_news(news)
    # email = compose_email(processed)
    # send_email(email)