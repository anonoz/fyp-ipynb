from bs4 import BeautifulSoup
import re

def tokenize(text):
  return normalise_text(text).split()

def normalise_text(text):
  #1 Remove HTML (inspired by Kaggle)
  text = BeautifulSoup(text, "html.parser").getText()

  #2 Tokenize (stolen from Yoon Kim's CNN)
  text = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", text)     
  text = re.sub(r"\'s", " \'s", text) 
  text = re.sub(r"\'ve", " \'ve", text) 
  text = re.sub(r"n\'t", " n\'t", text) 
  text = re.sub(r"\'re", " \'re", text) 
  text = re.sub(r"\'d", " \'d", text) 
  text = re.sub(r"\'ll", " \'ll", text) 
  text = re.sub(r",", " , ", text) 
  text = re.sub(r"!", " ! ", text) 
  text = re.sub(r"\(", " \( ", text) 
  text = re.sub(r"\)", " \) ", text) 
  text = re.sub(r"\?", " \? ", text) 
  text = re.sub(r"\s{2,}", " ", text)
  
  # Step 3: 
  return text.lower()
