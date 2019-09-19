#! python3
import praw
import json
import pandas as pd
import datetime as dt

class clsStartup:

    # setup reddit connection
    reddit = praw.Reddit(client_id='PBvTiroJrJyl9Q', \
                        client_secret='fFmU4S-W6PovNWqgMM6bbLfK2GE', \
                        user_agent='jessRedditProj', \
                        username='MindlessIce2', \
                        password='2p*mnc6FZ!yA')
    
    curation_dict = {}

    def GetCurationSettings(self):
        with open('curationSettings.json', 'r') as f:
            curation_dict = json.load(f)

        ##TEST##
        print(curation_dict)

    def __init__(self):
        self.GetCurationSettings()
        #fetch curation from settings file     --- eventually database
        #try
        #call scraper class instance for each curation in list
        #catch
        #log success/failure  setup logging lol

        # scaper class needs to work around rate limit, waits for a minute if rate limit succeeded, logs waiting etc


    


main = clsStartup()


    # subreddit = reddit.subreddit('AskComputerScience')

    # hot_subreddit = subreddit.hot(limit=25)

    # for submission in subreddit.hot(limit=5):
    #     print("Title: " + submission.title, 
    #     "Id: " + str(submission.id), 
    #     "Upvotes: " + str(submission.score), 
    #     "Text: " + submission.selftext, "\n\n\n\n",  sep="\n")