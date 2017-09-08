import json

from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener


consumer_key = '9sLvkQd4oIveb58vmXEaairNo'
consumer_secret = 'eIQ1aRoCY5dpgGvvq5EbHqiWAbcRek0k0ZooBJQv5ezwMfDQTM'
access_token = '887566994559479809-ti7KFWpBCLfMd4FU92pI4Cijy2P9Oqf'
access_token_secret = 'ZFTFlnVe6qaUB0N6qM7FCGspmgai6QrJAsRiRlSoXwXH6'

auth = OAuthHandler(consumer_key,
                    consumer_secret)

auth.set_access_token(access_token, access_token_secret)


class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text.encode('utf8'),)
            print(status.author.screen_name.encode('utf8'),
                  status.created_at,
                  status.source,
                  '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True # keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True # keep stream alive


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)


def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


if __name__ == '__main__':
    # print_to_terminal()
    pull_down_tweets(auth.username)
