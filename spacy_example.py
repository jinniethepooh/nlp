import spacy

nlp = spacy.load("en_core_web_sm")

# tokenization
sentence = nlp.tokenizer("we live in paris.")

# length of sentence
print("the number of tokens:", len(sentence))

# print individual words
print("tokens in sentence :")
for token in sentence:
	print(token)
