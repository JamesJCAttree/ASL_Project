import spacy

# Variable declerations
words = [("my", "determiner"), ("name", "noun"), ("is", "determiner")]
isQuestion = ""
input = input("ASL Sentence: ")
wordsInputed = input.split()
nlp = spacy.load("en_core_web_sm")
questionWordsList = ["who", "when", "what", "where", "which", "why", "how",
                     "you", "me", "how-much", "what-do", "how many", "for-for", "will"]
finalSentence = [[], [], []]

# Checks what the word is in the English language
def WordIs(word):
    doc = nlp(word)
    for token in doc:
        print(f"Word: {token.text}, Part of Speech: {token.pos_}")
        if token.pos_ == "PRON":
            finalSentence[0].append(token.text)
        if token.pos_ == "VERB":
            finalSentence[1].append(token.text)
        if token.pos_ == "NOUN":
            finalSentence[2].append(token.text)

# Tests to see if the sentence is likely a question
def TestQuestionWordInList(questionWord):
    if questionWord in questionWordsList:
        return True
    return False

# This tests to see if the sentence is likely a question
def TestIfQuestion():
    for i in range(len(wordsInputed)):
        if i == len(wordsInputed) - 1 and TestQuestionWordInList(wordsInputed[len(wordsInputed) - 1]):
            isQuestion = "?"
        else:
            WordIs(wordsInputed[i])

# Prints the sentence section by section
def PrintSentence():
    for i in range(3):
        for x in range(len(finalSentence[i])):
            print(finalSentence[i][x], end = " ")
    print(isQuestion)

# Runs the code
TestIfQuestion()
PrintSentence()