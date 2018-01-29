from PyQt5 import QtCore
import twitter

CONSUMER_KEY = 'FOCsEQzKgiGsmcKjGfIxCMvzG'
CONSUMER_SECRET = '1b7vcnfWi0XB2ToWg6DyExUPJyJChQNlI80hk9cRFBgeGDP5hP'
ACCESS_TOKEN_KEY = '2389226360-hx1JtwawH75LNKmgi0x5Ec5qHw15yLRn6hqpQQP'
ACCESS_TOKEN_SECRET = 'pq26olnBNatEEORQM4fVDbDsBmvCpfnxTvYB9Rw9AKNpu'

MAX_QUERY = 5

api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)

def getTweets(url, count):
    tweets = []
    if count > 100:
        iterationCount = count / 100
        url = "q=" + url + "&lang=en&tweet_mode=extended&count=100"
        results = api.GetSearch(raw_query=url)
        for result in results:
            tweets.append(result.full_text)
        while len(tweets) < count and iterationCount > 0:
            ids = [result.id for result in results]
            minId = min(ids)-1
            results = api.GetSearch(raw_query=url + "&max_id=" + str(minId))
            for result in results:
                tweets.append(result.full_text)
            iterationCount -= 1
    else:
        url = "q=" + url + "&tweet_mode=extended&count=" + str(count)
        results = api.GetSearch(raw_query=url)
        for result in results:
            tweets.append(result.full_text)
    return tweets