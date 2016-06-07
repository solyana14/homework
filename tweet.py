''' printing a list of abbreviation from a tweet along with its decoded meaning'''

def Tweet(tweet):
    if 'LOL' in tweet:
        print('LOL = laughing out loud')
    if 'BFN' in tweet:
        print('BFN = bye for now')
    if 'FTW' in tweet:
        print('FTW = for the win')
    if 'IRL' in tweet:
        print('IRL = in real life')
    if 'TTYL' in tweet:
        print('TTYL = talk to you later')
    if 'PROLLY' in tweet:
        print('PROLLY = probably')
    if 'PPL' in tweet:
        print('PPL = people')
    if 'POV' in tweet:
        print('POV = point of view')
    else:
        print('Sorry no abbrevations found!')
# prompt the user to enter a tweet
def main():
    tweet = input("Enter a tweet that has less than 160 characters: ")
    while len(tweet) > 160:
        tweet = input("Enter another tweet that has LESS THAN 160 characters: ")
    Tweet(tweet)

main()
    
