# imports.py

# ייבוא ספריות כלליות
import os
import re
import pandas as pd
import numpy as np

# ייבוא ספריות לעיבוד טקסט
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from textblob import TextBlob
import language_tool_python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import textstat

# ייבוא ספריות לניתוח סטטיסטי
from scipy.stats import pearsonr, spearmanr, f_oneway, kruskal, chi2_contingency

# ייבוא ספריות ויזואליזציה
import seaborn as sns
import matplotlib.pyplot as plt

# הגדרות או אתחול (אם יש צורך)
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool('en-US')

# ייבוא פונקציות עזר (אם יש לך פונקציות נוספות)
from utils import json_to_df, get_most_common_word_simple
