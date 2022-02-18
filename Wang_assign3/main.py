'''
2021-11-14  20:02
written by @Wang Whisky
function:interact with the user and use the module of sentiment_analysis.py
'''
import sentiment_analysis as sa

#receive the input files names from the user
input_tweets = "Please input the file name of the tweets information file(store in this dir):"
tweets =input(input_tweets)
input_keyfile ="Please input the file name of the keywords file(store in this dir):"
keyfile =input(input_keyfile)

output = sa.compute_tweets(tweets,keyfile)
print(output)
if (len(output)!=0):
    print("\n\n\n")
    print("**********Output Summary**********")
    #print("*****Eastern*****")
    print(f'Eastern Region:average happiness score:{output[0][0]},{output[0][1]} keyword tweets,{output[0][2]} tweets in total for the region.')
    print("\n")
    #print("*****Central*****")
    print(f'Central Region:average happiness score:{output[1][0]},{output[1][1]} keyword tweets,{output[1][2]} tweets in total for the region.')
    print("\n")
    #print("*****Mountain*****")
    print(f'Mountain Region:average happiness score:{output[2][0]},{output[2][1]} keyword tweets,{output[2][2]} tweets in total for the region.')
    print("\n")
    #print("*****Pacific*****")
    print(f'Pacific Region:average happiness score:{output[3][0]},{output[3][1]} keyword tweets,{output[3][2]} tweets in total for the region.')
    print("\n")
else:
    print("\n\n\n")
    print("**********Output Summary**********")
    print("the input files does not exist or empty or does not satisfy the format of this program! ")