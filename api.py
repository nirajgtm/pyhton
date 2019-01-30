import praw

print("Welcome To Reddit (read-only)")

reddit = praw.Reddit(client_id='hWZCBpTu00MaBg',
                     client_secret='Myzkhl_Kir7KoWU_1vIgq9rJUaQ',
                     user_agent='my user agent')
                     
print(reddit.read_only)
b=0
while b==0:
    a= input ("Which subreddit?")
    mysubreddit= reddit.subreddit(a)

    try:
       
        print(mysubreddit.title)
        print(mysubreddit.description)
        print("\n" * 5)
        print("--"*60)
        for submission in mysubreddit.hot(limit=10):
            print(submission.title)
            print("\n")
            print("--"*60)
            print("\n")

    except:
        print("Sorry the subreddit" + a + " does not exist")
    a= input("Do you want to continue? (y/n)")
    if a== "y":
        b=0
    else:
            b=1
print("\n" * 5)
print("--"*60)
print("Thankyou for using this simple app")