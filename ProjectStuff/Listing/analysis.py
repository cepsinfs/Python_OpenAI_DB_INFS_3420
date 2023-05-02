from textblob import TextBlob

def textPol(text):
    pol = TextBlob(text).sentiment.polarity
    return pol
  
def textAnalysis(polScore):
    if(polScore > 0):
        return "Positive"
    elif(polScore == 0):
        return "Neutral"
    elif(polScore < 0):
        return "Negative"
     