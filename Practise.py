import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

hi=pd.read_csv('FIFA.csv')
# h['Tweet'].to_pickle('Tweets.pickle')
# hi=pd.read_pickle('Tweets.pickle')
neut=0
pos=0
neg=0
n=int(input("Enter the number of tweets you want to analyse out of 5.3 lac tweets:"))

for i in hi['Tweet'][:n]:
    blob=TextBlob(str(i))
    # print(blob.sentiment)
    if blob.polarity<0:
        neg+=1
    elif blob.polarity>0:
        pos+=1
    else:
        neut+=1
print("Number of negative tweets: ",neg)
print("Number of positive tweets: ",pos)
print("Number of neutral tweets: ",neut)
negp=(neg/n)*100
neutp=(neut/n)*100
posp=(pos/n)*100
print("Percentage of negative tweets: ",negp)
print("Percentage of positive tweets: ",posp)
print("Percentage of neutral tweets: ",neutp)

labels = 'Positive',"Negative","Neutral"
sizes = [posp,negp,neutp]
m=max(posp,negp,neutp)
if m==posp:
    explode=(0.1,0,0)
elif m==negp:
    explode = (0, 0.1, 0)
else:
    explode = (0, 0, 0.1)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()