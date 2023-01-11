tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

#creamos lista de palabras tristes y felices
happy_words=['great','excited','happy','nice','wonderful','amazing','good','best']
sad_words=['sad','bad','tragic','unhappy','worts']

sample_tweet= tweets[0]
print(sample_tweet)

"""para cade palabra de la lista de palabras felices comprobamos si es parte del
twit seleccionado si la palabra se incluye como parte del twet establecmos la variable 
is tweet happy =True"""
is_tweet_happy=False
for word in happy_words:
    if word in sample_tweet:
        is_tweet_happy=True
        print(is_tweet_happy)
print("numero de tweets felices")
number_of_happy_tweets=0

for i in happy_words:
    for j in tweets:
        if i in j:
            number_of_happy_tweets=number_of_happy_tweets+1
        
print("Number of happy tweets :",number_of_happy_tweets)

happy_fraction=number_of_happy_tweets/10

print("the fraction of happy tweets",happy_fraction)

number_of_sad_tweets=0

for i in sad_words:
    for j in tweets:
        if i in j :
            number_of_sad_tweets=number_of_sad_tweets+1
            
print("Number of sad tweet ", number_of_sad_tweets)
sad_fraction=number_of_sad_tweets/10
print("the fraction  of sad tweets is ", sad_fraction)



