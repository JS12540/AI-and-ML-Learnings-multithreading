from scipy.special import softmax
from model import Model
import numpy as np

class Classifier:
  def __init__(self):
    self.model = Model.load_model()
    self.tokenizer = Model.load_tokenizer()

  def get_sentiment_label_and_score(self, text: str):
    result = {}
    labels = ['holdings','capital_gains','scheme_wise_returns','investment_account_wise_returns','portfolio_update','Current Year','Previous Year','Daily',
              'Monthly','Weekly','Yearly','None_date','None_module']
    encoded_input = self.tokenizer(text, return_tensors='pt')
    output = self.model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    result["label"] = str(labels[ranking[0]])
    result["score"] = np.round(float(scores[ranking[0]]), 4)
    return result