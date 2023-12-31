from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
import spacy

# Basically a spacy import type
nlp = spacy.load("en_core_web_sm")

# Variables
sentenceList = []
sentenceData = []
aSLSentences = []
englishSentences = []
questionMark = ""
inputText = "you name you" # This is the import from James King

# Creates list of data to be used from the text files
with open('Source\\NLP_Data\\NLP_Question_Data.txt', 'r') as file:
    for line in file:
        sentenceList.append(line.strip())

with open('Source\\NLP_Data\\NLP_Sentence_Data.txt', 'r') as file:
    for line in file:
        sentenceData.append(line.strip())

with open('Source\\NLP_Data\\NLP_Sentence_ASL.txt', 'r') as file:
    for line in file:
        aSLSentences.append(line.strip())

with open('Source\\NLP_Data\\NLP_Sentence_English.txt', 'r') as file:
    for line in file:
        englishSentences.append(line.strip())

# For later use with question and statement assignment
class Category:
    Question = "Question"
    Statement = "Statement"

def get_word_category(word, word_categories):
    for category, words in word_categories.items():
        if word in words:
            return category
    return None  # Return None if the word is not found in any category

word_categories = {
    'pronouns': {
        'i': 'prn',
        'you' : 'prn' 
        },
    'nouns': {
        'student' : 'noun',
        'teacher' : 'noun',
        'book' : 'noun',
        'people' : 'noun',
        'person' : 'noun',
        'icecream' : 'noun',
        'spaghetti' : 'noun'
        },
    'verbs': {
        'read' : 'verb',
        'borrow' : 'verb',
        'see' : 'verb',
        'help' : 'verb',
        'run' : 'verb',
        'jump' : 'verb',
        'eat' : 'verb'
        },
    'time': {
        'yesterday',
        'tomorrow',
        'last week',
        'next week',
        'last year',
        'next year'
        }
}

brokenUpInputText = inputText.split()
changedText = []

for i in range(len(brokenUpInputText)):
    category = get_word_category(brokenUpInputText[i], word_categories)
    if category:
        changedText.append(category)
    else:
        changedText.append(brokenUpInputText[i])

print(f"Test changes: {changedText}")

sentenceData = [Category.Question if line.startswith("Q") else Category.Statement for line in sentenceData]

# Basic information to check if everything was imported correctly
print(f"Imported [{len(sentenceData)}] question/statement data sentences")
print(f"Imported [{len(englishSentences)}] ASL → English data sentences")

# Vectorizes the dataset's sentences for questions/statements
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(sentenceList)
clf_svm = svm.SVC(kernel = 'linear')
clf_svm.fit(vectors, sentenceData)
text_x = vectorizer.transform([inputText]) # This is the imput text
test = clf_svm.predict(text_x)

# miscellaneous components
print(f"\t→ '{inputText}' is likely a {test[0]}")
questionMark = "?" if test[0] == "Question" else ""
encoded_labels = englishSentences

# Vectorizes the dataset's sentences (ASL → English)
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(aSLSentences)
clf_svm = svm.SVC(kernel = 'linear')
clf_svm.fit(vectors, encoded_labels)
label_encoder = LabelEncoder()
label_encoder.fit(encoded_labels)

# Final output prediction & output
input_x = vectorizer.transform([inputText])
predicted_class_encoded = clf_svm.predict(input_x)
print(f"Input: ['{inputText}'] → Output: ['{predicted_class_encoded[0].capitalize()}{questionMark}']")

# Send onto Sean's code
sendToSean = f'{predicted_class_encoded[0].capitalize()}{questionMark}'
print("Send to Sean: ", sendToSean)