import numpy as np
import pandas as pd
import json
import tweepy

#access tokens and consumer keys and secrets
consumer_key="4FwqkxfsxWtAW8438GOwdA53o"
consumer_secret="Z5hqRV1FvoVUie2rrQbKZRpsQbLn0FLtxnGPvSHY6ar0n7pZ6R"
access_token_key="722383236718964736-6lEkXp5fG6M2Y9VfanJmsX4lPLCLIjw"
access_token_secret="tJO4PrBw5jMSF7NVTHaqvSzMSUGgZTjT4UKDTfICfbZF6"

path = r"memCongwithNaN.csv"

#extract the info
df = pd.read_csv(path)

#dataframes from the columns
df_lastName = df["last_name"]
df_poliParty = df["party"]
df_twitter = df["twitter"]

#turn this into arrays
lastName = df_lastName.values
poliParty = df_poliParty.values
twitter_handle = df_twitter

#turn this into a dictionary to be able to store the information

#get all politicians
def populateDictionary(party_list, twitter_list, lastNames):

    politicians = {}
    for x in range(len(party_list)):
        valuesForDict = []
        valuesForDict.append([party_list[x], str(twitter_list[x])])

        politicians[lastNames[x]] = valuesForDict

    return politicians

#get republicans
def extractRepublicans(party_list, twitter_list, lastNames):
    republicans={}
    for x in range(len(party_list)):
        valuesForDict = []
        valuesForDict.append([party_list[x], str(twitter_list[x])])
        if valuesForDict[0][0] == 'Republican':
            republicans[lastNames[x]] = valuesForDict
        else:
            continue
    return republicans

#get democrats
def extractDemocrats(party_list, twitter_list, lastNames):
    democrats={}
    for x in range(len(party_list)):
        valuesForDict = []
        valuesForDict.append([party_list[x], str(twitter_list[x])])
        if valuesForDict[0][0] == 'Democrat':
            democrats[lastNames[x]] = valuesForDict
        else:
            continue
    return democrats

#get all the others
def extractOther(party_list, twitter_list, lastNames):
    other={}
    for x in range(len(party_list)):
        valuesForDict = []
        valuesForDict.append([party_list[x], str(twitter_list[x])])

        if (valuesForDict[0][0] != 'Democrat' and valuesForDict[0][0] != 'Republican'):
            other[lastNames[x]] = valuesForDict
        else:
            continue
    return other

#extract the handles for dems and rep
def extract_handles(party_list, twitter_list, partyName):
    t_handles = []
    for x in range(len(party_list)):
        if(party_list[x] == partyName):
            t_handles.append(twitter_list[x])
        else:
            continue
    return t_handles

#extract the handles for independents
def extract_Oth_handles(party_list, twitter_list):
    t_handles = []
    for x in range(len(party_list)):
        if(party_list[x] == 'Independent'):
            t_handles.append(twitter_list[x])
        else:
            continue
    return t_handles

#function to get all of the tweets
def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    # calling the api
    api = tweepy.API(auth)

    # extracting last 200 tweets
    tweets = api.user_timeline(screen_name=username)

    # create empty array to store tweets
    tmp = []
    tweets_dict = {}

    # create the csv file to hold all the tweets
    tweets_for_csv = [tweets.text for tweets in tweets]
    for j in tweets_for_csv:
        tmp.append(j)

    print("Gathered tweets for " + str(username))
    return tmp

#all_members = populateDictionary(poliParty, twitter_handle, lastName)
#republicans = extractRepublicans(poliParty, twitter_handle, lastName)
#democrats = extractDemocrats(poliParty, twitter_handle, lastName)


#writing to json file

def writeToJSON(fileName, data):
    filePathNameWExt = fileName + '.json'
    with open(filePathNameWExt, 'w') as f:
        json.dump(data, f, indent=1)

def toTextFile(desired_file_name, handles):
    file = open(desired_file_name,"w", encoding='utf-8')
    for handle in handles:
        tweets = get_tweets(handle)
        print("Writing tweets for " + str(handle))
        for tweet in tweets:
            file.write(str(tweet) + "\n")

        print("Finish writing tweets for " + str(handle))
        print(" ")



#writeToJSON('example',all_members)

#make the sure we are getting the name of the politicians
dem_handles = extract_handles(poliParty,twitter_handle, "Democrat")
#rep_handles = extract_handles(poliParty, twitter_handle, "Republican")
#oth_handles = extract_Oth_handles(poliParty,twitter_handle)

toTextFile("dem4_tweets.txt", dem_handles)
#toTextFile("rep_tweets.txt", rep_handles)
#toTextFile("oth4_tweets.txt", oth_handles)

#tweets = get_tweets("ikechukwu_anude")
#toTextFile("example.txt", tweets)