import tweepy
import cohere 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from cohere.classify import Example 

def get_tweets(key, token):

    # connects to twitter api and pulls tweets
    


    client = tweepy.Client(bearer_token= token)

    query = f'#{key} -is:retweet lang:en'

    #tweets = client.search_recent_tweets(query=query)
    tweets = tweepy.Paginator(client.search_recent_tweets, query=query,
                max_results=50).flatten(limit=1000)

    return tweets

def clean_tweet(tweet):

    # Cleans tweets to remove @mentions, links, stop words, & punctuation
    # @param tweet: a string representing a tweet
    # @return: cleaned tweet as string

    tweet = tweet.lower() # lowercase

    tweet = re.sub(r'(@[A-Za-z0-9_]+)', '', tweet) # remove @mentions

    tweet = re.sub('http://\S+|https://\S+', '', tweet) # remove links

    tweet = re.sub(r'[^\w\s]', '', tweet) #remove punctuation

    tokens = tweet.split(' ') #split words based on space 
    tweet = [t for t in tokens if not t in stopwords.words()] # remove stopwords

    tweet = ' '.join(tweet)

    return tweet

def get_examples():

    examples = [Example("I'm so proud of you", "positive"), 
            Example("What a great time to be alive", "positive"), 
            Example("That's awesome work", "positive"), 
            Example("The service was amazing", "positive"), 
            Example("I love my family", "positive"), 
            Example("They don't care about me", "negative"), 
            Example("I hate this place", "negative"), 
            Example("The most ridiculous thing I've ever heard", "negative"), 
            Example("I am really frustrated", "negative"), 
            Example("This is so unfair", "negative"),
            Example("This made me think", "neutral"), 
            Example("The good old days", "neutral"), 
            Example("What's the difference", "neutral"), 
            Example("You can't ignore this", "neutral"), 
            Example("That's how I see it", "neutral"), 
            Example("I love this brand", "positive"), 
            Example("It is too expensive", "negative"),
            Example("the wait time is very long", "negative"),
            Example("wow that's so cute", "positive"),
            Example("It fits so well", "positive"),
            Example("this is mediocre", "neutral"),
            Example("The employee was rude", "negative"),
            Example("fast shipping times", "positive"),
            Example("wonderful customer service", "negative"),         
            ]

    return examples

def classify_text(inputs,examples, co):
    # classifies tweets
    response = co.classify(
    model='large',
    inputs=inputs[:30],
    examples=examples)
  
    return response.classifications

def get_labels(classify_text):
    # gets label (positive, neutrel or negative) and tweet
    labels = []
    text = []
    for t in classify_text:
        labels.append(t.prediction)
        
    return labels


    

