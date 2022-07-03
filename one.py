import pdfplumber
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

skills = "Django Python Pandas Flask CSS HTML ML Hadoop Data Analysis Visualization"

with pdfplumber.open(r'Raj Chhabria Resume.pdf') as pdf:
    first_page = pdf.pages[0]
    resume_text = first_page.extract_text()

stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(resume_text)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
  

def listToString(s):
   
    
    s1 = " "
   
     
    return (s1.join(s))
       
         
resume_text_wo_stopwords = listToString(filtered_sentence)

print(resume_text_wo_stopwords)

wnl = WordNetLemmatizer()

lemmatized_resume_text = wnl.lemmatize(resume_text_wo_stopwords)

tfidf = TfidfVectorizer()

corpus = [skills, lemmatized_resume_text]

tfidf_matrix = tfidf.fit_transform(corpus)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("Match % = ",cosine_sim[0][1]*100)