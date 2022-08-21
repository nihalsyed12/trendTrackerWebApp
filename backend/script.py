
import tweepy
import cohere
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from functions import clean_tweet, get_tweets, get_examples, get_labels, classify_text
from cohere.classify import Example 

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAG6%2FgAEAAAAAy7iHcVgxnZcGExwRjzHXqT%2FhPtE%3DGQEPcxnLQIL2do5DwvCHw8dFNuBlEVf9vtthVZ4fEDsr1zRVGx'
COHERE_KEY = 'DaOdiziacxhtYOe2pYWM1HDdK1PHh4EC2P5TFojG'

KEY = "andrewtate" # key entered by user

def main(key):
    print("gh")
    tweets = get_tweets(key, BEARER_TOKEN)

    clean_tweets = []

    i = 0
    for tweet in tweets:
        if i > 30:
            break
        print(tweet.text)
        t = clean_tweet(tweet.text)
        clean_tweets.append(t)
        i += 1

    examples = get_examples()

    co = cohere.Client(COHERE_KEY)

    classifications = classify_text(clean_tweets, examples, co)
    

    labels = get_labels(classifications)
    return labels

# if __name__ == "__main__":
#     main(KEY)


