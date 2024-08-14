# nlp.py
from classifier import Classifier

classifier = Classifier()

def sentiment_analysis(query:str, classifier): 
  sentiment = classifier.get_sentiment_label_and_score(query)
  return sentiment 
     