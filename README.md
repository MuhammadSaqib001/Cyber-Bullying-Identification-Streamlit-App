# Cyberbullying Tweet Recognition App

[Live Demo](https://cyberbullying-tweet-recognition-jayant-verma.streamlit.app/)

This project focuses on analyzing tweets to identify cyberbullying. Using natural language processing techniques, the app predicts whether a tweet is classified as cyberbullying and further categorizes it into one of six types:

- Age
- Ethnicity
- Gender
- Religion
- Other Cyberbullying

## Dataset
The dataset used for this project is the **Cyberbullying Classification** data from Kaggle. [Dataset Link](https://www.kaggle.com/datasets/d7pfHGT8)

## Approach

1. **Library Installation & Data Import**  
   - Installed required libraries and imported the dataset using `pandas`.

2. **Data Review**  
   - Conducted an initial review to check for missing values.

3. **Text Preprocessing**  
   Applied several preprocessing techniques to clean and prepare the text data:
   - Removed emojis
   - Converted text to lowercase and removed unwanted characters (e.g., `/r`, `/n`, URLs)
   - Eliminated non-UTF characters, numbers, punctuation, and stopwords
   - Handled contractions, hashtags, and special characters
   - Removed multi-space characters
   - Applied stemming and lemmatization

4. **Handling Duplicates**  
   - Identified and removed duplicate entries in the dataset.

5. **Exploratory Data Analysis**  
   - Performed data exploration to understand patterns and distributions.

6. **Train-Test Split**  
   - Split the data into training and testing sets.

7. **TF-IDF Vectorization**  
   - Applied TF-IDF vectorization to convert text data into numerical features.

8. **Model Selection**  
   - Tried different classification models:
     - Logistic Regression
     - Support Vector Classifier (SVC)
     - Naive Bayes Classifier
     - Decision Tree Classifier
     - Random Forest Classifier
     - AdaBoost Classifier

9. **Model Tuning**  
   - Fine-tuned the Support Vector Classifier for optimal performance.

10. **Model Evaluation**  
    - Evaluated model performance using standard metrics and saved the best-performing model.

11. **Web App Creation**  
    - Developed a user-friendly web application using Streamlit.

12. **Deployment**  
    - Deployed the web app on Streamlit.

## Libraries Used
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `re`, `nltk`, `emoji`, `wordcloud`, `streamlit`, `pickle`, `scikit-learn`

## Deployment Platform
- Streamlit

## Kaggle Link
The dataset can be accessed [here](https://www.kaggle.com/datasets/d7pfHGT8).
