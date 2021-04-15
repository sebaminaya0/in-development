#Import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re, string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from textblob import TextBlob
nltk.download('punkt')
nltk.download('wordnet')

#Get the data into a DataFrame
df = pd.read_csv("YOUR CSV FILE")

df.head()

sw = stopwords.words('english')

#Data Manipulation, you can add any other word to be changed here :)
df.astype('str')

df['Comentarios']=df['Comentarios'].str.replace(',','')

df['Comentarios']=df['Comentarios'].str.replace('.','')

df['Comentarios']=df['Comentarios'].str.replace('I','')

df['Comentarios']=df['Comentarios'].str.replace('!','')

#The function
def clean_text(text):
    #Tokenize the data
    text = nltk.word_tokenize(text)
    #Remove stopwords
    text = [w for w in text if w not in sw]
    return text

df['Comentarios'] = df['Comentarios'].apply(lambda x: clean_text(x))

#Lemmatizer
lemmatizer = WordNetLemmatizer()
def lem(text):
    text = [lemmatizer.lemmatize(t) for t in text]
    text = [lemmatizer.lemmatize(t, 'v') for t in text]
    return text

df['Comentarios'] = df['Comentarios'].apply(lambda x: lem(x))

#Remove all empty comments
empty_comment = df['Comentarios'][223]
for i in range(len(df)):
    if df['Comentarios'][i]==empty_comment:
        df=df.drop(i)
df=df.reset_index(drop=True)

#From lists of comments to a single list containing all words      
all_words=[]        
for i in range(len(df)):
    all_words = all_words + df['Comentarios'][i]

#Get word frequency        
nlp_words = nltk.FreqDist(all_words)
plot1 = nlp_words.plot(40, color='salmon', title='Word Frequency')

#Bigrams
bigrm = list(nltk.bigrams(all_words))
words_2 = nltk.FreqDist(bigrm)
words_2.plot(40, color='salmon', title='Bigram Frequency')

#Trigrams
trigrm = list(nltk.everygrams(all_words,3,3))
words_2 = nltk.FreqDist(trigrm)
words_2.plot(40, color='salmon', title='Trigram Frequency')

#Sentiment Analysis
bloblist_desc = list()

df_descr_str=df['Comentarios'].astype(str)
for row in df_descr_str:
    blob = TextBlob(row)
    bloblist_desc.append((row,blob.sentiment.polarity, blob.sentiment.subjectivity))
    df_polarity_desc = pd.DataFrame(bloblist_desc, columns = ['sentence','sentiment','polarity'])
 
def f(df_polarity_desc):
    if df_polarity_desc['sentiment'] > 0:
        val = "Positive"
    elif df_polarity_desc['sentiment'] == 0:
        val = "Neutral"
    else:
        val = "Negative"
    return val

df_polarity_desc['Sentiment_Type'] = df_polarity_desc.apply(f, axis=1)

plt.figure(figsize=(10,10))
sns.set_style("whitegrid")
ax = sns.countplot(x="Sentiment_Type", data=df_polarity_desc)
