import random
import spacy
import matplotlib.pyplot as plt


# Variable declerations
questionWeight = 0
questionDist = 0

wordWeightingDefault = [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
]

wordWeighting = [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
]

wordWeightingPos = [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
]

# Test words
questionWordsList = ["who", "when", "what", "where", "which", "why", "how",
                     "you", "me", "how-much", "what-do", "how many", "for-for", "will"]

# Testing sentences
sentenceList = ["you name",
                "deaf you",
                "student you",
                "your teacher name huh",
                "how you feel",
                "yesterday you shower",
                "hungry you",
                "learn sign language you",
                "you parents deaf",
                "please sign slow",
                "fingerspell again",
                "you read lips you",
                "understand",
                "good afternoon",
                "goodbye",
                "how you",
                "arrive how",
                "home me go",
                "hey name you",
                "you married",
                "he who",
                "I need brush teeth",
                "who hurt you feel",
                "sit where"
                ]

wordWeightingFull = [[] for i in range(len(sentenceList))]
wordWeightingPosFull = [[] for i in range(len(sentenceList))]

sentenceData = [
                "Question",
                "Question",
                "Question",
                "Question",
                "Question",
                "Question",
                "Question",
                "Question",
                "Question",
                "Statement",
                "Statement",
                "Question",
                "Question",
                "Statement",
                "Statement",
                "Question",
                "Question",
                "Statement",
                "Question",
                "Question",
                "Question",
                "Statement",
                "Question",
                "Question"
                ]

# Define a mapping of POS tags to numeric values
PosToNumber = {
    "X": 0, # This is for trhow away words
    "ADJ": 1,
    "ADP": 2,
    "ADV": 3,
    "AUX": 4,
    "CONJ": 5,
    "CCONJ": 6,
    "DET": 7,
    "INTJ": 8,
    "NOUN": 9,
    "NUM": 10,
    "PART": 11,
    "VERB": 12,
    "PROPN": 13,
    "PUNCT": 14,
    "SCONJ": 15,
    "SYM": 16,
    "PRON": 17
}

for x in range(len(sentenceList)):
    testInt = x
    # random.randint(0, len(sentenceList))
    sentence = sentenceList[testInt]

    print(f"-=[ {sentence} ]=-")

    wordsInputed = sentence.split()
    nlp = spacy.load("en_core_web_sm")

    def WordIs(word, location):
        doc = nlp(word)
        for token in doc:
            print()
            print(f"Word: {token.text}, Part of Speech: {token.pos_}, Loc: {location}")
            wordWeighting[PosToNumber[token.pos_]] = wordWeighting[PosToNumber[token.pos_]] + PosToNumber[token.pos_]
            wordWeightingPos[PosToNumber[token.pos_]] = (location + 1) + wordWeightingPos[PosToNumber[token.pos_]]


    for i in range(len(wordsInputed)):
        WordIs(wordsInputed[i], i)

    print(f"Word ratings:")
    #for i in range(len(wordWeighting)):
    #    print(i, "| ", wordWeighting[i])

    wordWeightingFull[x] = wordWeighting
    wordWeightingPosFull[x] = wordWeightingPos

    wordWeighting = wordWeightingDefault.copy()
    wordWeightingPos = wordWeightingDefault.copy()

    print(f"The sentence: '{sentence}', should be a [{sentenceData[testInt]}]")

for i in range(len(wordWeightingFull)):
    print(f"\n\t'{sentenceList[i]}' is a: [{sentenceData[i]}]")
    print(wordWeightingFull[i])
    
    # Create a scatterplot
    for y in range(17):
        if sentenceData[y] == "Statement":
            plt.scatter(wordWeightingFull[y][i], wordWeightingPosFull[y][i], color = 'green')
        else:
            plt.scatter(wordWeightingFull[y][i], wordWeightingPosFull[y][i], color = 'red')

    # Add labels and a title
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title(i)

    # Display the plot
    plt.show()
    print()