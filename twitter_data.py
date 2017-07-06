import pickle
from nltk.corpus import twitter_samples
import re
import random
from nltk import NaiveBayesClassifier
import nltk
from nltk.tokenize import word_tokenize

negative_tweets = twitter_samples.strings('negative_tweets.json')
positive_tweets = twitter_samples.strings('positive_tweets.json')

print len(negative_tweets)
print len(positive_tweets)

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

pos = []
neg = []

for tweet in positive_tweets:
    words = word_tokenize(processTweet(tweet))
    pos.append((create_word_features(words), "pos"))

for tweet in negative_tweets:
    words = word_tokenize(processTweet(tweet))
    neg.append((create_word_features(words), "neg"))

all_tweets = pos + neg

random.shuffle(all_tweets)

training_data_size = int(len(all_tweets) * 0.75)
print training_data_size

training_data = all_tweets[:training_data_size]
testing_data = all_tweets[training_data_size:]

classifier = NaiveBayesClassifier.train(training_data)
print ("Naive bayes algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_data)) * 100)
classifier.show_most_informative_features(20)

save_classifier = open("twitter_classifier.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()