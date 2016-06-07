''' Convert the user’s tweet to a decoded tweet, replacing the abbreviations directly within the tweet'''

def Tweet(tweet):
    new_tweet = tweet[:]
    new_tweet = new_tweet.replace("LOL", "Laughig out loud")
    new_tweet = new_tweet.replace("BFN", "bye for now")
    new_tweet = new_tweet.replace("FTW", "for the win")
    new_tweet = new_tweet.replace("IRL", "in real life")
    new_tweet = new_tweet.replace("TTYL", "talk to you later")
    new_tweet = new_tweet.replace("PROLLY", "probably")
    new_tweet = new_tweet.replace("PPL", "people")
    new_tweet = new_tweet.replace("POV", "point of view")
    print(new_tweet)
# prompt the user to enter a tweet
      
def main():
    tweet = input("Enter a tweet that has less than 160 characters: ")
    while len(tweet) > 160:
        tweet = input("Enter another tweet that has LESS THAN 160 characters: ")
    Tweet(tweet)

main()
