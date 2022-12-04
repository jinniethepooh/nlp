import spacy

nlp = spacy.load("en_core_web_sm")

# tokenization
sentence = nlp.tokenizer("we live in paris.")

# length of sentence
print("the number of tokens: ", len(sentence))

# print individual words
print(sentence)

import pandas as pd
import os

cwd = os.getcwd()

# import jeopardy questions
data = pd.read_csv(cwd + '/data/jeopardy_questions/jeopardy_questions.csv')
data = pd.DataFrame(data=data)

# lowercase, strip whitespace, and view columns name
data.columns = map(lambda x: x.lower().strip(), data.columns)

# reduce size of data
data = data[0:1000]

# tokenize jeopardy questions
data["question_tokens"] = data["question"].apply(lambda x: nlp(x))

# view first question
example_question = data.question[0]
example_question_tokens = data.question_tokens[0]
print("full question :")
print(example_question)
print('-' * 20)
print("question tokens :")
for token in example_question_tokens:
	print(token)

# view POS tags for tokens in the first question
print('-' * 20)
print("the Part-of-speech tags for each token in the first question :")
for token in example_question_tokens:
	print(token.text, '|', token.pos_, '|', spacy.explain(token.pos_))
