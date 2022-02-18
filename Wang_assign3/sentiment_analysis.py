'''
2021-11-06  15:02
written by @Wang Whisky
function:perform simple sentiment analysis on Twitter data and determine which timezone is the happiness
detail:(1) Analyze each tweet to determine a score(sum of sentiment values/number of keywords)
       (2) Analyze each tweet to determine which region
'''
import string
import json

'''
def keywords_score(txt):
    key_score ={}
    file_key = txt #keywords-1.txt
    try:
        with open(file_key,"r",encoding="utf-8") as fk:
            for line in fk:
                kv = line.strip().split(",")
                key_score[kv[0]] =kv[1] 
    except FileNotFoundError:
        print(f'Sorry,the file {file_key} does not exist!Please try again!')
        return []
    else:
        return key_score
'''
##############Determining timezones by the latitude and longitude of each tweets########################
def timezone(lat,long):
    if (24.660845 < lat < 49.189787):
        if (-125.242264 <= long < -115.236428):
            return "Pacific"
        elif(-115.236428 <= long < -101.998892):
            return "Mountain"
        elif(-101.998892 <= long < -87.518395):
            return "Central"
        elif(-87.518395 <= long <= -67.444574):
            return "Eastern"
        else:
            return "Skip"  #if outside the scale upper,SKIP!
    else:
        return "Skip"

##############Consider the conditions that the dividend can be zero######################################
def compute_average_zone_happiness_score(happiness_score_zone,keywordtweet_num):
    if(keywordtweet_num!=0):
        happiness_average_region = happiness_score_zone/keywordtweet_num
    else:
        happiness_average_region = "No results,because the number of keyward tweets in this region is none."
    return happiness_average_region


##############Compute the happiness score of each tweets and each region#################################
def compute_tweets(file_tweets,file_keywords):
    key_score ={}
    file_key = file_keywords #keywords-1.txt
    file_tweet=file_tweets #tweets-1.txt
    try:
        with open(file_key,"r",encoding="utf-8") as fk:
            for line in fk:
                kv = line.strip().split(",")
                key_score[kv[0]] =kv[1]  #store in the dict
    except FileNotFoundError:
        print(f'Sorry,the file {file_key} does not exist!Please try again!')
        return [] #return empty list
    punctuation = string.punctuation #all possible results of the punctuation
    #initial
    tweet_num_P = 0
    tweet_num_M = 0
    tweet_num_C = 0
    tweet_num_E = 0
    happiness_score_P = 0
    happiness_score_M = 0
    happiness_score_C = 0
    happiness_score_E = 0
    keywordtweet_num_P = 0
    keywordtweet_num_M = 0
    keywordtweet_num_C = 0
    keywordtweet_num_E = 0
    try:
        with open(file_tweet,"r",encoding="utf-8") as file_object:
            for line in file_object:
                flag = "FASLE" #initial 
                happiness_score_line_sum = 0
                key_num = 0
                happiness_score_line = 0
                # Pacific 、Mountain、Central 、Eastern
                line_s = line.split(" ",5)
                lat = float(line_s[0].strip("[],"))
                long = float(line_s[1].strip("[],"))
                tweet = line_s[5]
                words = tweet.strip("\n").split(" ")
                for word in words:
                    s = word.strip(punctuation) #strip
                    s = s.lower() #lower conversion
                    if s in key_score: #if match with the key in the dict
                        flag = "TRUE"
                        happiness_score_line_sum = happiness_score_line_sum + int(key_score.get(s))
                        key_num = key_num + 1
                if (key_num!=0):
                    happiness_score_line = happiness_score_line_sum/key_num
                else:
                    happiness_score_line = 0
                if (flag == "TRUE"):
                    keywordtweet_num =1
                else:
                    keywordtweet_num =0
                #print(happiness_score_line)
                if (timezone(lat,long)=="Pacific"): #Region determination
                    tweet_num_P = tweet_num_P +1
                    happiness_score_P  = happiness_score_P + happiness_score_line
                    keywordtweet_num_P = keywordtweet_num_P + keywordtweet_num
                elif(timezone(lat,long)=="Mountain"):
                    tweet_num_M = tweet_num_M +1
                    happiness_score_M  = happiness_score_M + happiness_score_line
                    keywordtweet_num_M = keywordtweet_num_M + keywordtweet_num
                elif(timezone(lat,long)=="Central"):
                    tweet_num_C = tweet_num_C +1
                    happiness_score_C  = happiness_score_C + happiness_score_line
                    keywordtweet_num_C = keywordtweet_num_C + keywordtweet_num
                elif(timezone(lat,long)=="Eastern"):
                    tweet_num_E = tweet_num_E +1
                    happiness_score_E  = happiness_score_E + happiness_score_line
                    keywordtweet_num_E = keywordtweet_num_E + keywordtweet_num

    except FileNotFoundError:
        print(f'Sorry,the file {file_tweet} does not exist!Please try again!')
        return []
    #Compute the average zone happiness score,pay attention to the zero 
    happiness_average_Pacific =compute_average_zone_happiness_score(happiness_score_P,keywordtweet_num_P)
    happiness_average_Mountain = compute_average_zone_happiness_score(happiness_score_M,keywordtweet_num_M)
    happiness_average_Central = compute_average_zone_happiness_score(happiness_score_C,keywordtweet_num_C)
    happiness_average_Eastern = compute_average_zone_happiness_score(happiness_score_E,keywordtweet_num_E)
    
    # tuple  
    Eastern = (happiness_average_Eastern,keywordtweet_num_E,tweet_num_E) #Eastern
    Central = (happiness_average_Central,keywordtweet_num_C,tweet_num_C) #Central
    Mountain = (happiness_average_Mountain,keywordtweet_num_M,tweet_num_M) #Mountain
    Pacific = (happiness_average_Pacific,keywordtweet_num_P,tweet_num_P) #Pacific
    # list output
    output = []
    output.append(Eastern)
    output.append(Central)
    output.append(Mountain)
    output.append(Pacific)
    return(output)


