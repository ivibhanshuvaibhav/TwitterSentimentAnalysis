import pickle
import re
from nltk import word_tokenize

save_classifier = open("twitter_classifier.pickle", "rb")
classifier = pickle.load(save_classifier)
save_classifier.close()

def processTweet(tweet):
    # remove links
    tweet = re.sub('((www.[^\s]+)|(https:[^\s]+)|(http:[^\s]+))', '', tweet)
    # remove :) and :( emoticons
    tweet = tweet.replace(":", "")
    tweet = tweet.replace(")", "")
    tweet = tweet.replace("(", "")
    # remove RT
    tweet = tweet.replace('RT', '')
    # lower text
    tweet = tweet.lower()
    # remove twitter handle
    tweet = re.sub('@[^\s]+', '', tweet)
    # remove ampersand
    tweet = re.sub('&[^\s]+', '', tweet)
    # remove hashtag
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # return processed tweet
    return tweet

def create_word_features(words):
    my_dict = dict([(word, True) for word in words])
    return my_dict

def analysis(text):
    words = word_tokenize(processTweet(text))
    print classifier.classify(create_word_features(words))
