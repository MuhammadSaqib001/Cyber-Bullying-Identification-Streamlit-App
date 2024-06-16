import pandas as pd
import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from Prediction import *

# Check if the necessary NLTK resources are downloaded, download them if not
nltk_resources = ['stopwords', 'wordnet', 'punkt', 'omw-1.4']
for resource in nltk_resources:
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(resource)

st.write('''
# Cyberbullying Tweet Recognition App

This app predicts the nature of the tweet into 6 Categories.
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

***
''')

image = Image.open('statics/twitter.png')
st.image(image, use_column_width= True)

# Text Box
st.header('Enter Tweet ')
tweet_input = st.text_area("Tweet Input", height= 150)
print(tweet_input)
st.write('''
***
''')

# print input on webpage
if tweet_input:
    st.header('''
    ***Predicting......
    ''')
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')
st.write('''
***
''')

# Output on the page
st.header("Prediction")
if tweet_input:
    prediction = prediction(tweet_input)
    if prediction == "age":
        st.image("statics/Age.png",use_column_width= True)
    elif prediction == "ethnicity":
        st.image("statics/Ethnicity.png",use_column_width= True)
    elif prediction == "gender":
        st.image("statics/Gender.png",use_column_width= True)
    elif prediction == "other_cyberbullying":
        st.image("statics/Other.png",use_column_width= True)
    elif prediction == "religion":
        st.image("statics/Religion.png",use_column_width= True)
    elif prediction == "not_cyberbullying":
        st.image("statics/not_cyber.png",use_column_width= True)
else:
    st.write('''
    ***No Text Entered!***
    ''')

st.write('''***''')
