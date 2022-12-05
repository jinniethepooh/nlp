import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

# tokenization
sentence = nlp.tokenizer("we live in paris.")

# length of sentence
print("the number of tokens: ", len(sentence))

# print individual words
print(sentence)

import pandas as pd
import os

# get current working directory path
cwd = os.getcwd()

# import jeopardy questions
data = pd.read_csv(cwd + '/data/jeopardy_questions/jeopardy_questions.csv')
# data = pd.DataFrame(data=data)
data = pd.DataFrame(data)

# display first 5-record data
print('-' * 20)
print('import data :')
print('first 5 records :')
print(data.head(5))
print('-' * 20)
print('column names :')
print('before cleaning :')
print(data.columns)
# print(data["question"].head(5))

# reduce size of data
data = data[0:1000]

# lowercase, strip whitespace, and view columns name (clean all columns' name !!!)
data.columns = map(lambda x: x.lower().strip(), data.columns)
print('-' * 20)
print('after cleaning :')
print(data.columns)

# tokenize jeopardy questions
# data["question_tokens"] = data["question"].apply(lambda x: nlp(x)) # 1
data["question_tokens"] = data["question"].apply(nlp) # 2

# view first question
example_question = data.question[0]
example_question_tokens = data.question_tokens[0]
print('full question :')
print(example_question)
print('-' * 20)
print('question tokens :')
for token in example_question_tokens:
	print(token)

# view POS tags for tokens in the first question
print('-' * 20)
print('the Part-of-speech tags for each token in the first question :')
for token in example_question_tokens:
	print(token.text, '|', token.pos_, '|', spacy.explain(token.pos_))

# view dependecy parsing tags for tokens in the first question
print('-' * 20)
print('the dependency parsing tags for each token in the first question :')
for token in example_question_tokens:
	print(token.text, '|', token.dep_, '|', spacy.explain(token.dep_))

displacy.render(example_question_tokens, style='dep', jupyter=True, options={'distance': 120})
