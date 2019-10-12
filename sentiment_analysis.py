# -*- coding: utf-8 -*-
"""sentiment_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LKUAR06f9Bgg5LF3Ce-3rP-MYAGl1f8V
"""

from google.colab import drive
drive.mount('/content/gdrive')

!unzip "/content/gdrive/My Drive/sentiment140.zip"

!ls "/content/gdrive/My Drive"

# Commented out IPython magic to ensure Python compatibility.
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np
import re
# %matplotlib inline

tweets = pd.read_csv('/content/sentiment140.csv',encoding='latin-1')

tweets.columns = ['label','userid','time','no','username','message']

tweets = tweets.sample(frac=1)

tweets = tweets.head(75000)

tweets = tweets.drop(columns=['time','no','userid'])

tweets = tweets.reset_index()

tweets = tweets.drop(columns = ['index'])

tweets

Y = tweets.label

X = tweets.drop(columns = ['label'])

from sklearn.model_selection import train_test_split
X_train, X_test ,Y_train, Y_test = train_test_split(X, Y,test_size=0.15)

print(X_train.size)
print(X_test.size)
print(Y_test.size)
print(Y_train.size)


