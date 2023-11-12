from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from gramformer import Gramformer
import torch

gf = Gramformer(models = 1, use_gpu = True)

sentenceList = []
sentenceData = []

inputText = "what dog do"

print(gf.correct(inputText))

# Creates list of data to be used
with open('Source\\Data\\NLP_Question_Data.txt', 'r') as file:
    for line in file:
        sentenceList.append(line.strip())

with open('Source\\Data\\NLP_Sentence_Data.txt', 'r') as file:
    for line in file:
        sentenceData.append(line.strip())

class Category:
    Question = "Question"
    Statement = "Statement"

sentenceData = [Category.Question if line.startswith("Q") else Category.Statement for line in sentenceData]

print(f"Imported [{len(sentenceData)}] data sentences")

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(sentenceList)
clf_svm = svm.SVC(kernel = 'linear')
clf_svm.fit(vectors, sentenceData)
text_x = vectorizer.transform([inputText]) # This is the imput text
test = clf_svm.predict(text_x)

print(f"'{inputText}' is likely a {test[0]}")

print(f'{gf.correct(inputText)} {"?" if test[0] == "Question" else ""}')